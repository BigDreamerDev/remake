from __future__ import annotations

import random
from datetime import date, datetime
from typing import Iterable

from stillwater import auth, codicology, cymatics, discordian, forms, handbook, hex_codec, hydrology, nodes, pattern_integrity


def _join(lines: Iterable[str]) -> str:
    return "\n".join(lines)


def _block(*lines: str) -> list[str]:
    return list(lines)


def _choice_block(blocks: list[list[str]]) -> str:
    return _join(random.choice(blocks))


STATIC_COMMANDS = {
    "version": [
        [
            " comShell v4.9.1",
            " previous version: v4.9.1",
            " version before that: v4.9.1",
            " the changelog has no entries",
            " the changelog was last modified six years before comShell was developed",
        ],
        [
            " comShell v4.9.1 / public terminal build",
            " this build was audited by a team of three",
            " the audit found nothing",
            " one auditor is no longer with the Foundation",
            " one auditor does not remember the audit",
            " one auditor has requested not to be asked about it again",
        ],
        [
            " comShell v4.9.1",
            " last verified: [REDACTED]",
            " note: the terminal you are using is not the terminal in the system photograph",
            " note: the terminal in the system photograph is not in this building",
        ],
    ],
 
    "motd": [
        [
            " Message of the day:",
            " The east wing has been closed for renovation since March.",
            " Renovation teams report no progress.",
            " Renovation teams report, on average, 30% fewer members than when they entered.",
            " Renovation continues.",
        ],
        [
            " Message of the day:",
            " The sound reported in Stairwell B is not a person.",
            " Staff are not to respond to it if it uses their name.",
            " Staff are not to respond to it if it uses a name they used to have.",
            " Staff who are unsure whether they used to have a name should report to Pattern Integrity",
            " before entering Stairwell B.",
        ],
        [
            " Message of the day:",
            " Floor -4 does not exist in this building.",
            " The lift does not go to Floor -4.",
            " Employees are reminded that the lift going somewhere is not the same",
            " as that somewhere existing.",
            " If you reach Floor -4, do not get out.",
            " If you got out, submit Form PI-3 immediately.",
            " If you cannot find your way back to submit Form PI-3, remain where you are.",
            " Someone will come for you.",
            " Someone has always come for you.",
        ],
        [
            " Message of the day:",
            " The annual photograph will be taken Friday.",
            " Attendance is mandatory.",
            " Employees who do not appear in the developed photograph should report",
            " to Pattern Integrity within 24 hours.",
            " They should not tell anyone else that they did not appear in the photograph",
            " before they report.",
            " Last year, two employees did not appear.",
            " One reported within 24 hours.",
            " We do not discuss what was done for them.",
            " The other did not report.",
            " We do not discuss what found them instead.",
        ],
    ],
 
    "id": [
        [
            " uid=0000(anon)",
            " status: present",
            " note: a uid=0000(anon) session was opened at this terminal at 03:14 this morning",
            " note: the building was locked at 03:14 this morning",
            " note: no one was in the building at 03:14 this morning",
        ],
        [
            " designation: anon / TRAINEE",
            " note: your badge has been read by three readers you did not pass",
            " note: the readers are in the east wing",
            " note: the east wing has been locked since March",
        ],
        [
            " uid=0000(anon)",
            " prior designation: [not displayed at this clearance]",
            " note: four employees have sat at this terminal this week",
            " note: three of them have since been reassigned",
            " note: one of them has since been reclassified",
        ],
    ],
 
    "lights.status": [
        [
            " Lighting report:",
            "  Atrium ................. on",
            "  Corridor Δ-04 west ..... on",
            "  Floor -3 corridor ...... off",
            "  Floor -3 corridor ...... something is casting a shadow on the floor",
            "  Floor -3 corridor ...... the light is off",
            "  Stairwell B ............ fluorescent fitting removed 2019",
            "  Stairwell B ............ hum continues",
            "  East wing .............. [MEASUREMENT UNAVAILABLE]",
        ],
        [
            " Lighting audit complete.",
            " One room is lit from the inside.",
            " That room has no light source.",
            " That room has no windows.",
            " That room has been sealed since the third survey team entered the east wing.",
            " The light in that room has been on since before the room was sealed.",
        ],
        [
            " Lights ON: all public corridors, atrium, archive ground floor.",
            " Lights OFF: east wing (locked), Floor -4 (does not exist), Room ྾2-A (admin absent).",
            " Lights ON in Room ྾2-A.",
            " This has been logged.",
            " This has been logged before.",
        ],
    ],
 
    "door.test": [
        [
            " Door test started.",
            "  Archive hatch ........... closed",
            "  Sub-level fire door ..... closed",
            "  East wing main door ..... closed (locked March, standard padlock)",
            "  East wing main door ..... warm on the inside face",
            "  East wing main door ..... something tried the handle from the inside at 02:47",
            "  East wing main door ..... the east wing has not been occupied since March",
            " Result: all doors closed. One door is being used from the wrong side.",
        ],
        [
            " Door test started.",
            "  Six doors tested. Six doors closed. Five doors are where they were yesterday.",
            "  One door has moved.",
            "  It has moved 40 centimetres down the corridor.",
            "  It is still a working door.",
            "  Facilities has been notified.",
            "  Facilities sent someone to look at it.",
            "  Facilities is not sure the person they sent came back.",
        ],
        [
            " Door test complete.",
            "  All tested doors functional.",
            "  One door could not be tested.",
            "  The door could not be tested because the room it opens into",
            "  is the same room the door is in.",
        ],
    ],
 
    "badge.read": [
        [
            " Badge read: ANON / TRAINEE",
            " Access log shows this badge passed through",
            "  Δ-04 north gate: today 09:02 (you)",
            "  sub-level access panel: today 09:02 (you)",
            "  east wing inner gate: today 09:02",
            " The east wing inner gate is not on this badge's access list.",
            " The east wing inner gate has been locked since March.",
            " You were at the Δ-04 north gate at 09:02.",
        ],
        [
            " Badge read failed.",
            " The reader found a name on the badge.",
            " The name is not your current designation.",
            " The reader has been asked not to say what the name was.",
            " The reader's log has been sealed.",
        ],
        [
            " Badge read: ANON / TRAINEE.",
            " Note: this badge was reported lost by a previous employee.",
            " Note: that employee left the building.",
            " Note: that is the last confirmed record of that employee.",
        ],
    ],
 
    "descale.status": [
        [
            " Cafeteria maintenance: 02:00–04:00 daily, Floor -3.",
            " Do not enter during the maintenance window.",
            " Do not enter during the maintenance window even if you hear voices you recognise.",
            " Do not enter during the maintenance window even if you recognise your own voice.",
            " If you recognise your own voice coming from the cafeteria during the maintenance window,",
            " do not respond to it.",
            " Do not tell it what it is asking.",
        ],
        [
            " Descaling status: active.",
            " Last six maintenance windows: routine.",
            " On the seventh: staff on the floor above reported the sound of",
            " someone dragging something heavy across a tiled floor for 90 minutes.",
            " This is consistent with routine descaling equipment.",
            " The equipment in question has not been used in four years.",
            " The equipment in question is in the locked storage room off Floor -3.",
        ],
        [
            " Cafeteria: operational.",
            " Floor -3 cafeteria Wednesday soup: discontinued.",
            " Reason for discontinuation: filed under Inherited Silences.",
            " The chef who prepared it: reassigned.",
            " The recipe: sealed.",
            " One employee has submitted six requests for the recipe since the discontinuation.",
            " That employee has been reminded that the soup is discontinued.",
            " That employee has been reminded of this in an office, in writing, and by phone.",
            " That employee does not remember any of these reminders.",
        ],
    ],
 
    "atrium.clock": [
        [
            " Clock audit:",
            "  Clock A (north): 06:00",
            "  Clock B (south): 06:00",
            "  Clock C (east):  removed for maintenance in 2018 / not yet returned",
            "  Clock C (east):  the clock face is still on the wall",
            "  Clock C (east):  the hands are moving",
            "  Clock C (east):  Pattern Integrity has been notified",
            "  Clock D (lobby): running. running toward something.",
        ],
        [
            " All atrium clocks show 06:00.",
            " They have shown 06:00 for the past 6 days.",
            " Facilities has verified the mechanism on all three remaining clocks.",
            " The mechanisms are correct.",
            " Facilities has suggested the clocks may be right.",
            " Facilities has not explained what would need to be true for that to be the case.",
        ],
        [
            " Clock D in the lobby shows the correct time.",
            " Staff are asked not to use Clock D as a reference.",
            " Clock D does not show the same time to everyone who looks at it.",
        ],
    ],
 
    "observance.next": [
        [
            " Next observance: Annual Memorial Ceremony. Bcy 50, 3192 YOLD. Atrium, 11:11.",
            " Silence is mandatory and total.",
            " The silence is not broken under any provocation.",
            " Last year's ceremony: silence was broken by a sound from the east corridor.",
            " The east corridor was empty.",
            " Eleven employees turned to look.",
            " Nine employees remember turning to look.",
            " Do not turn to look.",
        ],
        [
            " Next observance: Standing Quiet. Daily. Unsynchronised.",
            " Sixty seconds of silence, individual.",
            " Do not adjust your silence to match nearby employees.",
            " If you hear someone else's silence, report it.",
            " Silence does not make a sound.",
            " If you can hear it, it is not silence.",
        ],
        [
            " Next observance: Annual Photograph. Bcy 49, 3192 YOLD. Atrium, 14:30.",
            " Mandatory attendance.",
            " Employees who do not appear in the developed photograph have 24 hours to report.",
            " This is not precautionary.",
            " This is because 24 hours is how long you have.",
        ],
    ],
 
    "orange.when": [
        [
            " Setting Orange cannot be forecast from this terminal.",
            " The department responsible for forecasting Setting Orange was dissolved.",
            " The department was dissolved because of what it forecast.",
            " The forecast is sealed under Pattern Integrity clearance.",
            " Pattern Integrity has not been asked to unseal it.",
            " Pattern Integrity has not been asked because the people who would ask",
            " know what the forecast says.",
        ],
        [
            " Setting Orange: not scheduled.",
            " Setting Orange: not cancelled.",
            " The last Setting Orange was 11 years ago.",
            " Fourteen employees were in the building.",
            " Seven were in the building the following morning.",
            " The other seven were also in the building the following morning.",
            " This is why Setting Orange is not discussed in advance.",
        ],
        [
            " Query refused. Setting Orange scheduling is handled by a sealed sub-process.",
            " You do not have clearance for the sub-process.",
            " You do not want clearance for the sub-process.",
        ],
    ],
 
    "weather.inside": [
        [
            " Internal conditions:",
            "  Temp: 18.1°C, all floors, all rooms",
            "  Temp variance between floors: 0.0°C",
            "  This has been the case for 22 consecutive days",
            "  External temperature range this period: -3°C to 14°C",
            "  HVAC system was shut down for maintenance on day 9 of this period",
            "  Temperature remained 18.1°C",
            "  HVAC system remains shut down",
            "  Temperature remains 18.1°C",
        ],
        [
            " Internal environment report:",
            "  humidity: 51%, stable",
            "  temperature: 18.1°C, stable",
            "  air movement: none recorded in east wing",
            "  air movement: candles in east wing office have been observed flickering",
            "  east wing has been locked since March",
            "  the candles were not there in March",
        ],
        [
            " Building environment: within acceptable parameters.",
            " Floor -3 is 4°C colder than Floor -2.",
            " This is consistent with a floor below ground.",
            " Floor -3 is above ground.",
        ],
    ],
 
    "waterline": [
        [
            " Hydrology bay: no active standing water.",
            " Historic waterline marks are present on sub-level walls.",
            " The highest mark is 2.3m.",
            " The sub-level ceiling is 2.4m.",
            " The sub-level has never been flooded.",
            " The mark is old.",
            " There is no record of it being made.",
        ],
        [
            " Standing water survey: dry, all floors.",
            " Floor -3 drain: operational.",
            " Floor -3 drain: sound of running water, continuous.",
            " Floor -3 drain: dry.",
            " The sound has been classified Class-I.",
            " Three employees have requested a reclassification.",
            " All three have since been reassigned.",
        ],
        [
            " Waterline registry: no active readings.",
            " Note: the waterline mark in Archive Stack 7 is 1.8m high.",
            " Note: the mark appears fresh.",
            " Note: Archive Stack 7 is sealed.",
            " Note: Pattern Integrity has been notified.",
            " Note: Pattern Integrity has asked that the mark not be",
            " photographed, described, or measured again.",
        ],
    ],
 
    "mailroom.check": [
        [
            " Mailroom audit:",
            "  Incoming: 3 items",
            "  Outgoing: 3 items",
            "  Returned: 1 item addressed to Mr. 437265737377656C6C",
            "  Do not open the returned item.",
            "  Do not open it to verify the addressee.",
            "  An employee opened the last one to verify the addressee.",
            "  That employee is currently the subject of a Pattern Integrity review.",
            "  The employee is fine.",
            "  The employee says they are fine.",
            "  The employee has been saying they are fine for six months without being asked.",
        ],
        [
            " Mailroom: sealed until further notice.",
            " One package arrived this morning.",
            " It is addressed to someone who left last year.",
            " It is addressed to someone who left last year in a way that suggests the sender",
            " knew they would have left by now.",
            " The postmark is from three weeks before that person was hired.",
        ],
        [
            " Mailroom: operational.",
            " One envelope has been in the outgoing tray for 11 days.",
            " It has been processed three times.",
            " It returns each morning.",
            " We are no longer processing it.",
            " It returns each morning anyway.",
        ],
    ],
 
    "maintenance.window": [
        [
            " Maintenance windows:",
            "  02:00–04:00   Floor -3 cafeteria (do not enter / do not respond to voices)",
            "  04:04–04:04   East corridor (zero-duration window; do not attempt to attend)",
            "  17:00–19:00   Stairwell B (cymatic monitoring active; no vocalisations of any kind)",
            "  ongoing       East wing (locked March; renovation team status: under review)",
        ],
        [
            " Scheduled maintenance: Stairwell B tone investigation.",
            " Scheduled for three consecutive Tuesdays.",
            " Week 1: acoustic team reported tone consistent with resonant frequency.",
            " Week 2: acoustic team reported the tone was responding to the measurement equipment.",
            " Week 3: acoustic team did not submit a report.",
            " Week 3 maintenance window is listed as complete.",
        ],
        [
            " Maintenance windows: no windows scheduled this week.",
            " Floor -3 descaling: on hold pending review of Week 7 incident.",
            " Week 7 incident details: sealed.",
            " Cafeteria is operational.",
            " Cafeteria staff report they would prefer not to work the opening shift.",
            " Cafeteria staff have not said why.",
            " Cafeteria staff have been working the opening shift.",
        ],
    ],
 
    "memorial.check": [
        [
            " Memorial Ceremony: Bcy 50, 3192 YOLD. Mandatory.",
            " Attendance confirmed by roll. Names marked present are present.",
            " Last ceremony: 14 marked present. 14 in the photograph.",
            " One person in the photograph was not on the roll.",
            " Three people on the roll were not in the photograph.",
            " This was reported.",
            " The three who were not in the photograph have 24 hours to report.",
            " All three reported.",
            " We do not discuss what was done for them.",
        ],
        [
            " Memorial ledger: current.",
            " Names listed: sufficient for quorum.",
            " Names listed who are no longer employed here: 4.",
            " Of those 4: two resigned, one retired, one is listed as STILL_ON_SITE.",
            " The STILL_ON_SITE listing has been reviewed three times.",
            " It has not been changed.",
        ],
        [
            " Memorial silence: mandatory and total.",
            " It is not broken under any provocation.",
            " 'Any provocation' has been tested.",
            " We do not discuss what provoked it.",
            " We do not discuss how long the silence actually lasted.",
        ],
    ],
 
    "silence.begin": [
        [
            " Standing Quiet initiated.",
            " Sixty seconds. Unsynchronised.",
            " Do not listen too carefully during Standing Quiet.",
            " Pattern Integrity recommends that employees not listen too carefully",
            " to the silence in this building.",
            " The silence does not always stay where it is put.",
        ],
        [
            " Silence begins now.",
            " ...",
            " ...",
            " Sixty seconds completed.",
            " Note: the terminal clock shows the silence lasted 60 seconds.",
            " Three employees on Floor -3 have reported it lasting significantly longer.",
            " Their reports are consistent with each other.",
            " This is the third time this has been reported.",
        ],
        [
            " Quiet period started.",
            " One sound has been logged during this period.",
            " It was logged before this period started.",
            " The log timestamp is being reviewed.",
        ],
    ],
 
    "silence.status": [
        [
            " Standing Quiet: filed.",
            " One employee submitted a standing quiet report that described what they heard during it.",
            " They were told Standing Quiet is silent.",
            " They said they know.",
            " They said that's what they heard.",
            " Their report is sealed.",
        ],
        [
            " Silence status: complete.",
            " Duration on record: 60 seconds.",
            " Duration as reported by employees on Floor -3: 60 seconds.",
            " Duration as reported by employees in the east wing:",
            " [the east wing has been locked since March]",
        ],
        [
            " Quiet period: logged as complete.",
            " One employee reported hearing their name during the quiet period.",
            " They were asked who said it.",
            " They said no one did.",
            " They were asked how they knew it was their name.",
            " They said they didn't, at first.",
        ],
    ],
 
    "contact.office": [
        [
            " Contact routing:",
            "  Pattern Integrity ......... do not contact while status is NOMINAL",
            "  Inherited Silences ........ no extension / all contact by written request",
            "  Codicology ................ knock twice. document the third knock.",
            "  East Wing Facilities ...... extension disconnected March",
            "  East Wing Facilities ...... extension answers",
            "  East Wing Facilities ...... do not speak to whoever answers",
        ],
        [
            " No office accepts direct calls from this terminal.",
            " Emergency contact: Pattern Integrity Working Group.",
            " Note: Pattern Integrity has not responded to contact in 72 hours.",
            " Note: Pattern Integrity's status light is green.",
            " Note: Pattern Integrity's office light is on.",
            " Note: Pattern Integrity's door is locked from the inside.",
        ],
        [
            " Contact directory: restricted above standard routing.",
            " Most contact is now handled through Inherited Silences.",
            " All contact was re-routed to Inherited Silences after the east wing incident.",
            " There is no record of an east wing incident.",
            " Contact was re-routed anyway.",
        ],
    ],
 
    "return.path": [
        [
            " Return path: not calculated.",
            " This terminal cannot generate a return path for the east wing.",
            " The east wing does not have an exit on any current floor plan.",
            " If you are in the east wing, you did not come from this terminal.",
            " If you are in the east wing, remain where you are.",
            " Someone will come for you.",
        ],
        [
            " Return path generated.",
            "  Step 1: proceed to the nearest stairwell",
            "  Step 2: do not use Stairwell B",
            "  Step 3: do not use Stairwell B",
            "  Step 4: do not use Stairwell B",
            " Result: egress confirmed via Stairwell A only.",
            " Note: Stairwell B is structurally sound.",
            " Note: this restriction is not structural.",
        ],
        [
            " Route calculated.",
            " Route passes through corridor ྾2-A.",
            " Corridor ྾2-A no longer exists administratively.",
            " Route still passes through it.",
            " This is why the route passes through it.",
        ],
    ],
}
 
 
RANDOM_LINES = {
    "notice.roll": [
        "Notice 44-B: The east wing renovation is ongoing. Personnel assigned to the east wing prior to March are reminded that reassignment requests must be submitted in person.",
        "Notice 12-C: Employees who hear their name in Stairwell B are not to respond. Employees who hear a name they used to have are especially not to respond.",
        "Notice 7-F: The suggestion box is operational. Three suggestions were submitted anonymously this month. Handwriting analysis is underway. We will find out who submitted them.",
        "Notice 19-A: Conference Room ྾2-A does not exist administratively. Meetings still scheduled there are to be reported to Inherited Silences. Do not attend them.",
        "Notice 22-D: The seventh visitor log entry is to remain blank. It is already filled in. Do not read it. This is the fourth notice about this.",
        "Notice 31-K: The lift did not go to Floor -4 this week. Report any week in which it does. Do not report what you saw. Report that it happened. Do not describe what you saw.",
        "Notice 5-D: Mail addressed to Mr. 437265737377656C6C is not to be opened. An employee opened it. That employee is currently on administrative leave. The employee says they are fine.",
        "Notice 88-A: Two employees did not appear in last year's Annual Photograph. One reported within 24 hours. One did not. We do not discuss what found the one who did not report.",
        "Notice 10-R: Mirrors and screens in sleep mode must be covered between 23:00 and 04:00. This policy exists for a reason. You do not have clearance for the reason.",
        "Notice 61-C: The car park line markings have been updated. Do not cross the new markings. The previous notices did not say why. This one also does not say why.",
        "Notice 14-F: The list of decommissioned departments is not to be retained, duplicated, or read more than once. If you have read it more than once, report to Pattern Integrity.",
        "Notice 9-A: The new evacuation siren is quieter. Inability to hear it is not evidence of its absence. Inability to move when it sounds is evidence of a different problem.",
    ],
 
    "log.tail": [
        "06:00:01 pattern_integrity: NOMINAL — status unchanged for 847 days — reviewing what happened on day 847",
        "06:00:04 node Δ-04: ping acknowledged — acknowledged from east wing — east wing is locked",
        "06:01:18 stairwell-B: 44.1Hz tone logged — tone classified Class-I — tone asked the logging system to stop — classification unchanged",
        "06:02:00 lift-B: travelled to Floor -4 — door did not open — floor does not exist — something pressed the button from inside on the way back",
        "06:03:33 archive: document returned from review with different handwriting than it was sent with — both versions filed",
        "06:04:04 east-wing: motion detected — east wing locked March — motion consistent with a person — no persons unaccounted for — yet",
        "06:05:16 room-2A: light confirmed on — room does not exist administratively — power draw confirmed — light on — no fixture listed in room",
        "06:07:00 badge-reader: badge [REDACTED] scanned at east wing inner gate — gate locked March — gate scanned the badge — badge is currently on your lanyard",
        "06:11:45 mirror-audit: reflection in east wing corridor running 0.8s behind subject — subject removed from east wing — reflection remains",
        "06:12:12 floor-3: cafeteria voice detected during maintenance window — voice said a name — name belongs to an employee — employee was not on Floor -3 — employee has been notified",
        "06:16:02 node-2C: response received 3.1 seconds before packet sent — packet sent — packet did not arrive — response already received",
        "06:21:09 pattern_integrity: status checked — NOMINAL — the pattern integrity officer who checks this has not been seen since 06:00 — status: NOMINAL",
    ],
 
    "mirror.audit": [
        "Mirror audit: one reflection is present in a room with no mirror. Form HA-12 opened. Auditor declined to return to the room.",
        "Mirror audit complete: all mirrors covered. One covered mirror is still visible in an uncovered mirror in a different room.",
        "Mirror audit: reflection in east wing main corridor is 0.8 seconds behind. East wing is locked. Audit team did not enter. Audit was conducted through the door glass.",
        "Mirror audit: auditor reported the reflection in Room ྾2-C did not copy their movements. Auditor asked to remain at their desk. Auditor is remaining at their desk. Auditor has not moved since.",
        "Mirror audit complete. One mirror covered itself before the audit team reached it. This is the second time this has happened. The mirror is different this time.",
        "Mirror audit interrupted. Auditor on Floor -3 reported the mirror showed the room as it appeared before the renovation. The renovation was in 2019. The pre-renovation room contained a person.",
        "Mirror audit: all mirrors compliant. The mirror in the east wing breakroom was not audited. The east wing breakroom was not entered. The mirror in the east wing breakroom was watching the door.",
        "Mirror audit complete. One reflection is still there. The employee it belonged to was reassigned in February. Facilities has been asked not to cover it until Pattern Integrity has reviewed it.",
    ],
 
    "stairwell.listen": [
        "Stairwell B: 44.1Hz tone — continuous — source unassigned — tone has been present since 2021 — the fitting that was making it was removed in 2021 — the tone continued — we have stopped investigating.",
        "Stairwell B: landing count going up is 9. Landing count going down is 8. Structural team has verified the stairwell. Structural team found 9 landings. Structural team found 8 landings. Structural team has submitted conflicting reports. Structural team has been asked not to enter Stairwell B again.",
        "Stairwell B: footsteps recorded on Floor -3 landing, 03:17. No personnel in building at 03:17. Footsteps recorded descending. Floor -3 is the lowest floor. The footsteps continued.",
        "Stairwell B: tone responded to being measured. When the acoustic meter was held at 44.1Hz calibration, the tone shifted to match. When the meter was removed, the tone returned. The tone knows what 44.1Hz sounds like.",
        "Stairwell B: employee reported hearing their name on the landing between Floor -1 and Floor -2. Employee was alone. Employee was told not to respond. Employee said they had already answered. Employee is currently on administrative leave.",
        "Stairwell B: door at sub-level 2 opens onto a room. Room is not on the floor plan. Room is lit. Room is furnished. Room appears to have been occupied recently. The door to Stairwell B from that room opens onto a different room.",
        "Stairwell B: the hum is louder this week. This is the third week it has been louder. Pattern Integrity has been notified. Pattern Integrity status: NOMINAL. Pattern Integrity has not acknowledged the notification.",
        "Stairwell B: closed for routine acoustic survey. Survey team entered at 09:00. Survey team exited at 09:11. Survey team reported the survey took four hours.",
    ],
 
    "cafeteria.menu": [
        "Today: cafeteria operational 08:00–17:00. Do not enter between 02:00–04:00. Do not enter between 02:00–04:00 even if someone holds the door for you.",
        "Today: all menu items available. Wednesday soup permanently discontinued. The chef who made it has been reassigned. The recipe is sealed. An employee has submitted 7 requests for the recipe. That employee does not remember submitting any of them.",
        "Today: cafeteria fully staffed. Staff would prefer not to open. Staff are opening anyway. Staff have been opening anyway for 4 months. Staff have not said what changed 4 months ago.",
        "Today: vending machine on Floor -3 removed from inventory February. Do not accept change from it. Do not spend the change. Two employees spent the change. This is why the vending machine was removed.",
        "Today: meal substitution available via Form S-44b for Rank Codicology and above. Note: three Rank Codicology employees have been on meal substitution since the cafeteria incident. They have not been asked about the cafeteria incident. They do not bring it up.",
        "Today: cafeteria queue operational. Queue moves normally. Employees are reminded that normal is a relative term in this building.",
        "Today: no soup. No explanation for the discontinuation has been provided. No explanation will be provided. The pot the soup was made in has been destroyed. Pattern Integrity supervised the destruction.",
        "Today: regular menu. Cafeteria staff report the cold storage room sounds different than it did last week. Cafeteria staff have been asked not to enter the cold storage room until Facilities has investigated. Facilities will investigate Thursday. It is Monday.",
    ],
 
    "policy.random": [
        "Clause 5.1: The phrase 'as it was' is restricted to Rank Hauntology and above. This restriction was added after an incident in 2019. The incident is not described in Clause 5.1.",
        "Clause 7.2: Mirrors and monitors in sleep mode must be covered between 23:00 and 04:00. This is not precautionary. This is because of something that has already happened.",
        "Clause 9.7: The seventh visitor log entry is to remain blank. It is always already filled in. Do not read it. You have been warned about this.",
        "Clause 11.3: The PCT90156 command requires authentication. Unauthorised invocations are logged. The log is reviewed. The review is done by someone who has been running the review alone for three years.",
        "Clause 13.4: Do not invoke the names of decommissioned departments. Several departments on the list were decommissioned because of what their names did.",
        "Clause 18.7: Mail for Mr. 437265737377656C6C is not to be opened. An employee opened it. That employee is fine. That employee keeps saying they are fine. We are monitoring.",
        "Clause 19.0: Conference Room ྾2-A no longer exists administratively. Treat rooms that no longer exist as you would treat a room that should not be there. Do not go in.",
        "Clause 20.0: Class-IV (Stabilised) means the building has stopped changing. This does not mean the building has stopped.",
        "Clause 22.1: The Memorial silence is not broken under any provocation. The provocation at last year's ceremony is not discussed. The silence held. This is all that is said about it.",
        "Clause 25.0: Standing Quiet is individual and unsynchronised. If you can hear someone else's silence, report it. Silence does not make a sound. If it does, report it immediately.",
    ],
 
    "memory.recall": [
        "Memory recall: no result. This terminal has no memory of the session that ran from 03:14 to 03:14 this morning. The session lasted zero minutes. The session log is 47 pages.",
        "Memory recall: record found. The record describes you entering a room you have not entered. The record is dated today. Today has not reached the time listed in the record.",
        "Memory recall: your badge was read at 11 locations today. You have been to 8 locations today. The other 3 readings are being investigated.",
        "Memory recall unavailable: the index for this period is sealed pending the east wing review. The east wing review has been pending for 6 months. The index has been sealed for 6 months.",
        "Memory recall complete: one result. The result matches an employee who no longer works here. The result is from this morning.",
        "Memory recall: the corridor you passed through at 09:14 is not on the floor plan. The corridor connected two locations that are not adjacent. You are here. You have no memory of a detour.",
        "Memory recall: session log shows you opened a command at 09:02 that you do not remember opening. The command ran for 11 seconds. The command is not in the index. The output is not in the log.",
        "Memory recall refused. The system flag says: if this employee requests this record, do not return it. The flag was placed six months ago. You have been employed here for three months.",
    ],
 
    "audit.roll": [
        "Audit roll: present × 14, absent × 0, STILL_ON_SITE × 1. The STILL_ON_SITE employee has been STILL_ON_SITE for four months. No one has seen them.",
        "Audit roll: all staff confirmed present. One confirmation arrived before the roll was taken. That employee was asked how they knew to confirm early. They said they didn't know they had.",
        "Audit roll: one signature on the roll is not from anyone currently employed. The signature is fresh. The ink is warm.",
        "Audit roll: quorum: achieved. Roll count: 14. Chairs: 14. Coats: 15. One coat does not belong to anyone present. The coat was there before the meeting started.",
        "Audit roll: two employees have submitted the same audit report. Identical wording. Submitted from different terminals at the same time. The employees work on different floors. Neither knows the other.",
        "Audit roll: one employee submitted their report in past tense in a way that describes events that have not yet happened. Their manager has reviewed it. Their manager has asked them not to submit another one.",
        "Audit roll: signed by all present staff. One signature belongs to a member of the third survey team. The third survey team has not returned from the east wing.",
        "Audit roll: complete. Pattern Integrity has reviewed the roll. Pattern Integrity has flagged three names. Pattern Integrity has not said which three.",
    ],
 
    "receipt.print": [
        "Receipt: printed. The receipt describes a transaction that has not taken place. The amount is not a currency denomination. The item column is blank. The printer was not told to print.",
        "Receipt: printer produced output unprompted at 03:14. Output is a receipt. The receipt is for the terminal you are currently using. The purchase date is listed as pending.",
        "Receipt: printed blank. Thermal paper warm. Blank receipts from this printer are filed under Incident Records, not Maintenance.",
    ],
 
    "queue.status": [
        "Queue: 4 people, 5 positions. The fifth position is between the second and third. It has been there since Thursday. No one stands in it. No one stands near it.",
        "Queue: moving. Two employees at the front of the queue since this morning. The queue opened at 09:00. Those employees were there before 09:00. The building was locked before 09:00.",
        "Queue: closed. The end of the queue is visible from the start of the queue. There is nothing between the start and the end. The queue is 40 metres long.",
    ],
 
    "cup.inspect": [
        "Cup: empty / correct temperature / facing away from Archive Stack 7. Employees are not to leave cups facing Archive Stack 7. This is in the handbook. The reason is not in the handbook.",
        "Cup: present. Contents: none visible. Temperature: above ambient by 4°C. Cup has not been touched today. This is the third consecutive day this has been logged.",
        "Cup inspection: cup is fine. Cup is fine. Cup is fine. Cup is fine. The employee who asked for this inspection has been asked to submit a statement about why they needed to know.",
    ],
 
    "chair.count": [
        "Chairs: 8 in Room 3. Meeting room 3 has 8 chairs. Seven people attended the last meeting. The minutes note eight attendees. No one in the room recalls an eighth person. The minutes are accurate.",
        "Chair count: 6 at last count, 7 now. No one added a chair. The chair is identical to the others. It is warm.",
        "Chair count: one chair in Archive Stack 7 that was not there during last month's audit. Archive Stack 7 has been locked since the deduplication incident. The chair has been there long enough to gather dust.",
    ],
 
    "window.cover": [
        "Window coverage: compliant, all floors. East wing windows: unable to verify. East wing is locked. The east wing windows are visible from outside the building. Something is covering them from the inside.",
        "Window: covered on this floor. The window in the stairwell between Floor -2 and Floor -3 cannot be covered. It does not have a frame. It is not a window. The glass is there anyway.",
        "Window covering complete. Facilities notes that the window in the Pattern Integrity office reflects a room that is not behind it. The window is covered. The reflection continues on the other side of the covering.",
    ],
 
    "paper.dry": [
        "Document: dry except for the section containing names. Names remain damp. This has been logged. The archivist who logged it has not touched the document again.",
        "Drying failed: document was filed wet. Document arrived dry. Document has been wet at the archive for three weeks. The archive is not damp. This is the document.",
        "Paper status: dry. The document that was sent for drying has been returned. It is dry. The content is different. Both versions have been filed.",
    ],
 
    "ink.test": [
        "Ink age: later than the document it appears on. The document is sealed. The ink appeared after sealing.",
        "Ink test: signatures on document 11-C are in an ink that does not match any Foundation-issued pen. Ink composition: unclassified. Document is from 1987. Ink type was not commercially available in 1987.",
        "Ink test complete. One ink sample matches a document in Archive Stack 7. The document it matches has not been unsealed in 40 years. Ink is fresh.",
    ],
 
    "tone.sample": [
        "Tone: 44.1Hz in Stairwell B, continuous. Source: removed 2021. Tone: continues. Tone: responded to equipment. Tone: has been responding to equipment for three years. We have stopped bringing equipment.",
        "Tone classified Class-I. Three employees have submitted reclassification requests. All three have been moved to other buildings. The tone has been reclassified as Class-I.",
        "Tone sample: collected. Sample reviewed. Sample contains a sound that is not a tone. Sound has been isolated. Sound has not been identified. Sound has not been returned to the stairwell. Sound is still in the sample file.",
    ],
 
    "basement.name": [
        "Floor -3: accessible, operational. Floor -4: not on floor plan. Lift reaches Floor -4. We have stopped sending people to verify. We have the reports from the last team. We do not share the reports.",
        "Sub-level designation: Floor -3 is the lowest floor in this building. The floor below Floor -3 predates this building. We are aware of it.",
        "Basement classification: standard. The east sub-level is not standard. Access to the east sub-level requires a form that is only available in the east sub-level.",
    ],
 
    "lamp.replace": [
        "Lamp replacement: deferred. Stairwell B lamp was replaced. The hum continued. The lamp was replaced again. The hum continued. The lamp was removed. The hum continued. We have stopped replacing it.",
        "Replacement lamp found lit in sealed packaging. Packaging intact. Lamp warm. Facilities has been notified. Facilities is not replacing any more lamps in Stairwell B.",
        "Lamp: east wing. East wing is locked. Lamp in east wing corridor has been on since March. Power to the east wing was cut in April. Lamp: on.",
    ],
}

