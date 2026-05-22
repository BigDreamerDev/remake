










from stillwater.hex_codec import decode_hex



_VISIBLE_NODES = [
    "Δ-01", "Δ-02", "Δ-03", "Δ-04", "Δ-05",
    "྾2-A*", "྾2-B", "྾2-C", "྾2-D",
]


_REDACTED_COUNT = 3



_SENTINEL_NODES = {
    "4e6f72646c616e64":     "the event has not yet occurred",
    "426f726465726c616b65": "perimeter sealed. no echo returned.",
    "506f6e64726f6f6d":     "1 packet sent, 0 received, 100% loss",
    "44726966746d6f6f72":   "host not in service",
    "4d6f737367617465":     "administratively merged with another corridor",
    "53616c746d61727368":   "responds only during memorial observance",
    "5468726573686f6c64":   "see audit log",
}


def list_nodes() -> str:

    lines = []
    lines.append("  " + "    ".join(_VISIBLE_NODES[:5]))
    lines.append("  " + "   ".join(_VISIBLE_NODES[5:]))
    lines.append("  " + "   ".join(["[redacted]"] * _REDACTED_COUNT))
    lines.append("")
    lines.append("  * administratively absent")
    return "\n".join(lines)


def ping(target: str) -> str:

    if not target:
        return "  usage: ping <node>"

    low = target.lower()

    
    for hex_name, message in _SENTINEL_NODES.items():
        if low == hex_name or low == decode_hex(hex_name).lower():
            return f"  {target}: {message}"

    
    if low.startswith(("δ-", "d-")):
        return f"  {target}: 4 packets sent, 4 received, 0% loss"

    
    if "2-a" in low:
        return f"  {target}: no route to host (target does not exist)"

    return f"  {target}: timeout"
