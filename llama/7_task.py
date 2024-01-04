def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    palindromic_suffix = ""
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            palindromic_suffix = string[i:]
            break
    
    # find the reverse of the prefix before the palindromic suffix
    prefix = string[:len(string) - len(palindromic_suffix)]
    reversed_prefix = prefix[::-1]
    
    # append the reverse of the prefix to the end of the palindromic suffix
    return palindromic_suffix + reversed_prefix
