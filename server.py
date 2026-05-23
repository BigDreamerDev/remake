from __future__ import annotations
import hashlib
import hmac
import json
import os
import random
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()

from stillwater import auth, comshell_extra, debrief, egress, forms, nodes, pattern_integrity, senion_verify
from stillwater._internal import repository

try:
    from stillwater import document_browser
except Exception:
    document_browser = None

try:
    from stillwater import codicology_call
except Exception:
    codicology_call = None

app = Flask(__name__)

# Replace with your actual GitHub Pages URL once deployed
CORS(app, origins=[
    "https://<your-github-username>.github.io",
    "http://localhost:8080",  # for local testing
])

# ── session store (in-memory, per-request — stateless is fine for a REPL) ──
# The frontend sends session state with every request and gets it back updated.

def make_session():
    return {
        "rank": "Trainee",
        "auth_level": 0,
        "auth_key": None,
        "session_id": f"SW-{random.randint(10000,99999)}-{random.randint(100,999)}",
        "node": random.choice(["Δ-04","Δ-04","྾2-A","North Archive","West Stair"]),
        "banner_variant": random.randint(100,999),
    }


def _comshell_sign(session_id: str) -> str | None:
    pw = os.environ.get("STILLWATER_COMSHELL_PASSWORD", "")
    if not pw or not session_id:
        return None
    return hmac.new(pw.encode("utf-8"), session_id.encode("utf-8"), hashlib.sha256).hexdigest()


def _is_comshell_verified(session: dict) -> bool:
    sig = session.get("comshell_sig")
    if not isinstance(sig, str):
        return False
    expected = _comshell_sign(session.get("session_id", ""))
    if not expected:
        return False
    return hmac.compare_digest(expected, sig)


def _unverified_response(payload: dict, status: int = 403):
    return jsonify(payload), status


@app.route("/api/command", methods=["POST"])
def command():
    data = request.get_json(force=True)
    raw: str = data.get("raw", "").strip()
    session: dict = data.get("session", make_session())

    if not _is_comshell_verified(session):
        return _unverified_response({
            "output": "comShell access requires operator verification.",
            "session": session,
        })

    output, session = dispatch(raw, session)
    return jsonify({"output": output, "session": session})


@app.route("/api/session", methods=["GET"])
def new_session():
    return jsonify(make_session())


@app.route("/api/auth/comshell", methods=["POST"])
def auth_comshell():
    data = request.get_json(force=True) or {}
    session = data.get("session") or make_session()
    submitted = data.get("password", "")
    if not isinstance(submitted, str):
        submitted = str(submitted)

    if not auth.verify_comshell_password(submitted):
        session.pop("comshell_verified", None)
        session.pop("comshell_sig", None)
        return jsonify({"ok": False, "session": session, "message": "verification failed."})

    sig = _comshell_sign(session.get("session_id", ""))
    if not sig:
        return jsonify({"ok": False, "session": session, "message": "verification not configured on the server."})

    session["comshell_verified"] = True
    session["comshell_sig"] = sig
    return jsonify({"ok": True, "session": session})


@app.route("/api/senion/begin", methods=["POST"])
def senion_begin():
    data = request.get_json(force=True) or {}
    session = data.get("session") or make_session()
    if not _is_comshell_verified(session):
        return _unverified_response({
            "status": "error",
            "message": "comShell access requires operator verification.",
            "session": session,
        })
    return jsonify(senion_verify.begin(session))


@app.route("/api/senion/answer", methods=["POST"])
def senion_answer():
    data = request.get_json(force=True) or {}
    session = data.get("session") or make_session()
    if not _is_comshell_verified(session):
        return _unverified_response({
            "status": "error",
            "message": "comShell access requires operator verification.",
            "session": session,
        })
    submitted = data.get("answer", "")
    if not isinstance(submitted, str):
        submitted = str(submitted)
    return jsonify(senion_verify.answer(session, submitted))


@app.route("/health", methods=["GET"])
def health():
    return "ok", 200


# ── command dispatch (mirrors main.py) ────────────────────────────────────────