RANDOM_LINES.update({
    "receipt.print": [
        "Receipt printed: blank / warm / not yours.",
        "Printer produced the sound of a receipt. Paper tray denies involvement.",
        "Receipt output suppressed because the purchase has not happened yet.",
    ],
    "queue.status": [
        "Queue status: moving only when unwatched.",
        "Queue contains 4 people, 5 positions, and no first place.",
        "Queue closed; end remains visible for training purposes.",
    ],
    "cup.inspect": [
        "Cup is empty and facing away. This is compliant.",
        "Cup contains still water deep enough for policy, not physics.",
        "Cup inspection stopped when the bottom looked back.",
    ],
    "chair.count": [
        "Chairs counted: 8. Occupants expected: 7. Difference accepted.",
        "Chair count changed while report was open. Displaying earlier count: 6.",
        "No chairs missing. One chair extra and acting senior.",
    ],
    "window.cover": [
        "Window covering request logged. Window status: maybe mirror.",
        "No uncovered windows found. One covered window found watching.",
        "Cover applied to nearest reflective disagreement.",
    ],
    "paper.dry": [
        "Paper remains damp around names only.",
        "Drying request refused: document was filed wet.",
        "Paper dry enough to read but not dry enough to trust.",
    ],
    "ink.test": [
        "Ink age: later than signature.",
        "Ink migration resembles a corridor map. Do not follow.",
        "Ink test complete: black, blue, and one colour not filed.",
    ],
    "tone.sample": [
        "Tone sample: 44.1Hz, or the nearest apology.",
        "Tone sample failed; microphone repeated a previous stairwell.",
        "Tone classified as Class-I unless it begins answering questions.",
    ],
    "basement.name": [
        "Basement designation: Floor -3 for public purposes.",
        "Basement declined name request. Try again from above it.",
        "Basement alias removed from this terminal build.",
    ],
    "lamp.replace": [
        "Lamp replacement deferred until light finishes leaving.",
        "Replacement bulb found already lit in packaging.",
        "Do not replace lamps in Stairwell B while humming persists.",
    ],
})


