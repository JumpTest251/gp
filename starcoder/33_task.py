def flatten_list(nested_list):
    """
    Write a function to flatten a given nested list structure.
    
    flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    """
    return [item for sublist in nested_list for item in sublist]
