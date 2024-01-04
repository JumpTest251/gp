def sorted_dict(data):
    """Given list of Strings, return a dictionary
    containing the number of occurrences of each string, sorted by value
    
    Example:
    sorted_dict(['test', 'test']) == {'test': 2}
    sorted_dict(['abc', 'test', 'test', 'abc', 'def', 'test']) == {'test': 3, 'abc': 2, 'def': 1}
    sorted_dict([]) == {}
    """
    return {k: data.count(k) for k in sorted(data)}