def _as_float(value: str | None, fallback: float = 0.0) -> float:
    try:
        return float(value) if value is not None else fallback
    except (TypeError, ValueError):
        return fallback


def _as_int(value: str | None, fallback: int = 0) -> int:
    try:
        return int(value) if value is not None else fallback
    except (TypeError, ValueError):
        return fallback


def command_names() -> tuple[str, ...]:
    return tuple(sorted(set(STATIC_COMMANDS) | set(RANDOM_LINES) | set(DYNAMIC_COMMANDS)))


def help_text(show_all: bool = False) -> str:
    core = [
        "Available commands:",
        " help                         Display this message",
        " help all                     Display extended low-clearance command list",
        " whoami                       Display current designation",
        " status                       System status overview",
        " ls                           List visible nodes",
        " ping <node>                  Test connectivity to a node",
        " auth <code>                  Submit restricted invocation authentication code",
        " egress.recall --verify       Verify egress protocol (Δ / ྾2)",
        " debrief.schedule --voluntary Register voluntary debriefing",
        " PCT90156                     [RESTRICTED — see handbook 11.3]",
        " clear                        Clear terminal",
        " exit                         Terminate session",
    ]
    preview = [
        " version                      Display shell build information",
        " motd                         Display current message of the day",
        " notice.roll                  Display an operational notice",
        " handbook.lookup <clause>     Display a handbook clause summary",
        " forms.list                   List known form designations",
        " cymatics.classify <hz>       Classify a frequency band",
        " hydrology.depth <m>          Classify standing-water depth",
        " codex.folia <pages>          Convert pages to folia",
        " archive.status               Report archive queue status",
        " mirror.audit                 Run surface-covering audit",
        " stairwell.listen             Sample stairwell B",
        " log.tail                     Display recent harmless log lines",
        " queue.status                 Display queue state",
        " cup.inspect                  Inspect a cup that should not matter",
    ]
    if not show_all:
        return "\n".join(core + ["", "Additional low-clearance commands:"] + preview + ["", "A complete list of commands is not available at your current rank."])

    extra_lines = ["", "Extended low-clearance command list:"]
    for name in command_names():
        extra_lines.append(f" {name}")
    extra_lines.append("")
    extra_lines.append("Some commands are ceremonial, duplicative, misleading, or maintained only for audit compatibility.")
    return "\n".join(core + extra_lines)