def dispatch(raw: str, session: dict) -> tuple[str, dict]:
    import shlex
    if not raw:
        msg = None
        if random.random() < 0.18:
            msg = random.choice([
                "The terminal accepts your silence and files it under Form S-00.",
                "No command entered. The corridor does not count this as hesitation.",
                "Silence received. No further action, except storage.",
            ])
        return (msg or ""), session

    try:
        parts = shlex.split(raw)
    except ValueError as e:
        return f"Input refused: {e}\nThe terminal dislikes unmatched quotation marks. So do the rooms.", session

    if not parts:
        return "", session

    cmd = parts[0].lower()
    args = parts[1:]

    COMMANDS = {
        "help":                    lambda a: cmd_help(a),
        "whoami":                  lambda a: cmd_whoami(a, session),
        "status":                  lambda a: cmd_status(a),
        "ls":                      lambda a: cmd_ls(a),
        "ping":                    lambda a: cmd_ping(a),
        "auth":                    lambda a: cmd_auth(a, session),
        "egress.recall":           lambda a: cmd_egress_recall(a),
        "debrief.schedule":        lambda a: cmd_debrief_schedule(a),
        "pct90156":                lambda a: cmd_pct90156(a, session),
        "verify.senion":           lambda a: cmd_senion(a, session),
        "senion.verify":           lambda a: cmd_senion(a, session),
        "rosetta.verify":          lambda a: cmd_senion(a, session),
        "verify":                  lambda a: cmd_senion(a, session),
        "contact.office":          lambda a: cmd_contact_office(a, session),
        "call.codicology":         lambda a: cmd_codicology(session),
        "codicology.call":         lambda a: cmd_codicology(session),
        "switchboard.codicology":  lambda a: cmd_codicology(session),
        "dial.codicology":         lambda a: cmd_codicology(session),
        "clear":                   lambda a: "__CLEAR__",
        "cls":                     lambda a: "__CLEAR__",
        "exit":                    lambda a: "__EXIT__",
        "quit":                    lambda a: "__EXIT__",
    }

    for name in comshell_extra.command_names():
        COMMANDS.setdefault(name.lower(), lambda a, n=name: comshell_extra.run(n, a, session))
    if document_browser:
        for name in document_browser.command_names():
            COMMANDS.setdefault(name.lower(), lambda a, n=name: document_browser.run(n, a, session))
    if codicology_call:
        for name in codicology_call.command_names():
            COMMANDS.setdefault(name.lower(), lambda a: cmd_codicology(session))

    if cmd in COMMANDS:
        try:
            result = COMMANDS[cmd](args)
            return result, session
        except SystemExit:
            return "__EXIT__", session
        except Exception as e:
            err = random.choice([
                f"Process failed: {e}\n The process ran correctly for 4.2 seconds before it failed.",
                f"Handler returned an error: {e}\n The handler also returned something that is not an error.",
                f"Execution error: {e}\n This error has occurred before. The previous session is still marked ONGOING.",
            ])
            return err + f"\n ({forms.lookup('anomaly')} recommended)", session
    else:
        unknown = random.choice([
            f"'{cmd}' is not in the command index.\n '{cmd}' is in the incident index.\n These are different indexes.",
            f"'{cmd}' is not a permitted command at your rank.\n '{cmd}' is not a permitted command at any rank currently held by a living employee.",
            f"'{cmd}' timed out.\n A command cannot time out at this terminal.\n Pattern Integrity has not responded.",
        ])
        hint = random.choice([" Try 'help'.", " Try 'help all', unless you dislike long corridors."])
        return unknown + "\n" + hint, session


# ── individual command implementations ───────────────────────────────────────

def cmd_help(args):
    show_all = bool(args and args[0].lower() == "all")
    blocks = [comshell_extra.help_text(show_all=show_all)]
    if document_browser:
        blocks.append(document_browser.help_text(show_all=show_all))
    if codicology_call:
        blocks.append(codicology_call.help_text(show_all=show_all))
    blocks.append("Senion verification: verify.senion / senion.verify / verify rosetta")
    return "\n\n".join(b for b in blocks if b)

