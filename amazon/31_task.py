def re_arrange_array(arr, n):
    """
    Write a function that takes in an array and an integer n, 
    and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, 
    and where the relative order among negative and positive elements is preserved.
    
    re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    """
    return [x for x in arr if x < 0] + [x for x in arr if x >= 0]