def cmd_date(args: list[str], session: dict) -> str:
    today = date.today()
    endings = [
        "Local policy: clocks may not be used as witnesses without Form T-2.",
        "Local policy: dates observed in mirrors are advisory only.",
        "Local policy: if today repeats, keep the older receipt.",
        "Local policy: the calendar is not liable for rooms that arrive late.",
    ]
    return _join([
        f" Gregorian date : {today.isoformat()}",
        f" Discordian     : {discordian.format_long(today)}",
        f" {random.choice(endings)}",
    ])


def cmd_handbook_lookup(args: list[str], session: dict) -> str:
    if not args:
        return random.choice([" usage: handbook.lookup <clause>", " handbook lookup requires a clause. Do not guess aloud."])
    clause = args[0]
    entry = handbook.lookup(clause)
    if not entry:
        return random.choice([
            f" Clause {clause} is not visible at rank {session.get('rank', 'Trainee')}.",
            f" Clause {clause} exists only in an edition not facing this terminal.",
            f" Clause {clause} returned a covered page.",
        ])
    title, description = entry
    return _join([
        f" Clause {clause}: {title}",
        f" Summary: {description}",
        random.choice([
            " Full text: consult the handbook edition facing away from the window.",
            " Full text: available from Archive after the page agrees to be numbered.",
            " Full text: redacted at low clearance, or pretending to be.",
        ]),
    ])


