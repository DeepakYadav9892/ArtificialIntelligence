from collections import deque

class BidirectionalSearch:
    def __init__(self, graph):
        self.graph = graph

    def neighbors(self, node):
        return self.graph.get(node, [])

    def build_path(self, parents_start, parents_goal, meeting_node):
        # from Start to meeting node  path
        path_start = []
        node = meeting_node
        while node is not None:
            path_start.append(node)
            node = parents_start.get(node)
        path_start.reverse()

        # From Goal  to meeting node  path (excluding meeting node)
        path_goal = []
        node = parents_goal.get(meeting_node)
        while node is not None:
            path_goal.append(node)
            node = parents_goal.get(node)

        # add path 
        return path_start + path_goal

    def search(self, start, goal):
        if start == goal:
            return [start]

        # Initialization
        frontier_start = deque([start])
        frontier_goal = deque([goal])

        visited_start = set([start])
        visited_goal = set([goal])

        parents_start = {start: None}
        parents_goal = {goal: None}

        while frontier_start and frontier_goal:
            # From Start side
            current_start = frontier_start.popleft()
            for neighbor in self.neighbors(current_start):
                if neighbor not in visited_start:
                    parents_start[neighbor] = current_start
                    visited_start.add(neighbor)
                    frontier_start.append(neighbor)

                if neighbor in visited_goal:
                    return self.build_path(parents_start, parents_goal, neighbor)

            # From Goal side
            current_goal = frontier_goal.popleft()
            for neighbor in self.neighbors(current_goal):
                if neighbor not in visited_goal:
                    parents_goal[neighbor] = current_goal
                    visited_goal.add(neighbor)
                    frontier_goal.append(neighbor)

                if neighbor in visited_start:
                    return self.build_path(parents_start, parents_goal, neighbor)

        return "No Path Found"





# Step 1: Graph define 
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E']
}

# Step 2:create  Class object
bds = BidirectionalSearch(graph)

# Step 3: Search function call 
start = 'A'
goal = 'F'

path = bds.search(start, goal)
print("Shortest Path:", path)
