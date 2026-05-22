# stillwater-libs​‌‌‌​‌​​​‌‌​‌​​​​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌‌​​‌​​‌‌​​​​‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌​‌‌‌‌‌​‌‌​​‌‌​​‌‌​​​​‌​‌‌​‌‌​​​‌‌​‌‌​​​‌‌‌​​‌‌​‌​‌‌‌‌‌​‌‌​‌​​​​‌‌​​‌​‌​‌‌​​​​‌​‌‌‌​‌‌​​‌‌‌‌​​‌​‌​‌‌‌‌‌​‌‌‌​‌‌‌​‌‌​‌​​​​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌‌​‌​​​‌‌​‌​​​​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌​​​‌​​‌‌​​‌​‌​‌‌​​​​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌​‌‌‌‌‌​‌‌​‌‌​​​‌‌​‌​​‌​‌‌​​‌​‌​‌‌‌​​‌‌​‌​‌‌‌‌‌​‌‌​‌‌​​​‌‌​‌​​‌​‌‌​​‌‌‌​‌‌​‌​​​​‌‌‌​‌​​​‌‌​‌‌​​​‌‌‌‌​​‌

> Part of a wider ARG. Ignore this repository if you are not meant to be here. - ARG players, if you have a github account follow the Repo for stat tracking

> Internal libraries for the **Stillwater Foundation**, consolidated for use across all departments.

This repository contains the canonical implementation of the Foundation's shared utilities, including:

- `stillwater.pattern_integrity` — Pattern Integrity sensor reporting
- `stillwater.cymatics` — acoustic monitoring (see Clause 2.8)
- `stillwater.hydrology` — still-water site survey utilities (Clause 14.2)
- `stillwater.codicology` — archive document handling (Clause 21.2)
- `stillwater.discordian` — Discordian calendar conversion (Clause 22.1)
- `stillwater.hex_codec` — sentinel-node identifier resolution
- `stillwater.nodes` — node listing and connectivity
- `stillwater.egress` / `stillwater.debrief` — operational protocols
- `stillwater.handbook` — programmatic access to handbook clauses
- `stillwater.auth` — restricted-command authentication

The entry point `main.py` provides the **comShell** REPL, the canonical interface for issuing commands against the consolidated libraries.

## Authorisation

The `PCT90156` command is reserved. Invocation requires an authentication code; see employee handbook, Clause: 11.3 Subsection: Restricted Invocations. Unauthorised invocations are logged but do not, in themselves, constitute a disciplinary event.

---

**Notice to employees:**

* All servers are down until the `4E6F72646C616E64` (See employee handbook, Clause: 6.19 Subsection: Titan-Class) event at 0600 on Bcy 28, 3192 YOLD.

* Employees are reminded not to call the `PCT90156` command within comShell until the Server-wide Restart PiP to all internal Nodes within buildings Δ and ྾2. Access is reserved to Employees of Rank Limonology. The High reminds all users to not contact the Pattern Integrity Working Group until the date of the `4E6F72646C616E64` event. (See employee handbook, Clause: 11.3 Subsection: Restricted Invocations.)

* The cafeteria on Floor -3 will be closed from 02:00 to 04:00 daily for routine descaling. Employees of Rank Codicology and above may request meal substitutions via Form S-44b. Do not enter the cafeteria during these hours, **even if you hear voices you recognise**. (See employee handbook, Clause: 7.7 Subsection: Acoustic Persistence.)

* The `426F726465726C616B65` quarterly inspection has been postponed indefinitely. Survey teams are NOT to enter the perimeter under any circumstance. The previous notice listing safe approach vectors is rescinded in full. (See employee handbook, Clause: 14.2 Subsection: Standing Water.)

* Effective immediately, the use of the phrase *"as it was"* in interdepartmental communication is restricted to Rank Hauntology and above. Repeated violations will be addressed via Form D-17(b). The High has emphasised that this is not a stylistic preference. (See employee handbook, Clause: 5.1 Subsection: Verbal Continuity.)

* All meetings previously scheduled in Conference Room ྾2-A have been relocated. Conference Room ྾2-A no longer exists administratively. Employees who continue to receive calendar invites for ྾2-A should report this immediately to the Office of Inherited Silences — *not* to IT. (See employee handbook, Clause: 19.0 Subsection: Administrative Absences.)

* Reports of "irregular reflections" in the east wing of building Δ should be filed using Form HA-12, not Form HA-9. Form HA-9 is for *audible* anomalies only. Repeated misfiling will be logged. (See employee handbook, Clause: 7.1 Subsection: Permitted Surfaces.)