def cmd_handbook_random(args: list[str], session: dict) -> str:
    clause = random.choice(list(handbook.CLAUSES.keys()))
    title, description = handbook.CLAUSES[clause]
    return _join([
        f" Random clause: {clause} — {title}",
        f" {description}",
        random.choice([
            " Random selection does not constitute authorisation.",
            " Random selection was witnessed by the shelf.",
            " Randomness is approximate inside the archive.",
        ]),
    ])


def cmd_forms_list(args: list[str], session: dict) -> str:
    footer = random.choice([
        "Not all forms are willing to be listed.",
        "Duplicate forms may have different handwriting.",
        "Submit only dry copies unless the form began wet.",
    ])
    return "Known forms:\n " + "\n ".join(forms.all_forms()) + f"\n{footer}"


def cmd_forms_lookup(args: list[str], session: dict) -> str:
    if not args:
        return " usage: forms.lookup <designation>"
    return random.choice([
        f" {args[0]} → {forms.lookup(args[0])}",
        f" form {args[0]} resolves to: {forms.lookup(args[0])}",
        f" lookup complete / {args[0]} / {forms.lookup(args[0])}",
    ])


def cmd_rank_required(args: list[str], session: dict) -> str:
    return _join([
        " Restricted invocation rank requirement:",
        f" {auth.required_rank()}",
        random.choice([
            " This does not open a restricted command by itself.",
            " Knowing the rank is not the same as being it.",
            " The terminal has logged your curiosity without judgement.",
        ]),
    ])


