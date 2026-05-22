#!/usr/bin/env python3
from __future__ import annotations

import os
import random
import shlex
import sys
import time
from typing import Callable

from stillwater import auth, comshell_extra, debrief, egress, forms, nodes, pattern_integrity, senion_verify, senion_verify
from stillwater._internal import repository

try:
    from stillwater import document_browser
except Exception:
    document_browser = None

try:
    from stillwater import codicology_call
except Exception:
    codicology_call = None

SESSION = {
    "rank": "Trainee",
    "auth_level": 0,
    "auth_key": None,
    "session_id": f"SW-{random.randint(10000, 99999)}-{random.randint(100, 999)}",
    "node": random.choice(["Δ-04", "Δ-04", "྾2-A", "North Archive", "West Stair"]),
    "banner_variant": random.randint(100, 999),
}
PROMPT = "stillwater@comShell:~$ "
STILLWATER_LOGOS = [
    r"""
        ~                         ~
 ███████╗████████╗██╗██╗     ██╗     ██╗    ██╗ █████╗ ████████╗███████╗██████╗
 ██╔════╝╚══██╔══╝██║██║     ██║     ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
 ███████╗   ██║   ██║██║     ██║     ██║ █╗ ██║███████║   ██║   █████╗  ██████╔╝
 ╚════██║   ██║   ██║██║     ██║     ██║███╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
 ███████║   ██║   ██║███████╗███████╗╚███╔███╔╝██║  ██║   ██║   ███████╗██║  ██║
 ╚══════╝   ╚═╝   ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                         F O U N D A T I O N
    """,
    r"""
        _________________________________________________
       /                                                 \
      /       S T I L L W A T E R   F O U N D A T I O N   \
     /_____________________________________________________\
             ||        ||        ||        ||        ||
             ||        ||        ||        ||        ||
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              internal systems // quiet-water branch
    """,
    r"""
             .-------------------------------.
             |   STILLWATER FOUNDATION       |
             |   shared libraries terminal   |
             '---------------.---------------'
                             / \
                       ~    /___\    ~
                           /_____\
                          /_______\
                water remembers its container
    """,
]
BOOT_LINES = [
    "Session opened. You are not the first person to open a session from this terminal today.\n There is no record of anyone else opening a session from this terminal today.",
    "Archive index loaded. 14 documents are addressed to you.\n You have not been employed here long enough for 14 documents to exist.",
    "Corridor geometry nominal. East wing geometry has been reclassified as Not Applicable.\n The third survey team has not yet been asked for its findings.",
    "Pattern Integrity: NOMINAL. This status has not changed in 847 days.\n The last time it changed, four rooms on Floor -3 were sealed. They remain sealed.",
    "Personnel roster loaded. 3 entries are flagged STILL_ON_SITE despite offboarding confirmation.\n Offboarding was confirmed by the employees themselves.",
    "Building ྾2 mounted. Class-IV designation means the building is no longer changing.\n It does not mean the building has stopped.",
    "Terminal ready. Seventeen previous sessions were opened from this terminal.\n Twelve were closed normally. The other five remain ONGOING.",
]
UNKNOWN_COMMAND_RESPONSES = [
    "'{cmd}' was last executed on this terminal 14 months ago.\n The session log from that day is sealed under Pattern Integrity review.",
    "'{cmd}' is not in the command index.\n '{cmd}' is in the incident index.\n These are different indexes.",
    "'{cmd}' is not a permitted command at your rank.\n '{cmd}' is not a permitted command at any rank currently held by a living employee.",
    "'{cmd}' completed.\n '{cmd}' did not complete.\n The discrepancy has been filed.",
    "'{cmd}' is not recognised.\n The terminal recognises that you typed it.\n These are different things.",
    "'{cmd}' has been removed from this terminal's command index following Incident 19-C.",
    "'{cmd}' timed out.\n A command cannot time out at this terminal.\n Pattern Integrity has not responded.",
]
ERROR_RESPONSES = [
    "Process failed: {error}\n The process ran correctly for 4.2 seconds before it failed. Those 4.2 seconds are not in the output.",
    "Handler returned an error: {error}\n The handler also returned something that is not an error and cannot be classified.",
    "Execution error: {error}\n This error has occurred before on this terminal. The previous session is still marked ONGOING.",
    "Command failed: {error}\n Three other terminals on this network produced the same error at the same moment.",
]


def _clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def _banner() -> None:
    print(random.choice(STILLWATER_LOGOS))
    print("=" * 78)
    print(" STILLWATER FOUNDATION — comShell v4.9.1 ")
    print(" INTERNAL USE ONLY / LOW-CLEARANCE PUBLIC TERMINAL ")
    print("=" * 78)
    print(f" Session ID : {SESSION['session_id']}")
    print(" User       : anon")
    print(f" Rank       : {SESSION['rank']}")
    print(f" Node       : {SESSION['node']}")
    print(f" Variant    : {SESSION['banner_variant']}")
    print(" Pattern Integrity .................. " + pattern_integrity.current_status())
    print("-" * 78)
    print(" " + random.choice(BOOT_LINES))
    print(" Type 'help' for a partial list of permitted commands. Use 'help all' for more noise.")
    print(" Archive access is mounted read-only. Some shelves answer out of order.")
    print()


