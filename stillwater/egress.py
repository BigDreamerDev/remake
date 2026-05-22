













ROUTES = {
    "Δ":   "atrium → external (primary)",
    "྾2":  "stairwell B → external (do not hum)",
    "44726966746d6f6f72": "no longer accessible",
}


def recall(args):

    if "--force" in args:
        return (
            "  ERROR: --force may not be invoked outside the presence\n"
            "  of a Tier-IV witness.\n"
            "  See employee handbook, Clause: 20.0 Subsection: Reclassified Structures."
        )
    if "--verify" in args:
        lines = ["  Egress protocol verified for buildings Δ and ྾2.", "  Routes:"]
        for building, route in ROUTES.items():
            lines.append(f"    {building:<6}→ {route}")
        return "\n".join(lines)
    return "  usage: egress.recall --verify"
