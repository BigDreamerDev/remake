





STATUS = "archival"
CLAUSE = "3.7"
DEPARTMENT = "Soft Alarms"


def describe():
    return {"department": DEPARTMENT, "clause": CLAUSE, "status": STATUS}


def validate_payload(payload):
    return isinstance(payload, dict) and payload.get("department") != "unassigned"
