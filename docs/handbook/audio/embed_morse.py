#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import struct
import sys
import wave
from pathlib import Path

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...",
    ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-",
    '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
}


def read_wav(path: Path) -> tuple[list[list[float]], int]:
    with wave.open(str(path), "rb") as wav:
        channel_count = wav.getnchannels()
        sample_width = wav.getsampwidth()
        sample_rate = wav.getframerate()
        frame_count = wav.getnframes()
        compression = wav.getcomptype()
        raw = wav.readframes(frame_count)

    if compression != "NONE":
        raise ValueError("Only uncompressed PCM WAV input is supported.")
    if sample_width not in (1, 2, 3, 4):
        raise ValueError(f"Unsupported sample width: {sample_width} bytes")

    total_samples = frame_count * channel_count
    decoded: list[float] = []

    if sample_width == 1:
        decoded = [(b - 128) / 128.0 for b in raw]
    elif sample_width == 2:
        ints = struct.unpack("<" + "h" * total_samples, raw)
        decoded = [x / 32768.0 for x in ints]
    elif sample_width == 3:
        for i in range(0, len(raw), 3):
            value = int.from_bytes(raw[i:i + 3], "little", signed=False)
            if value & 0x800000:
                value -= 0x1000000
            decoded.append(value / 8388608.0)
    elif sample_width == 4:
        ints = struct.unpack("<" + "i" * total_samples, raw)
        decoded = [x / 2147483648.0 for x in ints]

    channels = [[] for _ in range(channel_count)]
    for index, sample in enumerate(decoded):
        channels[index % channel_count].append(sample)

    return channels, sample_rate


def write_wav(path: Path, channels: list[list[float]], sample_rate: int) -> None:
    channel_count = len(channels)
    frame_count = len(channels[0])
    path.parent.mkdir(parents=True, exist_ok=True)

    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(channel_count)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)

        frames = bytearray()
        for i in range(frame_count):
            for ch in range(channel_count):
                value = max(-1.0, min(1.0, channels[ch][i]))
                frames.extend(struct.pack("<h", int(value * 32767)))

        wav.writeframes(frames)


def rms(values: list[float]) -> float:
    if not values:
        return 0.0
    return math.sqrt(sum(v * v for v in values) / len(values))


def text_to_morse(message: str) -> list[str]:
    tokens: list[str] = []
    for word_index, word in enumerate(message.upper().split()):
        if word_index > 0:
            tokens.append("/")
        for char in word:
            code = MORSE.get(char)
            if code:
                tokens.append(code)
    return tokens


def generate_morse(
    message: str,
    sample_rate: int,
    frequency: float,
    wpm: float,
    amplitude: float,
    fade_ms: float,
) -> list[float]:
    unit_samples = max(1, int((1.2 / wpm) * sample_rate))
    fade_samples = max(1, int((fade_ms / 1000.0) * sample_rate))
    output: list[float] = []
    phase = 0.0
    phase_step = 2.0 * math.pi * frequency / sample_rate

    def add_silence(samples: int) -> None:
        output.extend([0.0] * samples)

    def add_tone(samples: int) -> None:
        nonlocal phase
        for i in range(samples):
            envelope = 1.0
            if i < fade_samples:
                envelope = i / fade_samples
            elif i > samples - fade_samples:
                envelope = max(0.0, (samples - i) / fade_samples)

            output.append(math.sin(phase) * amplitude * envelope)
            phase += phase_step
            if phase > math.tau:
                phase -= math.tau

    tokens = text_to_morse(message)
    for token_index, token in enumerate(tokens):
        if token == "/":
            add_silence(unit_samples * 7)
            continue

        for symbol_index, symbol in enumerate(token):
            add_tone(unit_samples if symbol == "." else unit_samples * 3)
            if symbol_index < len(token) - 1:
                add_silence(unit_samples)

        if token_index < len(tokens) - 1:
            add_silence(unit_samples * 3)

    return output


