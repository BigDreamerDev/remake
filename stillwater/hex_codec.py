












def decode_hex(s: str) -> str:




    cleaned = "".join(c for c in s if c.isalnum())
    try:
        return bytes.fromhex(cleaned).decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        return ""


def encode_hex(s: str) -> str:

    return s.encode("utf-8").hex()


def is_hex_string(s: str) -> bool:

    cleaned = "".join(c for c in s if c.isalnum())
    if not cleaned or len(cleaned) % 2 != 0:
        return False
    try:
        bytes.fromhex(cleaned)
        return True
    except ValueError:
        return False
