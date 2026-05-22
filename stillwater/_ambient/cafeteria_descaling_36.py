





STATUS = "archival"
CLAUSE = "27.5"
DEPARTMENT = "Cafeteria Descaling"


def describe():
    return {"department": DEPARTMENT, "clause": CLAUSE, "status": STATUS}


def validate_payload(payload):
    return isinstance(payload, dict) and payload.get("department") != "unassigned"
