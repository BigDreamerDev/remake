

FORMS = ('S-21b', 'S-46c', 'S-54b', 'S-43c')


def list_forms():
    return list(FORMS)


def lookup_form(code):
    code = str(code).upper()
    return code if code in FORMS else None
