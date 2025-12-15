# Aim: Depth first search to find path between two nodes.

# Program:

# The graph is represented using an adjacency list (a dictionary).
# Keys are nodes, and values are lists of neighbors.
adj_list = {
    "a": ["b"],
    "b": ["a", "c"],
    "c": ["b", "d"],
    "d": ["a", "e", "f"],
    "e": ["d", "g"],
    "f": ["d", "e", "h"],
    "g": ["e", "h"],
    "h": ["f", "g"]
}

# --- Initialization ---
# Dictionary to keep track of visited nodes
visited = {}
# Dictionary to store the parent of each node in the DFS tree
parent = {}
# List to store the DFS traversal order
dfs_output = []

# Initialize visited and parent for all nodes
for node in adj_list.keys():
    visited[node] = False
    parent[node] = None

# --- DFS Function Definition ---
def dfs(node):
    """Performs Depth First Search starting from 'node'."""
    visited[node] = True
    dfs_output.append(node)

    # Traverse neighbors
    for neighbour in adj_list[node]:
        # If the neighbor has not been visited, call DFS recursively
        if not visited[neighbour]:
            parent[neighbour] = node # Set the current node as the parent
            dfs(neighbour)

# --- Path Finding Logic ---

# Get source and destination nodes from the user
source = input("Enter source node: ").lower()
destination = input("Enter destination node: ").lower()

# Start DFS from the source node
if source in adj_list:
    dfs(source)
else:
    print(f"Error: Source node '{source}' not found in the graph.")

# Print the DFS traversal order
print("\nIn DFS traversal:", dfs_output)

# Check if the destination was reached (i.e., visited)
if visited.get(destination):
    print(f"\nPath found from {source} to {destination}:")
    
    # Reconstruct the path using the parent dictionary
    path = []
    current_node = destination
    
    # Traverse backwards from destination to source using parent pointers
    while current_node is not None:
        path.append(current_node)
        current_node = parent[current_node]
        
    # The path is currently destination -> ... -> source. Reverse it.
    path.reverse()
    
    # Print the final path
    print(" --> ".join(path))

else:
    # This includes the case where the destination is not in the graph or not reachable
    print(f"\nNo path found between the given nodes ({source} and {destination})")