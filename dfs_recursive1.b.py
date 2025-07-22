graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]

    if start == goal:
        yield path

    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

print(list(dfs_paths(graph, 'C', 'F')))
