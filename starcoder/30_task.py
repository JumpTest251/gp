def sorted_dict(data):
    """Given list of Strings, return a dictionary
    containing the number of occurrences of each string, sorted by value, key.
    
    Example:
    sorted_dict(['test', 'test']) == {'test': 2}
    sorted_dict(['abc', 'test', 'test', 'abc', 'def', 'test']) == {'test': 3, 'abc': 2, 'def': 1}
    sorted_dict([]) == {}
    """
    # Your code here
    d = {}
    for i in data:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    



    


