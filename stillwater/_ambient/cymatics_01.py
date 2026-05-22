

FORMS = ('S-54c', 'S-43a', 'S-22c', 'S-31b')


def list_forms():
    return list(FORMS)


def lookup_form(code):
    code = str(code).upper()
    return code if code in FORMS else None
