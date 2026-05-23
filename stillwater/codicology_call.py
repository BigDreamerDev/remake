from __future__ import annotations

import html
import json
import random
import time
import webbrowser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RUNTIME_DIR = BASE_DIR / ".stillwater_runtime"

COMMANDS = (
    "call.codicology",
    "codicology.call",
    "dial.codicology",
    "switchboard.codicology",
)

import base64

_ROUTE_DATA = {
    "extension": "Hv",
    "kind": "VRd9_Zv",
    "kind_alt": "Q&%lPRYU",
    "item": "F*E",
}

def _route_value(name: str) -> str:
    return base64.b85decode(_ROUTE_DATA[name].encode("ascii")).decode("utf-8")
SEGMENT_COUNT = 14

AUDIO_EXTENSIONS = ("mp3", "wav", "ogg", "m4a", "aac", "flac")

SEGMENT_NAME_PATTERNS = (
    "SW-AUD-014_{index:02d}.{ext}",
    "SW-AUD-014-{index:02d}.{ext}",
    "SW-AUD-014.{index:02d}.{ext}",
    "SW-AUD-014_part_{index:02d}.{ext}",
    "SW-AUD-014-part-{index:02d}.{ext}",
    "SW-AUD-014_segment_{index:02d}.{ext}",
    "SW-AUD-014-segment-{index:02d}.{ext}",
    "SW-AUD-014_part{index:02d}.{ext}",
    "SW-AUD-014-part{index:02d}.{ext}",
    "SW-AUD-014_segment{index:02d}.{ext}",
    "SW-AUD-014-segment{index:02d}.{ext}",
    "SW-AUD-14_{index:02d}.{ext}",
    "SW-AUD-14-{index:02d}.{ext}",
    "SW-AUD-14.{index:02d}.{ext}",
    "SW-AUD-14_part_{index:02d}.{ext}",
    "SW-AUD-14-part-{index:02d}.{ext}",
    "SW-AUD-14_segment_{index:02d}.{ext}",
    "SW-AUD-14-segment-{index:02d}.{ext}",
    "SW-AUD-14_part{index:02d}.{ext}",
    "SW-AUD-14-part{index:02d}.{ext}",
    "SW-AUD-14_segment{index:02d}.{ext}",
    "SW-AUD-14-segment{index:02d}.{ext}",
    "SW-AUD-{index:02d}.{ext}",
)

AUDIO_SEARCH_DIRS = (
    "docs/handbook/audio",
    "docs/handbook/audio/SW-AUD-014",
    "docs/audio",
    "docs/sealed/audio",
    "docs/audio/SW-AUD-014",
    "docs/sealed/audio/SW-AUD-014",
)

READER_MARKER = "__OPEN_CODICOLOGY_CALL__"

SWITCHBOARD_ART = r"""
        ╔════════════════════════════════════════════════════════════╗
        ║          STILLWATER FOUNDATION LOWER SWITCHBOARD          ║
        ║             Codicology Wing / Archive Integrity            ║
        ╠════════════════════════════════════════════════════════════╣
        ║        .-----------------.        .----------------.       ║
        ║        |  LINE: PRESENT  |        |  OFFICE: ELSE  |       ║
        ║        '--------.--------'        '--------.-------'       ║
        ║                 |                          |               ║
        ║              ___|___                    ___|___            ║
        ║             /       \                  /       \           ║
        ║            |   0 0   |~~~~~~~~~~~~~~~~|   0 0   |          ║
        ║             \__ _ __/                  \__ _ __/           ║
        ║                |_|                        |_|              ║
        ║        fourteen rings             one lower receiver        ║
        ╚════════════════════════════════════════════════════════════╝
"""

TERMINATIONS = [
    "CALL TERMINATED. The receiver was placed back before it rang.",
    "CALL TERMINATED. The office heard the wrong request and folded the line.",
    "CALL TERMINATED. Lower switchboard has filed your attempt under almost.",
    "CALL TERMINATED. The line is still present. You are not.",
    "CALL TERMINATED. Codicology does not accept corrected mistakes by phone.",
]

ROUTING_LINES = [
    "routing request through wet copy intake...",
    "checking whether the line is still the same line...",
    "asking the archive to stop using the receiver as a bookmark...",
    "lower switchboard acknowledges a shape compatible with a call...",
    "operator unavailable. this is expected.",
    "fourteen archive fragments report present in the wrong order...",
]


def command_names() -> tuple[str, ...]:
    return tuple(sorted(COMMANDS))


