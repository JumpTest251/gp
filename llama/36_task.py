def sort_matrix(matrix):
    """
    Write a function to sort a given matrix in ascending order according to the sum of its rows.
    
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    """
    def sum_row(row):
        return sum(row)
    
    return sorted(matrix, key=sum_row)