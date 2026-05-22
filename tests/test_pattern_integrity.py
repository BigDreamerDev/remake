

from stillwater.pattern_integrity import current_status, detect_drift


def test_status_nominal_by_default():
    assert current_status() == "NOMINAL"


def test_no_drift_with_few_samples():
    assert detect_drift([1.0, 1.1]) is False


def test_detect_drift_monotonic():
    samples = [1.0, 1.0, 1.0, 1.0, 2.0, 2.1, 2.2]
    assert detect_drift(samples) is True
