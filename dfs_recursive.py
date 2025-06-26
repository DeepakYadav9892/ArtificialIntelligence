def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    print(node)
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)




graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}




######## Code explanation line by line ###########################################################################


🔹 Explanation (Line by Line):
def dfs_non_recursive(graph, start):

Define DFS function starting from a given node.

visited = set()

To keep track of already visited nodes.

stack = [start]

Initialize the stack with the starting node.

while stack:

Run until the stack becomes empty (no more nodes to visit).

node = stack.pop()

Pop the top node from the stack (LIFO behavior).

if node not in visited:

If not already visited:

print(node)

Process the node.

visited.add(node)

Mark it as visited.

for neighbor in reversed(graph[node]):

Loop over neighbors in reverse order (so leftmost node gets processed first when popped).

This mimics the order of recursive DFS.

if neighbor not in visited: stack.append(neighbor)

If neighbor isn’t visited, push onto the stack.




