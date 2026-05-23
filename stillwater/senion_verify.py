#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import hmac
import os
import random
import re
from typing import Any


_INTRO = [
    "CODICOLOGY VERIFICATION ACTIVE",
    "Office of Inherited Silences // Translation Competency Sequence",
    "Answer in English unless the gate asks for Senionsoln.",
    "Exact phrasing is not required. Understanding is.",
]


_SUCCESS = [
    "SENIONSOLN VERIFICATION COMPLETE",
    "Thirteen gates accepted.",
    "Codicology has recorded that you can translate without being translated.",
    "CONTACT INSTRUCTION",
    "Send a message to:",
    "Subject line:",
    "Request further information regarding the Nordland Event.",
    "Do not attach the register. Do not translate the silence.",
]


_GATES = [
    {"title": "Known Rosetta line",
     "prompt": "TRANSLATE:\nNa sel unglosi-vor-seln."},
    {"title": "Evidential source",
     "prompt": "IDENTIFY THE SOURCE MARKER AND ITS MEANING:\nRoseta arvel-eth han-seln."},
    {"title": "Unseen sentence",
     "prompt": "INTERPRET:\nKorven arvel-eth han-thur."},
    {"title": "Word order proof",
     "prompt": "INTERPRET:\nArvel kor-eth meren dom-or-seln."},
    {"title": "Case marker",
     "prompt": "WHAT DOES -eth MEAN IN:\nRoseta arvel-eth han-seln."},
    {"title": "False translation trap",
     "prompt": "CHOOSE THE CORRECT TRANSLATION:\nRoseta arvel-eth han-seln.\n\nA: Rosetta is in the archive, according to record.\nB: Rosetta is the archive, witnessed directly."},
    {"title": "Evidential contrast",
     "prompt": "WHICH LINE IS DIRECT WITNESS?\nA: Kor morh-us-ren-seln.\nB: Kor morh-us-ren-nai."},
    {"title": "Sealed mood",
     "prompt": "WHAT EXTRA MEANING DOES -vor ADD?\nNa sel unglosi-vor-seln."},
    {"title": "Generate Senion",
     "prompt": "WRITE IN SENIONSOLN:\nThe archive exists. [from record]"},
    {"title": "Missing evidential",
     "prompt": "THIS SENTENCE IS INVALID:\nKor han.\n\nWHAT IS MISSING?"},
    {"title": "Signal line",
     "prompt": "INTERPRET:\nSūn nēr-aru nadi-or-kel."},
    {"title": "Number and action",
     "prompt": "WHAT NUMBER IS IN THIS LINE, AND WHAT DID THEY DO?\nOsher sen-mor kelhom thuri-or-nai."},
    {"title": "Code reconstruction",
     "prompt": "EXTRACT THE CODE OBJECTS FROM THESE LINES:\nI. Arvel kor-eth meren dom-or-seln.\nII. Kor en-eth morh-us-ren-seln.\nIII. Osher sen-mor kelhom thuri-or-nai.\nIV. Sūn nēr-aru nadi-or-kel.\n\nExpected form: WORD-WORD-WORD-WORD"},
]