def help_text(show_all: bool = False) -> str:
    lines = [
        "Codicology switchboard:",
        " contact.office codicology     Contact Codicology through the lower switchboard",
        " call.codicology               Alias for Codicology switchboard",
    ]
    if show_all:
        lines.extend([
            " switchboard.codicology        Alias for Codicology switchboard",
            " dial.codicology               Alias for Codicology switchboard",
            " codicology.call               Alias for Codicology switchboard",
        ])
    return "\n".join(lines)


def _pause(seconds: float = 0.25) -> None:
    time.sleep(seconds)


def _ask(prompt: str) -> str | None:
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None


def _terminate(reason: str | None = None) -> None:
    if reason:
        print(reason)
    print(random.choice(TERMINATIONS))


def _normalise(value: str | None) -> str:
    return (value or "").strip().lower().replace("sw-aud-", "").lstrip("0")


def _candidate_paths_for_segment(index: int) -> list[Path]:
    candidates: list[Path] = []
    for directory in AUDIO_SEARCH_DIRS:
        base_dir = BASE_DIR / directory
        for pattern in SEGMENT_NAME_PATTERNS:
            for ext in AUDIO_EXTENSIONS:
                candidates.append(base_dir / pattern.format(index=index, ext=ext))
    return candidates


def _find_segment(index: int) -> Path | None:
    for candidate in _candidate_paths_for_segment(index):
        if candidate.exists() and candidate.is_file():
            return candidate.resolve()
    return None


def _find_audio_segments() -> tuple[list[Path], list[int]]:
    found: list[Path] = []
    missing: list[int] = []
    for index in range(1, SEGMENT_COUNT + 1):
        segment = _find_segment(index)
        if segment is None:
            missing.append(index)
        else:
            found.append(segment)
    return found, missing


def _expected_examples() -> list[str]:
    return [
        "docs/audio/SW-AUD-014_01.mp3",
        "docs/audio/SW-AUD-014_02.mp3",
        "...",
        "docs/audio/SW-AUD-014_14.mp3",
    ]


def _relative(path: Path) -> str:
    try:
        return str(path.relative_to(BASE_DIR))
    except ValueError:
        return str(path)


def _html_player(audio_segments: list[Path]) -> Path:
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    player = RUNTIME_DIR / "SW-AUD-014_segmented_loop_player.html"
    playlist = [
        {
            "index": i + 1,
            "name": path.name,
            "relative": _relative(path),
            "uri": path.as_uri(),
        }
        for i, path in enumerate(audio_segments)
    ]
    title = "SW-AUD-014 // segmented hold channel"
    playlist_json = json.dumps(playlist)

    player.write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>
