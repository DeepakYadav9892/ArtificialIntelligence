 #############Pseudo Code of A* Algorithm  ###################################


function A_Star(start, goal):
    open_set = PriorityQueue()
    open_set.put(start, f(start))  // f = g + h

    came_from = empty map
    g_score[start] = 0
    f_score[start] = h(start)

    while open_set is not empty:
        current = node in open_set with lowest f_score

        if current == goal:
            return reconstruct_path(came_from, current)

        remove current from open_set

        for each neighbor of current:
            tentative_g = g_score[current] + distance(current, neighbor)
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = g_score[neighbor] + h(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)
    return FAILURE


####################### program ###################

import heapq

def a_star(graph, start, goal, h):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = h[start]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

# Sample graph (adjacency list)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

# Heuristic values (estimated cost to goal)
h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

start = 'A'
goal = 'E'

path = a_star(graph, start, goal, h)
print("Path Found:", path)
