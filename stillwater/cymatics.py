












from typing import Iterable


SAMPLE_RATE = 44100
DEFAULT_THRESHOLD = 0.0014  


BANDS = {
    "subaural":     (0,     20),
    "Class-I":      (20,    60),
    "Class-II":     (60,    200),
    "Class-III":    (200,   2000),
    "Class-IV":     (2000,  20000),
}


def detect_sustained_tone(samples, threshold=DEFAULT_THRESHOLD):

    above = 0
    for s in samples:
        if abs(s) > threshold:
            above += 1
            if above > 100:
                return True
        else:
            above = 0
    return False


def classify_frequency(frequency: float) -> str:

    for label, (lo, hi) in BANDS.items():
        if lo <= frequency < hi:
            return label
    return "out-of-band"


def estimate_room_resonance(volume_m3: float, surface_m2: float) -> float:





    if volume_m3 <= 0:
        return 0.0
    return 2000.0 * ((surface_m2 / volume_m3) ** 0.5)
