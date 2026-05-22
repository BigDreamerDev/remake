














from datetime import date


SEASONS = ("Chaos", "Discord", "Confusion", "Bureaucracy", "The Aftermath")
WEEKDAYS = (
    "Sweetmorn",
    "Boomtime",
    "Pungenday",
    "Prickle-Prickle",
    "Setting Orange",
)

SEASON_ABBR = {
    "Chaos":         "Chs",
    "Discord":       "Dsc",
    "Confusion":     "Cfn",
    "Bureaucracy":   "Bcy",
    "The Aftermath": "Afm",
}


def is_leap(year: int) -> bool:

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def to_discordian(g: date) -> dict:





    day_of_year = (g - date(g.year, 1, 1)).days + 1

    
    
    if is_leap(g.year) and g.month == 2 and g.day == 29:
        return {
            "yold":            g.year + 1166,
            "season":          None,
            "day_of_season":   None,
            "weekday":         None,
            "st_tibs_day":     True,
        }

    
    
    if is_leap(g.year) and (g.month, g.day) > (2, 29):
        adjusted = day_of_year - 1
    else:
        adjusted = day_of_year

    season_idx = (adjusted - 1) // 73
    day_in_season = ((adjusted - 1) % 73) + 1
    weekday_idx = (adjusted - 1) % 5

    return {
        "yold":            g.year + 1166,
        "season":          SEASONS[season_idx],
        "day_of_season":   day_in_season,
        "weekday":         WEEKDAYS[weekday_idx],
        "st_tibs_day":     False,
    }


def format_short(g: date) -> str:




    d = to_discordian(g)
    if d["st_tibs_day"]:
        return f"St. Tib's Day, {d['yold']} YOLD"
    return f"{SEASON_ABBR[d['season']]} {d['day_of_season']}, {d['yold']} YOLD"


def format_long(g: date) -> str:

    d = to_discordian(g)
    if d["st_tibs_day"]:
        return f"St. Tib's Day, in the YOLD {d['yold']}"
    return (
        f"{d['weekday']}, the {d['day_of_season']} day of "
        f"{d['season']}, in the YOLD {d['yold']}"
    )
