def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    letter_counts = {}
    for letter in test:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
  
    max_count = 0
    most_frequent_letters = []
    for letter, count in letter_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_letters = [letter]
        elif count == max_count:
            most_frequent_letters.append(letter)
  
    return {letter: count for letter, count in letter_counts.items() if letter in most_frequent_letters}