html, body {{
    margin: 0;
    min-height: 100%;
    background: #040807;
    color: #b7c9bf;
    font-family: Consolas, Monaco, monospace;
}}
main {{
    max-width: 900px;
    margin: 6vh auto;
    padding: 32px;
    border: 1px solid #31443b;
    box-shadow: 0 0 48px rgba(140, 190, 170, 0.08);
    background:
        radial-gradient(circle at 30% 0%, rgba(91, 122, 112, 0.10), transparent 32%),
        linear-gradient(180deg, #08100e, #030504);
}}
pre {{
    color: #d5e3dc;
    line-height: 1.1;
}}
.notice {{ color: #8aa79b; }}
#segment {{ color: #dce9e2; }}
audio {{ width: 100%; margin-top: 24px; }}
button {{
    background: #0c1714;
    color: #d5e3dc;
    border: 1px solid #31443b;
    padding: 8px 12px;
    font-family: inherit;
    cursor: pointer;
}}
button:hover {{ background: #12211d; }}
ol {{ columns: 2; color: #86a096; }}
.active {{ color: #dce9e2; }}
</style>
</head>
<body>
<main>
<pre>
STILLWATER FOUNDATION
LOWER SWITCHBOARD / CODICOLOGY WING

LINE       : PRESENT
EXTENSION  : 7
TYPE       : AUDIO
ID         : 014
SEGMENTS   : 14
STATUS     : HOLD CHANNEL OPEN
</pre>

<p class="notice">The recovered lobby channel is fragmented. The switchboard will play each segment in order, then return to the first.</p>
<p>Current segment: <span id="segment">waiting</span></p>
<audio id="sw-audio-014" controls autoplay></audio>
<p class="notice" id="status">attempting playback...</p>
<p>
    <button id="restart">restart sequence</button>
    <button id="next">advance one segment</button>
</p>
<ol id="playlist"></ol>
</main>
<script>
const playlist = {playlist_json};
const audio = document.getElementById("sw-audio-014");
const status = document.getElementById("status");
const segment = document.getElementById("segment");
const list = document.getElementById("playlist");
const restart = document.getElementById("restart");
const next = document.getElementById("next");
let current = 0;

function renderList() {{
    list.innerHTML = "";
    playlist.forEach((item, index) => {{
        const li = document.createElement("li");
        li.textContent = String(item.index).padStart(2, "0") + " // " + item.name;
        if (index === current) {{ li.className = "active"; }}
        list.appendChild(li);
    }});
}}

function loadSegment(index, shouldPlay = true) {{
    current = ((index % playlist.length) + playlist.length) % playlist.length;
    const item = playlist[current];
    audio.src = item.uri;
    segment.textContent = String(item.index).padStart(2, "0") + " / 14";
    status.textContent = "loaded " + item.relative;
    renderList();
    if (shouldPlay) {{
        audio.play().then(() => {{
            status.textContent = "playing segment " + String(item.index).padStart(2, "0") + " / 14";
        }}).catch(() => {{
            status.textContent = "browser blocked autoplay; press play. sequence remains armed.";
        }});
    }}
}}

audio.addEventListener("ended", () => {{ loadSegment(current + 1, true); }});
audio.addEventListener("error", () => {{
    status.textContent = "segment failed to render; advancing as if the archive swallowed it.";
    setTimeout(() => loadSegment(current + 1, true), 1200);
}});
restart.addEventListener("click", () => {{ loadSegment(0, true); }});
next.addEventListener("click", () => {{ loadSegment(current + 1, true); }});
loadSegment(0, true);
</script>
</body>
</html>
""", encoding="utf-8")
    return player


def _open_segment_player(audio_segments: list[Path]) -> None:
    player = _html_player(audio_segments)
    webbrowser.open(player.as_uri())


# ── web-flow API (used by server.py) ──────────────────────────────────────
import hashlib
import hmac
import os


_STEPS = (
    {"key": "extension",
     "prompt": "DIAL EXTENSION:",
     "hint": "// the codicology line carries a single digit. //",
     "expected_keys": ("extension",)},
    {"key": "record_type",
     "prompt": "RECORD TYPE:",
     "hint": "// audio / video / textual / object — the line accepts one kind. //",
     "expected_keys": ("kind", "kind_alt")},
    {"key": "audio_id",
     "prompt": "AUDIO ID:",
     "hint": "// the file's number in the SW-AUD register. //",
     "expected_keys": ("item",)},
)


def _progress_secret() -> bytes | None:
    pw = os.environ.get("STILLWATER_COMSHELL_PASSWORD", "")
    return pw.encode("utf-8") if pw else None


def _sign(session_id: str, progress: int) -> str | None:
    secret = _progress_secret()
    if not secret or not session_id:
        return None
    msg = f"codicology:{session_id}:{progress}".encode("utf-8")
    return hmac.new(secret, msg, hashlib.sha256).hexdigest()


def _verify_signed_progress(session: dict) -> int | None:
    session_id = session.get("session_id")
    progress = session.get("codicology_progress")
    sig = session.get("codicology_sig")
    if not isinstance(session_id, str) or not isinstance(progress, int):
        return None
    if progress < 0 or progress > len(_STEPS):
        return None
    expected = _sign(session_id, progress)
    if not expected or not isinstance(sig, str):
        return None
    if not hmac.compare_digest(expected, sig):
        return None
    return progress


def _clear_progress(session: dict) -> None:
    session.pop("codicology_progress", None)
    session.pop("codicology_sig", None)


def _accepts(step_index: int, submitted: str) -> bool:
    if step_index < 0 or step_index >= len(_STEPS):
        return False
    step = _STEPS[step_index]
    candidate = _normalise(submitted)
    return any(
        candidate == _normalise(_route_value(key))
        for key in step["expected_keys"]
    )


def _step_payload(step_index: int) -> dict:
    step = _STEPS[step_index]
    return {
        "step": step_index + 1,
        "total": len(_STEPS),
        "key": step["key"],
        "prompt": step["prompt"],
        "hint": step["hint"],
    }


def has_verified_progress(session: dict) -> bool:
    """True if the session has completed the routing handshake."""
    progress = _verify_signed_progress(session)
    return progress == len(_STEPS)


def begin(session: dict) -> dict:
    """Start a new codicology call. Returns the first routing prompt."""
    session_id = session.get("session_id")
    if not isinstance(session_id, str) or not session_id:
        return {"session": session, "status": "error", "message": "session has no id."}
    sig = _sign(session_id, 0)
    if sig is None:
        _clear_progress(session)
        return {"session": session, "status": "error", "message": "call routing not configured on the server."}
    session["codicology_progress"] = 0
    session["codicology_sig"] = sig
    return {
        "session": session,
        "status": "step",
        "intro": [
            "STILLWATER FOUNDATION // LOWER SWITCHBOARD",
            "Codicology Wing / Archive Integrity",
            "Codicology does not accept direct verbal requests.",
            "The switchboard will accept one route. All other routes terminate.",
        ],
        "step": _step_payload(0),
    }


def answer(session: dict, submitted: str) -> dict:
    """Submit a value for the current routing step."""
    progress = _verify_signed_progress(session)
    if progress is None:
        return {"session": session, "status": "error",
                "message": "no verified call in progress. begin a new call."}

    if progress >= len(_STEPS):
        return {"session": session, "status": "complete",
                "message": "call already routed.", "segments": _segments_payload()}

    step_index = progress
    if not _accepts(step_index, submitted or ""):
        _clear_progress(session)
        step = _STEPS[step_index]
        return {
            "session": session,
            "status": "refused",
            "step": _step_payload(step_index),
            "message": (
                f"{step['key'].upper()} MISMATCH. " + random.choice(TERMINATIONS)
            ),
        }

    new_progress = progress + 1
    new_sig = _sign(session.get("session_id", ""), new_progress)
    if new_sig is None:
        _clear_progress(session)
        return {"session": session, "status": "error",
                "message": "call routing not configured on the server."}
    session["codicology_progress"] = new_progress
    session["codicology_sig"] = new_sig

    if new_progress >= len(_STEPS):
        return {
            "session": session,
            "status": "complete",
            "message": "archive channel located. fragmented hold channel open.",
            "segments": _segments_payload(),
        }

    return {
        "session": session,
        "status": "step",
        "message": f"{_STEPS[step_index]['key']} accepted.",
        "step": _step_payload(new_progress),
    }


def available_segments() -> list[Path]:
    """Return any SW-AUD audio segments found on disk, in index order."""
    segments: list[tuple[int, Path]] = []
    for index in range(1, SEGMENT_COUNT + 1):
        path = _find_segment(index)
        if path is not None:
            segments.append((index, path))
    return [path for _, path in segments]


def _segments_payload() -> list[dict]:
    paths = available_segments()
    return [
        {
            "index": i + 1,
            "name": path.name,
            "relative": _relative(path),
        }
        for i, path in enumerate(paths)
    ]


def segments_json(session: dict) -> dict:
    """Return the playlist if the session has completed the call routing."""
    if not has_verified_progress(session):
        return {"ok": False, "error": "call routing not verified on this session."}
    paths = available_segments()
    return {
        "ok": True,
        "segments": _segments_payload(),
        "count": len(paths),
    }


def start(session: dict | None = None) -> None:
    print(SWITCHBOARD_ART)
    print("Codicology does not accept direct verbal requests.")
    print("The switchboard will accept one route. All other routes terminate.")
    print()

    for line in random.sample(ROUTING_LINES, k=3):
        print(line)
        _pause(0.35)

    print()
    extension = _ask("dial extension: ")
    if _normalise(extension) != _route_value("extension"):
        _terminate("extension mismatch. no such desk is willing to be found from here.")
        return

    print("extension accepted.")
    _pause(0.3)
    print("the receiver becomes colder.")
    print()

    record_type = _ask("record type: ")
    if _normalise(record_type) not in {_normalise(_route_value("kind")), _normalise(_route_value("kind_alt"))}:
        _terminate("request type mismatch. codicology only accepts this line in one shape.")
        return

    print("audio route accepted.")
    _pause(0.3)
    print("retrieving archive channel index...")
    print()

    archive_id = _ask("audio id: ")
    if _normalise(archive_id) != _route_value("item"):
        _terminate("archive id mismatch. the wrong file answered first.")
        return

    print("archive channel located.")
    _pause(0.3)
    print("fragmented hold channel requested.")
    _pause(0.5)

    audio_segments, missing = _find_audio_segments()
    if missing:
        print("AUDIO SEGMENT SET INCOMPLETE.")
        print(f"Expected {SEGMENT_COUNT} segments. Mounted {len(audio_segments)}.")
        print("Missing segment numbers:")
        print("  " + ", ".join(f"{index:02d}" for index in missing))
        print()
        print("Recommended names:")
        for example in _expected_examples():
            print(f"  {example}")
        print()
        print("The call remains connected to a silent fragment.")
        return

    _open_segment_player(audio_segments)
    print("playing segmented archive channel:")
    for path in audio_segments:
        print(f"  {_relative(path)}")
    print()
    print("sequence: 01 → 02 → 03 → ... → 14 → 01")
    print("if the browser blocks autoplay, press play once. sequence remains armed.")
    print("line status: open / segmented / listening from below")
