def first_non_repeating_character(string):
    """
    Write a python function to find the first non-repeated character in a given string.

    first_non_repeating_character("abcabc") == None
    first_non_repeating_character("abacabad") == "c"
    """
    # Initialize a dictionary to keep track of the characters and their counts
    char_counts = {}
  
    # Iterate through each character in the input string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_counts[char] = 1
  
    # Iterate through each character in the input string again
    for char in string:
        # If the character's count is 1, it is the first non-repeated character
        if char_counts[char] == 1:
            return char
  
    # If no non-repeated characters are found, return None
    return None