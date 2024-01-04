import re

def verify_mail(mail) -> bool:
    """ Check if in given String is a valid mail address.
    >>> verify_mail("abc")
    False
    >>> verify_mail("abc@abc.com")
    True
    """
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    match = re.search(regex, mail)
    return bool(match)