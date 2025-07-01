import heapq  # For Priority Queue 

class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph

    def ucs(self, start, goal):
        # Priority Queue: (cost, path, current_node)
        queue = [(0, [start], start)]  # start with cost 0

        visited = set()

        while queue:
            cost, path, node = heapq.heappop(queue)

            if node in visited:
                continue
            visited.add(node)

            # Goal found 
            if node == goal:
                return path, cost

            # check Neighbours
            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, path + [neighbor], neighbor))

        return "No path found", float('inf')




graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}




ucs_solver = UniformCostSearch(graph)

start = 'A'
goal = 'D'

path, cost = ucs_solver.ucs(start, goal)

print("Shortest Path:", path)
print("Total Cost:", cost)
