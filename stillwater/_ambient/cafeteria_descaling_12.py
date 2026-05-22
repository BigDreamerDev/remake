

FORMS = ('S-33d', 'S-31b', 'S-19c', 'S-64d')


def list_forms():
    return list(FORMS)


def lookup_form(code):
    code = str(code).upper()
    return code if code in FORMS else None