def cmd_rank_list(args: list[str], session: dict) -> str:
    visible = ["Trainee", "Junior", "Senior", "Limonology", "Codicology", "Hauntology", "The High"]
    suffix = random.choice([
        "Rank order may be ceremonial after Hauntology.",
        "This list is visible, not complete.",
        "Do not cite this list in a promotion request.",
    ])
    return "Rank registry view:\n " + "\n ".join(visible) + f"\n{suffix}"


def cmd_cymatics_classify(args: list[str], session: dict) -> str:
    if not args:
        return " usage: cymatics.classify <hz>"
    hz = _as_float(args[0], -1.0)
    band = cymatics.classify_frequency(hz)
    return _join([
        f" frequency : {hz:g} Hz",
        f" band      : {band}",
        random.choice([
            " action    : file only if the sound repeats after being noticed",
            " action    : do not hum back unless supervised",
            " action    : compare against Stairwell B only from above it",
        ]),
    ])


def cmd_cymatics_scan(args: list[str], session: dict) -> str:
    hz = random.choice([17.5, 19.0, 31.0, 44.1, 73.0, 120.0, 200.0, 404.0, 2001.0])
    return _join([
        random.choice(["Cymatic scan complete.", "Cymatic scan almost complete enough.", "Passive cymatic sample accepted."]),
        f" Dominant detected frequency: {hz:g} Hz",
        f" Classification: {cymatics.classify_frequency(hz)}",
        random.choice([
            " Note: terminal microphone not calibrated for doors that breathe.",
            " Note: sample may contain reflected footsteps.",
            " Note: archive shelves introduce soft bias near 44.1Hz.",
        ]),
    ])


