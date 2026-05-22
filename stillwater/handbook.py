












CLAUSES = {
    "1.1":  ("Names Not Said",                "Naming conventions in the presence of visitors."),
    "2.6":  ("Submitted Sentiments",          "Suggestion box handling protocols."),
    "2.8":  ("Acoustic Continence",           "Restrictions on vocalisation in shared spaces."),
    "3.3":  ("Wishes Recorded and Unrecorded",
             "Birthday and commemorative correspondence review."),
    "4.4":  ("Local Time",                    "Lobby and atrium timepiece policy."),
    "5.1":  ("Verbal Continuity",             "Restrictions on phrases denoting prior state."),
    "5.5":  ("Vended Items",                  "Vending machine usage and returns."),
    "6.6":  ("Photograph Attendance",         "Mandatory annual photograph attendance."),
    "6.19": ("Titan-Class",                   "Designation and observance of Titan-Class events."),
    "7.1":  ("Permitted Surfaces",            "Reporting of reflective surface anomalies."),
    "7.2":  ("Reflective Discipline",         "Personal mirror and screen coverings after-hours."),
    "7.7":  ("Acoustic Persistence",          "Cafeteria descaling and adjacent audio events."),
    "8.0":  ("Discontinued Provisions",       "Withdrawal of recurring culinary items."),
    "8.2":  ("Permitted Reciprocity",         "Inter-departmental gift thresholds and review."),
    "9.7":  ("Enumerated Absences",           "Treatment of designated blank entries in logs."),
    "10.4": ("Vertical Conveyance",           "Lift recalibration and unselected floor events."),
    "11.3": ("Restricted Invocations",        "Authorisation procedure for restricted commands."),
    "12.2": ("Approved Correspondence",       "Permitted internal correspondence closings."),
    "12.6": ("Onomastic Hygiene",             "Use of former colleagues' names in communication."),
    "13.0": ("Postponed Observances",         "Handling of indefinitely-postponed annual reviews."),
    "13.4": ("Departmental Dissolution",      "References to and import of decommissioned modules."),
    "14.2": ("Standing Water",                "Survey protocol for designated still-water sites."),
    "15.5": ("Audible Warnings",              "Evacuation siren classification and tonal updates."),
    "16.3": ("Vehicular Geometry",            "Containment-aligned line markings in car parks."),
    "16.8": ("Rotational Assignment",         "Quarterly corridor and node rotations."),
    "17.1": ("Permitted Disclosures",         "Whistleblower invocation reading-room access."),
    "18.5": ("Personal Property",             "Locker contents disposal and reclamation."),
    "18.7": ("Returned Correspondence",       "Handling of mail addressed to non-personnel."),
    "19.0": ("Administrative Absences",       "Re-categorisation of disused meeting spaces."),
    "19.4": ("Photographic Discretion",       "Building-face photography restrictions."),
    "20.0": ("Reclassified Structures",       "Class-IV (Stabilised) buildings and egress."),
    "20.1": ("Structures No Longer in Service",
             "Decommissioned buildings and recall of memory."),
    "20.3": ("Spatial Reconciliation",        "Administrative merging of corridors and rooms."),
    "21.2": ("Archive Integrity",             "Routine deduplication and signature preservation."),
    "21.7": ("Recorded Reviews",              "Audit-period personal log submission."),
    "22.1": ("Communal Observances",          "Memorial ceremony attendance and silence."),
    "25.0": ("Standing Quiet",                "Daily minute of unsynchronised silence."),
}


def lookup(clause: str):

    return CLAUSES.get(clause)


def all_clauses():

    return sorted(CLAUSES.keys(), key=lambda c: tuple(int(p) for p in c.split(".")))








RESTRICTED_RANK_INDEX = 3
