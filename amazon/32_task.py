def combinations_colors(colors, n):
    """
    Write a function that takes in a list and length n, 
    and generates all combinations (with repetition) of the elements of the list 
    and returns a list with a tuple for each combination.
    
    combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
    """
    if n == 1:
        return [(color,) for color in colors]
    else:
        return [(color,) + combination for color in colors for combination in combinations_colors(colors, n-1)]
    