def _print_block(text: str | None) -> None:
    if text:
        print(text)


def cmd_help(args: list[str]) -> None:
    show_all = bool(args and args[0].lower() == "all")
    blocks = [comshell_extra.help_text(show_all=show_all)]
    if document_browser is not None:
        blocks.append(document_browser.help_text(show_all=show_all))
    if codicology_call is not None:
        blocks.append(codicology_call.help_text(show_all=show_all))
    blocks.append("Senion verification: verify.senion / senion.verify / verify rosetta")
    print("\n\n".join(block for block in blocks if block))


def cmd_whoami(args: list[str]) -> None:
    variants = [
        [" user : anon", f" rank : {SESSION['rank']}", f" session : {SESSION['session_id']}", " origin : unverified", " note : badge was not issued at login and has not been reported missing"],
        [" designation check complete:", " visible name ........... anon", f" administrative rank .... {SESSION['rank']}", " former designation ..... not on record / still resolving", " last verified by ....... a member of staff no longer listed here"],
        [f" anon@{SESSION['node']}", f" clearance: {SESSION['rank']}", " note: you have been in this corridor before. this has not been confirmed.", " note: do not respond if addressed by a name you do not currently hold."],
        [" identity query returned one result.", " that result is also a query.", f" rank on file: {SESSION['rank']}", " photograph on file: blank / still developing / not yet taken"],
    ]
    print("\n".join(random.choice(variants)))


def cmd_status(args: list[str]) -> None:
    prefix = random.choice([
        "Status request logged by Pattern Integrity.",
        "Status request received. One duplicate result suppressed.",
        "Status request accepted. Origin of request has been noted without comment.",
        "Status returned from the nearest node willing to answer.",
    ])
    print(prefix)
    print(pattern_integrity.full_report())


def cmd_ls(args: list[str]) -> None:
    print(nodes.list_nodes())
    if random.random() < 0.45:
        print(random.choice([
            "Note: one node is responding from a location inconsistent with its designation.",
            "Note: visible nodes do not include rooms currently outside their assigned floor.",
            "Note: a node listed here may be listed here twice. Both listings are correct.",
            "Note: node ྾2-A* is administratively absent. It is not physically absent.",
            "Note: do not ping a node that answers before you submit the packet.",
        ]))


def cmd_ping(args: list[str]) -> None:
    if not args:
        print(random.choice([" usage: ping <node>", " usage: ping <node>  # do not ping a node that answers before you type", " ping requires a node designation, even if the node already knows."]))
        return
    print(nodes.ping(args[0]))
    if random.random() < 0.35:
        print(random.choice(["round-trip variance accepted under Quiet Systems Policy.", "node response arrived with waterline metadata removed.", "latency witness unavailable; result preserved anyway."]))


def cmd_auth(args: list[str]) -> None:
    if not args:
        print(random.choice([" usage: auth `", " restricted invocation requires a submitted code.", " no code received. the terminal cannot authenticate a silence twice."]))
        return
    submitted = args[0]
    if auth.verify(submitted):
        SESSION["rank"] = "Limonology"
        SESSION["auth_level"] = 2
        SESSION["auth_key"] = submitted
        print(random.choice([" Authentication accepted.", " Authentication accepted after corridor comparison.", " Authentication accepted. Do not celebrate near uncovered glass."]))
        print(" Rank elevated: Limonology")
        print(random.choice([" Restricted commands now available.", " Restricted invocation gate opened quietly.", " Restricted command ledger has stopped pretending not to see you."]))
    else:
        print(random.choice([" Authentication denied.", " Authentication denied; submitted code lacks a witness.", " Authentication denied; the handbook disagrees with your pronunciation.", " Authentication denied; rank echo did not resolve."]))
        print(f" Incident logged. ({forms.lookup('denied_auth')})")


def cmd_egress_recall(args: list[str]) -> None:
    print(egress.recall(args))
    if random.random() < 0.3:
        print(random.choice(["Egress note: do not verify a route while standing in its memory.", "Egress note: return paths may point at rooms, people, or old weather.", "Egress note: if the exit remembers you, let it speak first."]))


def cmd_debrief_schedule(args: list[str]) -> None:
    print(debrief.schedule(args))
    if random.random() < 0.35:
        print(random.choice(["Debrief reminder: voluntary means recorded without resistance.", "Debrief reminder: bring a dry pen and a name you still answer to.", "Debrief reminder: rooms may be rescheduled if they become previous."]))


