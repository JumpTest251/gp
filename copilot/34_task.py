def first_non_repeating_character(string):
    """
    Write a python function to find the first non-repeated character in a given string.

    first_non_repeating_character("abcabc") == None
    first_non_repeating_character("abacabad") == "c"
    """
    for char in string:
        if string.count(char) == 1:
            return char
    return None