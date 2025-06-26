def dfs_non_recursive(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)






################## Code explanation ###################################################################################
###############################################################################################################

"""
Explanation (Line by Line):
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

If neighbor isn’t visited, push onto the stack."""
