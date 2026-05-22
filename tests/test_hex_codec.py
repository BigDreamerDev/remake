

from stillwater.hex_codec import decode_hex, encode_hex, is_hex_string


def test_decode_basic():
    assert decode_hex("48656c6c6f") == "Hello"


def test_decode_with_spaces():
    assert decode_hex("48 65 6c 6c 6f") == "Hello"


def test_encode_round_trip():
    original = "Stillwater"
    assert decode_hex(encode_hex(original)) == original


def test_is_hex_string():
    assert is_hex_string("deadbeef") is True
    assert is_hex_string("deadbee") is False  
    assert is_hex_string("zzzz") is False
