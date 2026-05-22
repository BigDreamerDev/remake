

from datetime import date

from stillwater.discordian import to_discordian, format_short


def test_known_date_bcy_28():
    
    d = to_discordian(date(2026, 9, 4))
    assert d["season"] == "Bureaucracy"
    assert d["day_of_season"] == 28
    assert d["weekday"] == "Boomtime"
    assert d["yold"] == 3192


def test_format_short():
    assert format_short(date(2026, 9, 4)) == "Bcy 28, 3192 YOLD"


def test_st_tibs_day():
    d = to_discordian(date(2024, 2, 29))
    assert d["st_tibs_day"] is True