def cmd_whoami(args, session):
    variants = [
        [" user : anon", f" rank : {session['rank']}", f" session : {session['session_id']}", " origin : unverified"],
        [f" anon@{session['node']}", f" clearance: {session['rank']}", " note: you have been in this corridor before."],
        [" identity query returned one result.", " that result is also a query.", f" rank on file: {session['rank']}"],
    ]
    return "\n".join(random.choice(variants))

def cmd_status(args):
    prefix = random.choice([
        "Status request logged by Pattern Integrity.",
        "Status returned from the nearest node willing to answer.",
    ])
    return prefix + "\n" + pattern_integrity.full_report()

def cmd_ls(args):
    out = nodes.list_nodes()
    if random.random() < 0.45:
        out += "\n" + random.choice([
            "Note: one node is responding from a location inconsistent with its designation.",
            "Note: a node listed here may be listed here twice. Both listings are correct.",
        ])
    return out

def cmd_ping(args):
    if not args:
        return random.choice([" usage: ping <node>", " ping requires a node designation, even if the node already knows."])
    out = nodes.ping(args[0])
    if random.random() < 0.35:
        out += "\n " + random.choice([
            "round-trip variance accepted under Quiet Systems Policy.",
            "latency witness unavailable; result preserved anyway.",
        ])
    return out

def cmd_auth(args, session):
    if not args:
        return random.choice([" usage: auth <code>", " no code received. the terminal cannot authenticate a silence twice."])
    if auth.verify(args[0]):
        session["rank"] = "Limonology"
        session["auth_level"] = 2
        session["auth_key"] = args[0]
        return (random.choice([" Authentication accepted.", " Authentication accepted after corridor comparison."])
                + "\n Rank elevated: Limonology"
                + "\n" + random.choice([" Restricted commands now available.", " Restricted command ledger has stopped pretending not to see you."]))
    else:
        return (random.choice([" Authentication denied.", " Authentication denied; submitted code lacks a witness."])
                + f"\n Incident logged. ({forms.lookup('denied_auth')})")

def cmd_egress_recall(args):
    out = egress.recall(args)
    if random.random() < 0.3:
        out += "\n" + random.choice(["Egress note: do not verify a route while standing in its memory.",
                                      "Egress note: if the exit remembers you, let it speak first."])
    return out

def cmd_debrief_schedule(args):
    out = debrief.schedule(args)
    if random.random() < 0.35:
        out += "\n" + random.choice(["Debrief reminder: bring a dry pen and a name you still answer to.",
                                      "Debrief reminder: rooms may be rescheduled if they become previous."])
    return out

def cmd_pct90156(args, session):
    if session["auth_level"] < 2:
        return (random.choice([" ACCESS DENIED.", " ACCESS DENIED BY HANDBOOK 11.3."])
                + "\n PCT90156 is reserved for Employees of Rank Limonology."
                + f"\n Incident logged. ({forms.lookup('restricted_invocation')})")
    out = random.choice([" PCT90156 — invoked.", " PCT90156 — please keep both hands visible to the terminal."])
    out += "\n" + random.choice([" Establishing channel to repository node ...", " Asking repository node to stop pretending to be asleep ..."])
    out += "\n Pattern Integrity ............ OK\n Authentication ............... OK\n Decoded endpoint:\n"
    out += f"\n {repository.get_endpoint(session['auth_key'])}\n"
    out += "\n" + random.choice([" Channel closed.", " Channel closed before it could be followed."])
    return out

def cmd_senion(args, session):
    return (
        "Senion verification has been moved to a dedicated gate-by-gate API.\n"
        "Begin a sequence: POST /api/senion/begin  (body: {\"session\": ...})\n"
        "Submit each answer: POST /api/senion/answer  (body: {\"session\": ..., \"answer\": ...})\n"
        "The terminal cannot conduct the rite in a single response."
    )

def cmd_contact_office(args, session):
    if args and args[0].lower() in {"codicology","codicology-wing","archive","archive-integrity"}:
        return cmd_codicology(session)
    return comshell_extra.run("contact.office", args, session)

def cmd_codicology(session):
    if codicology_call is None:
        return "Codicology switchboard module unavailable. The office is present but unreachable."
    return codicology_call.start(session)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)