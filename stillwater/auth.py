from __future__ import annotations

import getpass
import hmac
import os


def _normalised_comshell(submitted: str) -> str:
    return (submitted or "").strip()


def verify_comshell_password(submitted: str) -> bool:
    expected = os.environ.get("STILLWATER_COMSHELL_PASSWORD")
    if not expected or not submitted:
        return False
    return hmac.compare_digest(
        _normalised_comshell(submitted),
        expected.strip(),
    )


def require_comshell_password(max_attempts: int = 3) -> bool:
    print("comShell access requires operator verification.")
    for attempt in range(1, max_attempts + 1):
        try:
            submitted = getpass.getpass("operator phrase: ")
        except Exception:
            submitted = input("operator phrase: ")

        if verify_comshell_password(submitted):
            print("verification accepted.")
            return True

        remaining = max_attempts - attempt
        if remaining:
            print(f"verification failed. {remaining} attempt(s) remaining.")
        else:
            print("verification failed.")

    print("comShell access denied.")
    return False


def _normalised_restricted(submitted: str) -> str:
    return (submitted or "").strip().lower()


def verify(submitted: str) -> bool:
    expected = os.environ.get("STILLWATER_RESTRICTED_CODE")
    if not expected or not submitted:
        return False
    return hmac.compare_digest(
        _normalised_restricted(submitted),
        _normalised_restricted(expected),
    )


def required_rank() -> str:
    return "[restricted]"
