













FORMS = {
    "denied_auth":              "Form D-17(b)",
    "restricted_invocation":    "Form D-17(b)",
    "anomaly":                  "Form PI-3",
    "audible_anomaly":          "Form HA-9",
    "visual_anomaly":           "Form HA-12",
    "vending_return":           "Form V-9",
    "locker_reclamation":       "Form R-31",
    "device_confiscation":      "Form C-22",
    "memorial_attendance":      "Form M-1",
    "voluntary_debrief":        "Form D-12(v)",
    "involuntary_debrief":      "Form D-12(i)",
    "missing_photograph":       "Form P-7",
    "reflection_report":        "Form HA-12",
    "unrecognised_gift":        "Form G-4",
    "stairwell_audio":          "Form HA-9",
}


def lookup(category: str) -> str:

    return FORMS.get(category, "Form N/A")


def all_forms():

    return sorted(set(FORMS.values()))