* The seventh entry in the visitor log for any given day is to remain blank. Do not sign the seventh entry. Do not assign the seventh entry. Do not look at the seventh entry once it has been left blank. (See employee handbook, Clause: 9.7 Subsection: Enumerated Absences.)

* As of 47 days ago, building ྾2 has been reclassified as Class-IV (Stabilized). Employees continuing routine duties in ྾2 should familiarise themselves with the revised egress protocol via `comShell> egress.recall --verify`. Under no circumstance is `egress.recall --force` to be invoked outside the presence of a Tier-IV witness. (See employee handbook, Clause: 20.0 Subsection: Reclassified Structures.)

* The Pattern Integrity Working Group has requested that no employee invoke the names of decommissioned departments in any internal communication, including draft emails not yet sent. A list of decommissioned departments may be obtained from your direct supervisor. The list itself is not to be circulated, duplicated, or retained beyond a single viewing. (See employee handbook, Clause: 13.4 Subsection: Departmental Dissolution.)

* The Wednesday soup is no longer available. Culinary inquiries are to be directed to the Bureau of Inherited Silences, *not* to kitchen staff. Kitchen staff have been reminded of this for the third time. (See employee handbook, Clause: 8.0 Subsection: Discontinued Provisions.)

* All employees of Rank Limonology and below are reminded that personal mirrors in workstations must be covered between 23:00 and 04:00, regardless of shift assignment. This applies to reflective surfaces in general, including monitors in sleep mode. (See employee handbook, Clause: 7.2 Subsection: Reflective Discipline.)

* The `506F6E64726F6F6D` rotation schedule for Q4 has been amended. Employees previously assigned to the third rotation are now assigned to the first. Employees previously assigned to the first rotation are not to ask why. (See employee handbook, Clause: 16.8 Subsection: Rotational Assignment.)

* The annual `53616C746D61727368` Memorial Ceremony will be held in the Atrium of building Δ on Bcy 50, 3192 YOLD at 11:11. Attendance is mandatory for Rank Bryology and above. The ceremony is to be observed in silence; **the silence is not to be broken under any provocation**. (See employee handbook, Clause: 22.1 Subsection: Communal Observances.)

* Personal effects left in lockers on Floor -2 will be incinerated after 72 hours, regardless of contents. Items reclaimed from incineration via Form R-31 will be returned in a *substantively similar* condition. The Office of Inherited Silences does not entertain disputes regarding "substantive similarity." (See employee handbook, Clause: 18.5 Subsection: Personal Property.)

* The lobby clock in building ྾2 is not to be reset, reprogrammed, or referenced in any official correspondence. The time displayed is correct. (See employee handbook, Clause: 4.4 Subsection: Local Time.)

* Photography of the south face of building Δ is prohibited at all hours. This includes incidental photography in which the south face appears in the background. Confiscated devices will be returned via Form C-22 after a review period of 90 days, *less any images recovered*. (See employee handbook, Clause: 19.4 Subsection: Photographic Discretion.)

* Effective the next observance of Pungenday, all internal correspondence is to be signed using the Diplomatics-approved closing phrase. The previously approved phrase ("Regards") has been withdrawn from circulation. The new phrase will be communicated to each employee individually and is not to be shared. (See employee handbook, Clause: 12.2 Subsection: Approved Correspondence.)

* The `5468726573686F6C64` Audit is scheduled for Bcy 35, 3192 YOLD. Employees of Rank Karstology and above are required to submit their personal logs no later than 48 hours prior. Personal logs are not to contain references to the audit itself. This is the third such reminder. (See employee handbook, Clause: 21.7 Subsection: Recorded Reviews.)

* The vending machine on Floor -3 has been removed from active inventory. Employees who continue to receive change from the vending machine are asked to deposit the change in the receptacle marked "Returns" and to report the incident via Form V-9. **Do not spend the change.** (See employee handbook, Clause: 5.5 Subsection: Vended Items.)

* Whistleblower protections have been re-affirmed under Clause: 17.1 Subsection: Permitted Disclosures. Employees wishing to invoke these protections should first consult the list of permitted disclosures, available exclusively in the locked reading room of the Codicology wing. Reading-room access is reserved for the duration of the invocation only.

* The Suggestion Box outside the Pattern Integrity Working Group is operational. Suggestions are read, classified, and archived. They are not, under any circumstance, *acted upon*. Repeated suggestions of an actionable nature will be referred to the Office of Inherited Silences. (See employee handbook, Clause: 2.6 Subsection: Submitted Sentiments.)

