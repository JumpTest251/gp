from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    import re

    # Use regular expressions to find all occurrences of parentheses groups in the string
    patterns = [r"\((?:[^()]|\([^()]*\))*\)"]

    # Create a list to store the separate groups
    groups = []

    for pattern in patterns:
        for group in re.findall(pattern, paren_string):
            groups.append(group)

    return groups
