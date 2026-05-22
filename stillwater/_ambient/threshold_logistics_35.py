





STATUS = "archival"
CLAUSE = "12.3"
DEPARTMENT = "Threshold Logistics"


def describe():
    return {"department": DEPARTMENT, "clause": CLAUSE, "status": STATUS}


def validate_payload(payload):
    return isinstance(payload, dict) and payload.get("department") != "unassigned"