* The annual Phenology Review will not take place this year. Employees who have been notified that they are scheduled to attend the Phenology Review should disregard their notification but are not to delete it. Notifications must be retained until the next Phenology Review, the date of which has not been set. (See employee handbook, Clause: 13.0 Subsection: Postponed Observances.)

* The `4D6F737367617465` corridor on sub-level 5 has been administratively merged with the `506F6E64726F6F6D` corridor on sub-level 6. Maps in current employee handbooks may not yet reflect this change. Employees who encounter discrepancies between the map and the corridor should *trust the corridor*. (See employee handbook, Clause: 20.3 Subsection: Spatial Reconciliation.)

* Singing, humming, and whistling are not permitted in stairwell B between the hours of 17:00 and 19:00. This includes humming below the threshold of conscious awareness. Cymatic monitoring is in effect. (See employee handbook, Clause: 2.8 Subsection: Acoustic Continence.)

* The Foundation's name is not to be spoken aloud in the presence of visitors. Visitors who ask the name of the organisation are to be referred to Reception, where they will be provided with the appropriate response. The appropriate response is updated quarterly. (See employee handbook, Clause: 1.1 Subsection: Names Not Said.)

* Employees are not to refer to former colleagues by their full names in unsecured channels. Surnames alone are permitted. First names are permitted. The combination is not. (See employee handbook, Clause: 12.6 Subsection: Onomastic Hygiene.)

* The car park has been resurfaced. The new line markings reflect updated containment geometry and are not to be crossed when leaving a vehicle. Crossing the markings will not result in disciplinary action but is *strongly* discouraged. (See employee handbook, Clause: 16.3 Subsection: Vehicular Geometry.)

* Birthday cards circulated in the office are to be reviewed by Rank Sigillography prior to signing. This is not a new policy. Employees who do not recall the policy are advised to review the handbook in full. (See employee handbook, Clause: 3.3 Subsection: Wishes Recorded and Unrecorded.)

* The lift on the east side of building Δ has been recalibrated. Employees who experience the lift travelling to a floor that was not selected are not to disembark. The lift will return to the correct floor after a brief delay. **Do not press any further buttons during the delay.** (See employee handbook, Clause: 10.4 Subsection: Vertical Conveyance.)

* The Foundation does not employ a Mr. `437265737377656C6C`. Communications addressed to Mr. `437265737377656C6C` should be returned to the Office of Inherited Silences unopened. *They are not to be opened to verify the addressee.* (See employee handbook, Clause: 18.7 Subsection: Returned Correspondence.)

* The Stillwater Foundation Annual Photograph will be taken in the Atrium of building Δ at 14:30 on Bcy 49, 3192 YOLD. Employees of all ranks are required to attend. Employees who do not appear in the developed photograph are asked to report to the Pattern Integrity Working Group within 24 hours. (See employee handbook, Clause: 6.6 Subsection: Photograph Attendance.)

* The archive is undergoing routine deduplication. Employees who locate duplicates of documents bearing their own signature should *not* destroy them. Both versions are to be filed. The reason for this will be explained at the next All-Hands. (See employee handbook, Clause: 21.2 Subsection: Archive Integrity.)

* Building `44726966746D6F6F72` (formerly building ྾3) is not currently in service. Employees who recall attending meetings in building `44726966746D6F6F72` are encouraged to register for the next available debriefing via `comShell> debrief.schedule --voluntary`. (See employee handbook, Clause: 20.1 Subsection: Structures No Longer in Service.)

* The Foundation's emergency evacuation siren has been replaced. The new tone is significantly quieter and may be mistaken for a distant bell. Employees are advised to evacuate regardless of perceived volume. Inability to hear the siren is not, in itself, evidence of its absence. (See employee handbook, Clause: 15.5 Subsection: Audible Warnings.)

* Inter-departmental gifts exceeding £20 in value require review by Rank Hauntology under Clause: 8.2 Subsection: Permitted Reciprocity. Gifts of unspecified origin, including those that appear on desks overnight, are to be reported to the Office of Inherited Silences and not opened.

* The Foundation observes a minute of silence at 14:14 each Setting Orange. Employees are reminded that the silence is communal but **not synchronised**; do not adjust your observance to match those of nearby employees. (See employee handbook, Clause: 25.0 Subsection: Standing Quiet.)

* The All-Hands meeting has been postponed indefinitely.

---

*Maintained by the Office of Inherited Silences.*
