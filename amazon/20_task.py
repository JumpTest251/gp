def verify_mail(mail) -> bool:
    """ Check if in given String is a valid mail address.
    >>> verify_mail("abc")
    False
    >>> verify_mail("abc@abc.com")
    True
    """
    return "@" in mail