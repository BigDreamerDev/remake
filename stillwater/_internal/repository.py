from __future__ import annotations

import os


def get_endpoint(auth_key: str) -> str:
    if not auth_key:
        return "[no key supplied]"

    from stillwater import auth as _auth
    if not _auth.verify(auth_key):
        return "[decoding failed — key mismatch]"

    endpoint = os.environ.get("STILLWATER_PCT90156_ENDPOINT")
    if not endpoint:
        return "[endpoint not configured]"
    return endpoint
