def sorted_dict(data):
    """Given list of Strings, return a dictionary
    containing the number of occurrences of each string, sorted by value, key.
    
    Example:
    sorted_dict(['test', 'test']) == {'test': 2}
    sorted_dict(['abc', 'test', 'test', 'abc', 'def', 'test']) == {'test': 3, 'abc': 2, 'def': 1}
    sorted_dict([]) == {}
    """
    counts = {}
    for s in data:
        if s not in counts:
            counts[s] = 1
        else:
            counts[s] += 1
    return {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
