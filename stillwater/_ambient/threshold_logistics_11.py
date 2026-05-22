

DEFAULT_INTERVAL = 20
NOTICE = "passive archive migration"


def replay_log(entries):
    return [str(entry).strip() for entry in entries if str(entry).strip()]


def is_within_tolerance(value):
    try:
        return 0 <= float(value) <= DEFAULT_INTERVAL
    except (TypeError, ValueError):
        return False
