import re

def check_email(email):
    '''(str) -> bool

    Return True if your email is valid and False if not.

    >>>check_email("user@domain.ru")
    True
    >>>check_email("userdomainru")
    False
    '''

    my_email = re.split(r'\@',email)
    if len(my_email) != 2 or my_email[0] == "" or my_email == "":
        return False

    name  = my_email[0]
    domains = my_email[1]

    if re.search(r'^-|[^a-zA-Z0-9\_\-\.]|-\.|\.-|.{257}|\s|^.{0,2}$|-$', domains) is not None:
        return False

    if re.search(r'\.', domains) is None:
        return False

    if len(re.findall(r'(")', name)) % 2 != 0:
        return False

    if re.search(r'(\.\.)|.{129}|[^!:,a-z0-9"\._-]|\s|(^|[^"])[!:,]"|"[!:,]([^"]|$)|(^|[^"])[!:,]([^"]|$)', name) is not None:
        return False

    return True
