def sorted_dict(data):
    """Given list of Strings, return a dictionary
    containing the number of occurrences of each string, sorted by value, key.

    Example:
    sorted_dict(['test', 'test']) == {'test': 2}
    sorted_dict(['abc', 'test', 'test', 'abc', 'def', 'test']) == {'test': 3, 'abc': 2, 'def': 1}
    sorted_dict([]) == {}
    """
    count_dict = {}
    for item in data:
        count_dict[item] = count_dict.get(item, 0) + 1

    return dict(sorted(count_dict.items(), key=lambda x: (-x[1], x[0])))