def cmd_hydrology_depth(args: list[str], session: dict) -> str:
    if not args:
        return " usage: hydrology.depth <metres>"
    depth = _as_float(args[0], 0.0)
    return _join([
        f" depth          : {depth:g} m",
        f" classification : {hydrology.classify_depth(depth)}",
        f" static pressure: {hydrology.static_pressure(depth):.2f} Pa",
        random.choice([
            " reminder       : do not disturb still water that contains corridor light",
            " reminder       : reflected depth is not a safe measurement",
            " reminder       : water that remembers footsteps is not still enough",
        ]),
    ])


def cmd_hydrology_pressure(args: list[str], session: dict) -> str:
    if not args:
        return " usage: hydrology.pressure <metres>"
    depth = _as_float(args[0], 0.0)
    return random.choice([
        f" hydrostatic pressure at {depth:g} m: {hydrology.static_pressure(depth):.2f} Pa",
        f" pressure estimate: {hydrology.static_pressure(depth):.2f} Pa at {depth:g} m / witness not included",
        f" pressure reading accepted: {hydrology.static_pressure(depth):.2f} Pa. The water remained still enough.",
    ])


def cmd_codex_folia(args: list[str], session: dict) -> str:
    if not args:
        return " usage: codex.folia <pages>"
    pages = _as_int(args[0], 0)
    return random.choice([
        f" {pages} pages → {codicology.pages_to_folia(pages)} folia",
        f" foliation estimate: {codicology.pages_to_folia(pages)} folia from {pages} pages",
        f" {pages} pages counted. One page looked back. Estimated folia: {codicology.pages_to_folia(pages)}",
    ])


def cmd_codex_quire(args: list[str], session: dict) -> str:
    if not args:
        return " usage: codex.quire <pages> [binio|ternio|quaternio|quinternio|sexternio]"
    pages = _as_int(args[0], 0)
    preferred = args[1] if len(args) > 1 else "quaternio"
    count, leftover = codicology.estimate_quire_structure(pages, preferred)
    return _join([
        f" preferred structure : {preferred}",
        f" full quires         : {count}",
        f" leftover folia      : {leftover}",
        random.choice([
            " archive note       : incomplete quires sometimes continue on the shelf behind them",
            " archive note       : do not unfold quires that remember the press",
            " archive note       : margin sounds are not annotations",
        ]),
    ])


def cmd_hex_encode(args: list[str], session: dict) -> str:
    if not args:
        return " usage: hex.encode <text>"
    encoded = hex_codec.encode_hex(" ".join(args))
    if random.random() < 0.25:
        return f"{encoded}\nhex register note: encoded strings are not automatically meaningful."
    return encoded


def cmd_hex_decode(args: list[str], session: dict) -> str:
    if not args:
        return " usage: hex.decode <hex>"
    decoded = hex_codec.decode_hex("".join(args))
    if not decoded:
        return random.choice(["decode failed or produced silence", "hex decode returned a covered result", "decode failed; input may be a corridor pretending to be data"])
    if random.random() < 0.25:
        return decoded + "\nDecoded text should not be read near the cafeteria queue."
    return decoded


def cmd_archive_status(args: list[str], session: dict) -> str:
    variants = [
        ["Archive status:", " incoming crates ............... 11", " crates that arrived twice ..... 2", " signatures preserved .......... yes", " palimpsest review ............. pending until the ink sleeps"],
        ["Archive queue:", " dry boxes ..................... 9", " damp boxes .................... 3", " boxes denying containment ..... 1", " staff recommendation .......... do not stack apologies"],
        ["Archive status degraded:", " shelf labels .................. facing inward", " retrieval staff ............... almost present", " crate 0 ....................... counted as training material"],
    ]
    return _join(random.choice(variants))


def cmd_archive_request(args: list[str], session: dict) -> str:
    if not args:
        return " usage: archive.request <file-or-topic>"
    return _join([
        f" Request received for: {' '.join(args)}",
        random.choice([" Retrieval window: within the current quarter", " Retrieval window: when the shelf admits sequence", " Retrieval window: prior to the next dry audit"]),
        random.choice([" Condition: requester must not read the file before it is found", " Condition: file may request requester first", " Condition: do not bring a mirror into Archive East"]),
    ])


def cmd_corridor_map(args: list[str], session: dict) -> str:
    maps = [
        ["Corridor map view: LOW CLEARANCE", "Δ-01 → Δ-02 → Δ-03 → Δ-04 → Δ-05", "    ↘ [administratively absent]", "྾2-A* → ྾2-B → ྾2-C → ྾2-D", "* not all marked doors correspond to rooms"],
        ["Corridor map view: TRAINING", "Start at here", "Turn away from the third hum", "Ignore the first repeated exit", "Arrive where the floor remembers being dry"],
        ["Corridor map unavailable.", "Reason: route currently using itself.", "Try again after Standing Quiet."],
    ]
    return _join(random.choice(maps))


def cmd_lift_status(args: list[str], session: dict) -> str:
    return _join(random.choice([
        ["Lift A: service normal, mirror covered", "Lift B: service limited; stops at -3 when not addressed", "Lift C: removed from floor plan, still responds to button light", "Lift D: never installed; do not wait inside it"],
        ["Lift report:", " A: dry", " B: occupied by unpressed buttons", " C: visible only from corridor cache", " D: not to be discussed before 06:00"],
        ["Lift service degraded.", "Take the stairs only if the stairs do not take you first."],
    ]))


def cmd_room_query(args: list[str], session: dict) -> str:
    if not args:
        return " usage: room.query <room>"
    target = " ".join(args)
    variants = [
        f"Room {target}: booked by Office of Inherited Silences until previous notice.",
        f"Room {target}: administratively merged with a corridor that denies this.",
        f"Room {target}: vacant, except for the chair count.",
        f"Room {target}: available only to staff already inside.",
        f"Room {target}: door present; room pending.",
        f"Room {target}: listed in the handbook margin but not in Facilities inventory.",
        f"Room {target}: occupied by its previous meeting.",
        f"Room {target}: safe for storage of paper, not names.",
    ]
    return random.choice(variants)


def cmd_node_trace(args: list[str], session: dict) -> str:
    if not args:
        return " usage: node.trace <node>"
    target = args[0]
    hop2 = random.choice(["corridor-cache / repeated", "wet-relay / slower than itself", "lift-B / stopped between packets", "archive-east / filed by sound"])
    return _join([
        f" tracing route to {target}",
        f" hop 1: {session.get('node', 'Δ-04')} / acknowledged",
        f" hop 2: {hop2}",
        " hop 3: [redacted] / politely refused",
        random.choice([f" result: {target} cannot be trusted to be where it says it is", f" result: {target} responded from nearby, not there", f" result: route complete but unhelpful"]),
    ])