def cmd_pct90156(args: list[str]) -> None:
    if SESSION["auth_level"] < 2:
        print(random.choice([" ACCESS DENIED.", " ACCESS DENIED BY HANDBOOK 11.3.", " ACCESS DENIED; restricted invocation detected before permission."]))
        print(" PCT90156 is reserved for Employees of Rank Limonology.")
        print(f" Incident logged. ({forms.lookup('restricted_invocation')})")
        return
    print(random.choice([" PCT90156 — invoked.", " PCT90156 — invocation acknowledged by repository node.", " PCT90156 — please keep both hands visible to the terminal."]))
    time.sleep(0.4)
    print(random.choice([" Establishing channel to repository node ...", " Establishing channel through quiet-water relay ...", " Asking repository node to stop pretending to be asleep ..."]))
    time.sleep(0.6)
    print(" Pattern Integrity ............ OK")
    print(" Authentication ............... OK")
    print(" Decoded endpoint:")
    print()
    print(f" {repository.get_endpoint(SESSION['auth_key'])}")
    print()
    print(random.choice([" Channel closed.", " Channel closed before it could be followed.", " Channel closed. Do not reopen from a reflected terminal."]))





def cmd_verify_senion(args: list[str]) -> None:
    senion_verify.run(args, SESSION)

def cmd_contact_office(args: list[str]) -> None:
    if args and args[0].lower() in {"codicology", "codicology-wing", "archive", "archive-integrity"}:
        if codicology_call is None:
            print("Codicology switchboard module unavailable. The office is present but unreachable.")
            return
        codicology_call.start(SESSION)
        return
    _print_block(comshell_extra.run("contact.office", args, SESSION))


def cmd_codicology_call(args: list[str]) -> None:
    if codicology_call is None:
        print("Lower switchboard unavailable. The receiver is present, but the line is not.")
        return
    codicology_call.start(SESSION)

def cmd_clear(args: list[str]) -> None:
    _clear()
    _banner()


def cmd_exit(args: list[str]) -> None:
    print(random.choice([" Session terminated.", " Session lowered into archive state.", " Session closed; remaining echoes reassigned."]))
    print(f" Session {SESSION['session_id']} archived.")
    sys.exit(0)


def _make_extra_command(command_name: str) -> Callable[[list[str]], None]:
    def _handler(args: list[str]) -> None:
        _print_block(comshell_extra.run(command_name, args, SESSION))
    return _handler


def _make_document_command(command_name: str) -> Callable[[list[str]], None]:
    def _handler(args: list[str]) -> None:
        _print_block(document_browser.run(command_name, args, SESSION))
    return _handler


COMMANDS: dict[str, Callable[[list[str]], None]] = {
    "help": cmd_help,
    "whoami": cmd_whoami,
    "status": cmd_status,
    "ls": cmd_ls,
    "ping": cmd_ping,
    "auth": cmd_auth,
    "egress.recall": cmd_egress_recall,
    "debrief.schedule": cmd_debrief_schedule,
    "pct90156": cmd_pct90156,
    "verify.senion": cmd_verify_senion,
    "senion.verify": cmd_verify_senion,
    "rosetta.verify": cmd_verify_senion,
    "verify": cmd_verify_senion,
    "contact.office": cmd_contact_office,
    "call.codicology": cmd_codicology_call,
    "codicology.call": cmd_codicology_call,
    "switchboard.codicology": cmd_codicology_call,
    "dial.codicology": cmd_codicology_call,
    "clear": cmd_clear,
    "cls": cmd_clear,
    "exit": cmd_exit,
    "quit": cmd_exit,
}
for _extra_name in comshell_extra.command_names():
    COMMANDS.setdefault(_extra_name.lower(), _make_extra_command(_extra_name.lower()))
if document_browser is not None:
    for _doc_name in document_browser.command_names():
        COMMANDS.setdefault(_doc_name.lower(), _make_document_command(_doc_name.lower()))

if codicology_call is not None:
    for _call_name in codicology_call.command_names():
        COMMANDS.setdefault(_call_name.lower(), cmd_codicology_call)


def main() -> None:
    _clear()
    if hasattr(auth, "require_comshell_password") and not auth.require_comshell_password():
        sys.exit(1)
    _banner()
    while True:
        try:
            raw = input(PROMPT).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            cmd_exit([])
        if not raw:
            if random.random() < 0.18:
                print(random.choice(["The terminal accepts your silence and files it under Form S-00.", "No command entered. The corridor does not count this as hesitation.", "Silence received. No further action, except storage."]))
            continue
        try:
            parts = shlex.split(raw)
        except ValueError as error:
            print(f"Input refused: {error}")
            print("The terminal dislikes unmatched quotation marks. So do the rooms.")
            print()
            continue
        if not parts:
            continue
        cmd = parts[0].lower()
        args = parts[1:]
        if cmd in COMMANDS:
            try:
                COMMANDS[cmd](args)
            except SystemExit:
                raise
            except Exception as error:
                print(random.choice(ERROR_RESPONSES).format(error=error))
                print(f" ({forms.lookup('anomaly')} recommended)")
        else:
            print(random.choice(UNKNOWN_COMMAND_RESPONSES).format(cmd=cmd))
            print(random.choice([" Try 'help'.", " Try 'help all', unless you dislike long corridors.", " Consult the handbook edition that does not face the window.", " Command visibility may improve after debriefing."]))
        print()


if __name__ == "__main__":
    main()
