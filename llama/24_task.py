def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    # Initialize variables
    n = len(grid)
    m = len(grid[0])
    visited = set()
    queue = []
    path = []
    min_path = []
    
    # Initialize the starting point of the path
    start_x, start_y = 0, 0
    grid[start_x][start_y] = -1
    visited.add((start_x, start_y))
    queue.append((start_x, start_y))
    
    # Iterate through the queue until the path is complete or the queue is empty
    while len(queue) > 0 and k > 0:
        # Dequeue a cell from the queue
        current_x, current_y = queue.pop(0)
        
        # Check if the current cell has already been visited
        if (current_x, current_y) not in visited:
            visited.add((current_x, current_y))
            
            # If the current cell is on the path, add it to the path list
            if grid[current_x][current_y] > 0:
                path.append(grid[current_x][current_y])
                
            # If the current cell has not been visited before, visit its neighbors and enqueue them
            for x in range(max(0, current_x - 1), min(n - 1, current_x + 1) + 1):
                for y in range(max(0, current_y - 1), min(m - 1, current_y + 1) + 1):
                    if (x, y) not in visited:
                        queue.append((x, y))
                        
            # If the path is complete, check if it's less than the minimum path
            if len(path) == k:
                if len(min_path) < k or path < min_path[1:k]:
                    min_path = path
            
            # Decrement the number of steps remaining
            k -= 1
    
    # Return the minimum path
    return min_path
