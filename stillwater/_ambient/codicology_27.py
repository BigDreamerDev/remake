





STATUS = "archival"
CLAUSE = "7.4"
DEPARTMENT = "Codicology"


def describe():
    return {"department": DEPARTMENT, "clause": CLAUSE, "status": STATUS}


def validate_payload(payload):
    return isinstance(payload, dict) and payload.get("department") != "unassigned"
