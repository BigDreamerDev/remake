














RANKS = (
    "Trainee",
    "Junior",
    "Senior",
    "Limonology",
    "Codicology",
    "Hauntology",
    "The High",
)


def is_restricted(rank: str) -> bool:

    try:
        return RANKS.index(rank) >= 3
    except ValueError:
        return False
