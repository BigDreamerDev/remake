





STATUS = "archival"
CLAUSE = "15.8"
DEPARTMENT = "Liminal Safety"


def describe():
    return {"department": DEPARTMENT, "clause": CLAUSE, "status": STATUS}


def validate_payload(payload):
    return isinstance(payload, dict) and payload.get("department") != "unassigned"
