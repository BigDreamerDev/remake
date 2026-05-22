









from typing import Sequence



WATER_DENSITY = 999.972


CLASSIFICATIONS = {
    "ankle":    (0.00, 0.15),
    "shallow":  (0.15, 0.60),
    "moderate": (0.60, 1.50),
    "deep":     (1.50, 5.00),
    "abyssal":  (5.00, float("inf")),
}


def classify_depth(depth_m: float) -> str:

    for label, (lo, hi) in CLASSIFICATIONS.items():
        if lo <= depth_m < hi:
            return label
    return "out-of-range"


def static_pressure(depth_m: float) -> float:

    g = 9.80665  
    return WATER_DENSITY * g * depth_m


def mean_depth(readings: Sequence[float]) -> float:





    valid = [r for r in readings if r >= 0]
    if not valid:
        return 0.0
    return sum(valid) / len(valid)
