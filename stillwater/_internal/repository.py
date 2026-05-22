
















_CIPHER_HEX = (
    "3c1b020c0b0a084f13164c4609000d1c431c0218000c"
    "09400d030d1a141c331d041b0f01330c0b181f1a43020a"
)


def _xor_cycle(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def get_endpoint(auth_key: str) -> str:






    if not auth_key:
        return "[no key supplied]"
    cipher = bytes.fromhex(_CIPHER_HEX)
    plain = _xor_cycle(cipher, auth_key.lower().encode("utf-8"))
    try:
        return plain.decode("utf-8")
    except UnicodeDecodeError:
        return "[decoding failed — key mismatch]"