def overlay_once(channels: list[list[float]], morse: list[float], start_sample: int, pan: float) -> None:
    frame_count = len(channels[0])
    if start_sample >= frame_count:
        return

    if len(channels) == 1:
        gains = [1.0]
    else:
        left = math.cos((pan + 1.0) * math.pi / 4.0)
        right = math.sin((pan + 1.0) * math.pi / 4.0)
        gains = [left, right] + [0.5] * (len(channels) - 2)

    length = min(len(morse), frame_count - start_sample)
    for i in range(length):
        tone = morse[i]
        if tone == 0.0:
            continue
        target = start_sample + i
        for ch in range(len(channels)):
            channels[ch][target] += tone * gains[ch]


def peak_abs(channels: list[list[float]]) -> float:
    return max(max(abs(sample) for sample in channel) for channel in channels if channel)


def scale_if_needed(channels: list[list[float]], ceiling: float = 0.98) -> float:
    peak = peak_abs(channels)
    if peak <= ceiling:
        return 1.0

    scale = ceiling / peak
    for ch, channel in enumerate(channels):
        channels[ch] = [sample * scale for sample in channel]
    return scale


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Embed a quiet, low-pitched audible Morse code message into a WAV file."
    )
    parser.add_argument("input", type=Path, help="Input uncompressed PCM WAV file")
    parser.add_argument("output", type=Path, help="Output WAV file")
    parser.add_argument("message", help="Message to convert to Morse")
    parser.add_argument("--freq", type=float, default=180.0, help="Tone frequency in Hz. Default: 180")
    parser.add_argument("--wpm", type=float, default=12.0, help="Morse speed. Default: 12")
    parser.add_argument("--volume-db", type=float, default=-24.0, help="Morse RMS relative to source RMS. Default: -24")
    parser.add_argument("--offset", type=float, default=3.0, help="Seconds before Morse starts. Default: 3")
    parser.add_argument("--fade-ms", type=float, default=8.0, help="Tone fade to avoid clicks. Default: 8")
    parser.add_argument("--pan", type=float, default=0.0, help="Stereo pan: -1 left, 0 centre, 1 right. Default: 0")
    parser.add_argument("--loop", action="store_true", help="Repeat Morse across the full file")
    parser.add_argument("--gap", type=float, default=6.0, help="Seconds between looped messages. Default: 6")
    parser.add_argument("--min-volume", type=float, default=0.006, help="Minimum tone amplitude. Default: 0.006")
    parser.add_argument("--max-volume", type=float, default=0.08, help="Maximum tone amplitude. Default: 0.08")
    args = parser.parse_args()

    if args.wpm <= 0:
        print("--wpm must be greater than 0.", file=sys.stderr)
        return 2
    if not -1.0 <= args.pan <= 1.0:
        print("--pan must be between -1 and 1.", file=sys.stderr)
        return 2

    channels, sample_rate = read_wav(args.input)
    frame_count = len(channels[0])
    source_samples = [sample for channel in channels for sample in channel]
    source_rms = rms(source_samples)

    # Target a distant but audible level relative to the source RMS.
    target_rms = source_rms * (10 ** (args.volume_db / 20.0))
    amplitude = target_rms * math.sqrt(2.0)
    amplitude = max(args.min_volume, min(args.max_volume, amplitude))

    morse = generate_morse(
        message=args.message,
        sample_rate=sample_rate,
        frequency=args.freq,
        wpm=args.wpm,
        amplitude=amplitude,
        fade_ms=args.fade_ms,
    )

    start_sample = int(args.offset * sample_rate)
    if args.loop:
        cursor = start_sample
        gap_samples = int(args.gap * sample_rate)
        while cursor < frame_count:
            overlay_once(channels, morse, cursor, args.pan)
            cursor += len(morse) + gap_samples
    else:
        overlay_once(channels, morse, start_sample, args.pan)

    clip_scale = scale_if_needed(channels)
    write_wav(args.output, channels, sample_rate)

    print("Morse embedded successfully.")
    print(f"Input:       {args.input}")
    print(f"Output:      {args.output}")
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Duration:    {frame_count / sample_rate:.2f}s")
    print(f"Frequency:   {args.freq} Hz")
    print(f"WPM:         {args.wpm}")
    print(f"Volume:      {args.volume_db} dB relative to source RMS")
    print(f"Amplitude:   {amplitude:.5f}")
    print(f"Looped:      {args.loop}")
    print(f"Clip scale:  {clip_scale:.5f}")
    print("Morse:       " + " ".join(text_to_morse(args.message)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
