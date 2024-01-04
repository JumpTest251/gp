import re


def verify_ipv6(s) -> bool:
    """ 
    Check if in given String is a valid IPv6 address.
    return True if valid, else False

    >>> verify_ipv6("abc")
    False
    >>> verify_ipv6("2001:0db8:85a3:08d3:1319:8a2e:0370:7344")
    True
    >>> verify_ipv6("2001:db8:0:8d3:0:8a2e:70:7344")
    True
    """
    ipv6_pattern = r"^[0-9a-fA-F]{1,4}:([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    if re.match(ipv6_pattern, s):
        return True
    else:
        return False