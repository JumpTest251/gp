def first_non_repeating_character(string):
    """
    Write a python function to find the first non-repeated character in a given string.

    first_non_repeating_character("abcabc") == None
    first_non_repeating_character("abacabad") == "c"
    """
    # create a dictionary to store the frequency of each character
    char_freq = {}

    # loop through the string and add to the dictionary
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # loop through the string again and find the first non-repeated character
    for char in string:
        if char_freq[char] == 1:
            return char

    # if no non-repeated character is found, return None
    return None
