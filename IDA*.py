#####################Pseudo Code fo IDA* #################################



function IDA_Star(root, goal):
    threshold = f(root) = g(root) + h(root)  // usually g(root) = 0

    loop:
        temp = Search(root, 0, threshold)
        if temp == FOUND:
            return path to goal
        if temp == ∞:
            return FAILURE
        threshold = temp

function Search(node, g, threshold):
    f = g + h(node)
    if f > threshold:
        return f
    if node == goal:
        return FOUND

    min = ∞
    for each successor of node:
        temp = Search(successor, g + cost(node, successor), threshold)
        if temp == FOUND:
            return FOUND
        if temp < min:
            min = temp
    return min
 ###########################################Code section ####################################################################



# Python code for IDA* Search

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.h = heuristic  # heuristic value
        self.neighbors = []

    def add_neighbor(self, neighbor, cost):
        self.neighbors.append((neighbor, cost))

def ida_star(start, goal):
    def search(path, g, threshold):
        node = path[-1]
        f = g + node.h
        if f > threshold:
            return f
        if node.name == goal.name:
            return "FOUND"

        min_cost = float('inf')
        for neighbor, cost in node.neighbors:
            if neighbor not in path:  # avoid cycles
                path.append(neighbor)
                temp = search(path, g + cost, threshold)
                if temp == "FOUND":
                    return "FOUND"
                if temp < min_cost:
                    min_cost = temp
                path.pop()
        return min_cost

    threshold = start.h
    path = [start]
    while True:
        temp = search(path, 0, threshold)
        if temp == "FOUND":
            return [node.name for node in path]
        if temp == float('inf'):
            return None  # failure
        threshold = temp

# Sample Graph
A = Node("A", 7)
B = Node("B", 6)
C = Node("C", 2)
D = Node("D", 1)
E = Node("E", 0)

A.add_neighbor(B, 1)
A.add_neighbor(C, 4)
B.add_neighbor(D, 5)
C.add_neighbor(D, 1)
D.add_neighbor(E, 3)

result = ida_star(A, E)
print("Path Found:", result)

