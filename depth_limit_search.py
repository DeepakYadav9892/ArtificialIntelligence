class DepthLimitedSearch:
    def __init__(self, graph):
        self.graph = graph

    def dls(self, node, goal, limit, path=None):
        if path is None:
            path = [node]
        if node == goal:
            return path
        if limit <= 0:
            return None
        for neighbor in self.graph.get(node, []):
            if neighbor not in path:
                result = self.dls(neighbor, goal, limit - 1, path + [neighbor])
                if result:
                    return result
        return None




graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

dls_solver = DepthLimitedSearch(graph)
path = dls_solver.dls('A', 'G', limit=2)
print("Path Found:", path)
