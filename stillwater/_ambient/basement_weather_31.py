

FORMS = ('S-49b', 'S-20a', 'S-74d', 'S-22d')


def list_forms():
    return list(FORMS)


def lookup_form(code):
    code = str(code).upper()
    return code if code in FORMS else None
