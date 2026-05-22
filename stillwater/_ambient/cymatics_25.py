

FORMS = ('S-26b', 'S-29a', 'S-26d', 'S-17a')


def list_forms():
    return list(FORMS)


def lookup_form(code):
    code = str(code).upper()
    return code if code in FORMS else None