def cmd_node_quarantine(args: list[str], session: dict) -> str:
    if not args:
        return " usage: node.quarantine <node>"
    return _join([
        f" Quarantine request opened for {args[0]}",
        random.choice([" status: advisory only at current rank", " status: visible but not enforceable", " status: filed under ceremonial caution"]),
        f" ticket: Q-NODE-{random.randint(1000, 9999)}-UNVERIFIED",
    ])


def cmd_report_anomaly(args: list[str], session: dict) -> str:
    if not args:
        return " usage: report.anomaly <description>"
    ticket = random.randint(1000, 9999)
    return _join([
        f" Anomaly report #{ticket} accepted.",
        f" Description: {' '.join(args)}",
        f" Recommended form: {forms.lookup('anomaly')}",
        random.choice([" A representative may contact you before the event that produced the report.", " Do not correct the report if it begins describing you.", " Report will be reviewed after it stops being current."]),
    ])


def cmd_ticket_open(args: list[str], session: dict) -> str:
    subject = " ".join(args) if args else "unspecified maintenance concern"
    return _join([
        " Ticket opened.",
        f" Subject: {subject}",
        f" Reference: SW-T-{random.randint(10000, 99999)}",
        random.choice([" Status: waiting for a department to admit jurisdiction", " Status: received by Facilities, returned by room", " Status: open, but not facing you"]),
    ])


def cmd_inventory_sample(args: list[str], session: dict) -> str:
    sample = random.sample([
        "covered mirror", "unlabelled brass key", "wet floor sign", "blank badge", "folded chair", "receipt for an unopened door", "orange lightbulb", "sealed suggestion", "cup facing away", "stairwell tone card", "dry sponge", "archive twine", "clock hand without clock", "doorstop labelled previous",
    ], 4)
    footer = random.choice(["Inventory samples are representative only.", "Do not return sampled objects to rooms that ask for them.", "One sampled item may be theoretical."])
    return "Inventory sample:\n " + "\n ".join(sample) + f"\n{footer}"


def cmd_floor_plan(args: list[str], session: dict) -> str:
    return _join(random.choice([
        ["Floor plan request: degraded view", "Δ-levels: 01, 02, 03, 04, 05", "lower service: -1, -2, -3, [-4 removed]", "reminder: a floor omitted from a plan may still support weight"],
        ["Floor plan request: mirrored view refused", "Known floors: enough", "Unknown floors: one too many", "Use corridor.map for a less accurate answer."],
        ["Floor plan unavailable while the building is being remembered from below."],
    ]))


def cmd_registry_lookup(args: list[str], session: dict) -> str:
    if not args:
        return " usage: registry.lookup <term>"
    term = " ".join(args)
    return _join([
        f" Registry lookup: {term}",
        random.choice([" visible matches: 0", " visible matches: 1, but it looked away", " visible matches: too many to trust"]),
        random.choice([" near matches: 3", " near matches: filed by smell", " near matches: one chair, one receipt, one staff member"]),
        random.choice([" conclusion: term may have been filed under the sound it made", " conclusion: consult an older drawer", " conclusion: search successful but not useful"]),
    ])


def cmd_seal_verify(args: list[str], session: dict) -> str:
    if not args:
        return " usage: seal.verify <seal>"
    return _join([
        f" Seal verification for {args[0]}",
        random.choice([" wax temperature: room", " wax temperature: yesterday", " wax temperature: not relevant but recorded"]),
        random.choice([" signature: present but facing inward", " signature: copied from the fold", " signature: waiting for witness"]),
        random.choice([" result: seal is probably still deciding", " result: do not open unless the seal asks first", " result: verification adjacent to success"]),
    ])


def cmd_name_check(args: list[str], session: dict) -> str:
    if not args:
        return " usage: name.check <name>"
    return _join([
        f" Name hygiene check: {' '.join(args)}",
        random.choice([" former-colleague collision: none visible", " former-colleague collision: one possible echo", " former-colleague collision: not available at current rank"]),
        random.choice([" corridor echo collision: inconclusive", " corridor echo collision: delayed", " corridor echo collision: answered before query"]),
        random.choice([" recommendation: write it once, then cover the page", " recommendation: do not say it in Stairwell B", " recommendation: keep a spare designation dry"]),
    ])


def cmd_echo(args: list[str], session: dict) -> str:
    if not args:
        return ""
    text = " ".join(args)
    variants = [
        text,
        text + "\n" + " ".join(args[::-1]),
        text + "\n" + text.lower(),
        text + "\n[echo returned without witness]",
        text + "\n" + text.replace("a", "à") if "a" in text else text,
    ]
    return random.choice(variants)


def cmd_cat(args: list[str], session: dict) -> str:
    if not args:
        return " usage: cat <file>"
    target = args[0]
    return random.choice([
        _join([f"cat: {target}: file visible but not willing", "Try archive.request if the file has not already requested you."]),
        f"cat: {target}: permission denied by shelf, not filesystem",
        f"cat: {target}: output withheld because the margins are awake",
        f"cat: {target}: file opened into another room",
    ])


def cmd_sleep(args: list[str], session: dict) -> str:
    return random.choice([
        "sleep denied: terminals are not permitted to dream during business hours",
        "sleep deferred until after Standing Quiet",
        "sleep accepted for 0 seconds; wake reason: corridor",
        "sleep refused by Archive East. You may blink instead.",
    ])


DYNAMIC_COMMANDS = {
    "date": cmd_date,
    "handbook.lookup": cmd_handbook_lookup,
    "handbook.random": cmd_handbook_random,
    "forms.list": cmd_forms_list,
    "forms.lookup": cmd_forms_lookup,
    "rank.required": cmd_rank_required,
    "rank.list": cmd_rank_list,
    "cymatics.classify": cmd_cymatics_classify,
    "cymatics.scan": cmd_cymatics_scan,
    "hydrology.depth": cmd_hydrology_depth,
    "hydrology.pressure": cmd_hydrology_pressure,
    "codex.folia": cmd_codex_folia,
    "codex.quire": cmd_codex_quire,
    "hex.encode": cmd_hex_encode,
    "hex.decode": cmd_hex_decode,
    "archive.status": cmd_archive_status,
    "archive.request": cmd_archive_request,
    "corridor.map": cmd_corridor_map,
    "lift.status": cmd_lift_status,
    "room.query": cmd_room_query,
    "node.trace": cmd_node_trace,
    "node.quarantine": cmd_node_quarantine,
    "report.anomaly": cmd_report_anomaly,
    "ticket.open": cmd_ticket_open,
    "inventory.sample": cmd_inventory_sample,
    "floor.plan": cmd_floor_plan,
    "registry.lookup": cmd_registry_lookup,
    "seal.verify": cmd_seal_verify,
    "name.check": cmd_name_check,
    "echo": cmd_echo,
    "cat": cmd_cat,
    "sleep": cmd_sleep,
}


def run(command_name: str, args: list[str], session: dict) -> str:
    command_name = command_name.lower()
    if command_name in DYNAMIC_COMMANDS:
        return DYNAMIC_COMMANDS[command_name](args, session)
    if command_name in RANDOM_LINES:
        return random.choice(RANDOM_LINES[command_name])
    if command_name in STATIC_COMMANDS:
        return _choice_block(STATIC_COMMANDS[command_name])
    return random.choice([
        f"{command_name}: command has been catalogued but not remembered",
        f"{command_name}: interface variance exceeded available output",
        f"{command_name}: command visible but ceremonially empty",
    ])
