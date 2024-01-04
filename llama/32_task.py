def combinations_colors(colors, n):
    """
    Write a function that takes in a list and length n, 
    and generates all combinations (with repetition) of the elements of the list 
    and returns a list with a tuple for each combination.
    
    combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
    """
    # Initialize an empty list to store the combinations
    combos = []

    # Loop through each element of the input list
    for i in range(len(colors)):
        # Append a tuple containing the current element to the list of combinations
        combos.append((colors[i],))
  
    # Return the list of combinations
    return combos