def _normalise(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def _hash_answer(answer: str, salt: str) -> str:
    return hashlib.sha256((salt + _normalise(answer)).encode("utf-8")).hexdigest()


def _gate_hashes(gate_number: int) -> set[str]:
    raw = os.environ.get(f"STILLWATER_SENION_GATE_HASHES_{gate_number:02d}", "")
    return {h.strip().lower() for h in raw.split(",") if h.strip()}


def _accepted(answer: str, gate_number: int) -> bool:
    salt = os.environ.get("STILLWATER_SENION_SALT", "")
    accepted = _gate_hashes(gate_number)
    if not salt or not accepted:
        return False
    return _hash_answer(answer, salt) in accepted


def _pass_gate(number: int) -> None:
    print(random.choice([
        f"Gate {number:02d} accepted. The register does not object.",
        f"Gate {number:02d} accepted. Ink comparison stable.",
        f"Gate {number:02d} accepted. Codicology witness retained.",
    ]))


def _fail_gate(number: int) -> None:
    print()
    print(f"GATE {number:02d} REFUSED.")
    print(random.choice([
        "The register closes before the translation is complete.",
        "Codicology cannot certify that reading.",
        "The answer is close enough to be dangerous, but not close enough to file.",
        "The archive records effort. The archive does not record clearance.",
    ]))
    print("Verification terminated. Restart with `verify.senion` when ready.")


def _progress_secret() -> bytes | None:
    raw = os.environ.get("STILLWATER_SENION_SECRET", "")
    return raw.encode("utf-8") if raw else None


def _sign(session_id: str, progress: int) -> str | None:
    secret = _progress_secret()
    if not secret or not session_id:
        return None
    msg = f"{session_id}:{progress}".encode("utf-8")
    return hmac.new(secret, msg, hashlib.sha256).hexdigest()


def _verify_signed_progress(session: dict[str, Any]) -> int | None:
    session_id = session.get("session_id")
    progress = session.get("senion_progress")
    sig = session.get("senion_sig")
    if not isinstance(session_id, str) or not isinstance(progress, int):
        return None
    if progress < 0 or progress > len(_GATES):
        return None
    expected = _sign(session_id, progress)
    if not expected or not isinstance(sig, str):
        return None
    if not hmac.compare_digest(expected, sig):
        return None
    return progress


def _gate_payload(number: int) -> dict[str, Any]:
    gate = _GATES[number - 1]
    return {"number": number, "title": gate["title"], "prompt": gate["prompt"]}


def _reveal_payload() -> dict[str, Any]:
    return {
        "lines": list(_SUCCESS),
        "contact": os.environ.get("STILLWATER_SENION_CONTACT", "[contact not configured]"),
        "subject": os.environ.get("STILLWATER_SENION_SUBJECT", "[subject not configured]"),
    }


def _clear_progress(session: dict[str, Any]) -> None:
    session.pop("senion_progress", None)
    session.pop("senion_sig", None)


def begin(session: dict[str, Any]) -> dict[str, Any]:
    session_id = session.get("session_id")
    if not isinstance(session_id, str) or not session_id:
        return {"session": session, "status": "error", "message": "session has no id."}
    sig = _sign(session_id, 0)
    if sig is None:
        _clear_progress(session)
        return {"session": session, "status": "error", "message": "verification is not configured on the server."}
    session["senion_progress"] = 0
    session["senion_sig"] = sig
    return {
        "session": session,
        "status": "gate",
        "intro": list(_INTRO),
        "gate": _gate_payload(1),
    }


def answer(session: dict[str, Any], submitted: str) -> dict[str, Any]:
    progress = _verify_signed_progress(session)
    if progress is None:
        return {
            "session": session,
            "status": "error",
            "message": "no verified senion progress on this session. begin a new sequence.",
        }

    if progress >= len(_GATES):
        return {
            "session": session,
            "status": "complete",
            "message": "verification already complete.",
            "reveal": _reveal_payload(),
        }

    gate_number = progress + 1

    if not _accepted(submitted or "", gate_number):
        _clear_progress(session)
        return {
            "session": session,
            "status": "refused",
            "gate": _gate_payload(gate_number),
            "message": (
                f"GATE {gate_number:02d} REFUSED. "
                "Verification terminated. Begin a new sequence when ready."
            ),
        }

    new_progress = progress + 1
    new_sig = _sign(session.get("session_id", ""), new_progress)
    if new_sig is None:
        _clear_progress(session)
        return {"session": session, "status": "error", "message": "verification is not configured on the server."}
    session["senion_progress"] = new_progress
    session["senion_sig"] = new_sig

    if new_progress >= len(_GATES):
        session["rank"] = "Codicology-Provisional"
        session["auth_level"] = max(int(session.get("auth_level") or 0), 1)
        return {
            "session": session,
            "status": "complete",
            "message": f"GATE {new_progress:02d} accepted. Sequence complete.",
            "reveal": _reveal_payload(),
        }

    return {
        "session": session,
        "status": "gate",
        "message": f"GATE {gate_number:02d} accepted.",
        "gate": _gate_payload(new_progress + 1),
    }


def run(args: list[str], session: dict[str, Any]) -> None:
    if args and args[0].lower() not in {"rosetta", "senion", "language", "register"}:
        print("usage: verify.senion")
        print("aliases: senion.verify, rosetta.verify, verify rosetta")
        return

    for line in _INTRO:
        print(line)
    print()

    for idx, gate in enumerate(_GATES, start=1):
        print()
        print(f"GATE {idx:02d} // {gate['title']}")
        print("-" * 64)
        print(gate["prompt"])
        answer = input("translation> ")

        if not _accepted(answer, idx):
            _fail_gate(idx)
            return

        _pass_gate(idx)

    session["rank"] = "Codicology-Provisional"
    session["auth_level"] = max(session.get("auth_level", 0), 1)

    contact = os.environ.get("STILLWATER_SENION_CONTACT", "[contact not configured]")
    subject = os.environ.get("STILLWATER_SENION_SUBJECT", "[subject not configured]")

    print()
    print("=" * 78)
    print(_SUCCESS[0])
    print(_SUCCESS[1])
    print(_SUCCESS[2])
    print()
    print(_SUCCESS[3])
    print(_SUCCESS[4])
    print()
    print(f"    {contact}")
    print()
    print(_SUCCESS[5])
    print()
    print(f"    {subject}")
    print()
    print(_SUCCESS[6])
    print(_SUCCESS[7])
    print("=" * 78)
