def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) traversal on a given graph starting from a specified node.
    Return A list containing the nodes visited in BFS order.
    Example:
        >>> graph = {
        ...     'A': ['B', 'C'],
        ...     'B': ['A', 'D', 'E'],
        ...     'C': ['A', 'F'],
        ...     'D': ['B'],
        ...     'E': ['B', 'F'],
        ...     'F': ['C', 'E']
        ... }
        >>> bfs(graph, 'A')
        ['A', 'B', 'C', 'D', 'E', 'F']
    """
    # TODO: Implement BFS
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
    