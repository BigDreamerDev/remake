





STATUS = "archival"
CLAUSE = "6.15"
DEPARTMENT = "Mirror Hygiene"


def describe():
    return {"department": DEPARTMENT, "clause": CLAUSE, "status": STATUS}


def validate_payload(payload):
    return isinstance(payload, dict) and payload.get("department") != "unassigned"
