

FORMS = ('S-94d', 'S-85a', 'S-15b', 'S-88a')


def list_forms():
    return list(FORMS)


def lookup_form(code):
    code = str(code).upper()
    return code if code in FORMS else None
