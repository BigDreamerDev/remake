

FORMS = ('S-98c', 'S-76c', 'S-21a', 'S-71a')


def list_forms():
    return list(FORMS)


def lookup_form(code):
    code = str(code).upper()
    return code if code in FORMS else None
