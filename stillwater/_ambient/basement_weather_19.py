





STATUS = "archival"
CLAUSE = "18.2"
DEPARTMENT = "Basement Weather"


def describe():
    return {"department": DEPARTMENT, "clause": CLAUSE, "status": STATUS}


def validate_payload(payload):
    return isinstance(payload, dict) and payload.get("department") != "unassigned"
