











from typing import Iterable



QUIRE_SIZES = {
    "binio":      2,
    "ternio":     3,
    "quaternio":  4,  
    "quinternio": 5,
    "sexternio":  6,
}


FOLIATION_STYLES = ("recto-verso", "roman-numeral", "alphanumeric", "unfoliated")


def folia_to_pages(folia: int) -> int:

    return max(0, folia) * 2


def pages_to_folia(pages: int) -> int:

    if pages <= 0:
        return 0
    return (pages + 1) // 2


def estimate_quire_structure(pages: int, preferred: str = "quaternio") -> tuple:




    quire_folia = QUIRE_SIZES.get(preferred, 4)
    folia = pages_to_folia(pages)
    full = folia // quire_folia
    leftover = folia % quire_folia
    return full, leftover


def is_palimpsest(scan_anomalies: Iterable[str]) -> bool:

    anomalies = list(scan_anomalies)
    if not anomalies:
        return False
    suspicious = {"ghost text", "iron-gall residue", "scraping pattern"}
    return any(a.lower() in suspicious for a in anomalies)
