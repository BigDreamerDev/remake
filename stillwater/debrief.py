










import random



_RESPONSE_WINDOWS = (
    "[REDACTED]",
    "within the current quarter",
    "prior to the next Phenology Review",
    "no later than the next Setting Orange",
)


def schedule(args):

    if "--voluntary" in args:
        window = random.choice(_RESPONSE_WINDOWS)
        return (
            "  Voluntary debriefing request submitted.\n"
            "  A representative of the Office of Inherited Silences will contact you.\n"
            f"  Estimated response time: {window}"
        )
    if "--involuntary" in args:
        return (
            "  --involuntary is reserved for Pattern Integrity Working Group invocation.\n"
            "  See employee handbook, Clause: 13.4 Subsection: Departmental Dissolution."
        )
    return "  usage: debrief.schedule --voluntary"
