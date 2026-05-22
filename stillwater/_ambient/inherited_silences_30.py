





STATUS = "archival"
CLAUSE = "22.16"
DEPARTMENT = "Inherited Silences"


def describe():
    return {"department": DEPARTMENT, "clause": CLAUSE, "status": STATUS}


def validate_payload(payload):
    return isinstance(payload, dict) and payload.get("department") != "unassigned"
