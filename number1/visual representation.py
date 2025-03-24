import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix (Graph representation)
graph = [
    [0, 12, 10, 0, 0, 0, 12],  # City 1
    [12, 0, 8, 12, 0, 0, 0],   # City 2
    [10, 8, 0, 11, 3, 9, 0],   # City 3
    [0, 12, 11, 0, 11, 0, 10], # City 4
    [0, 0, 3, 11, 0, 6, 7],    # City 5
    [0, 0, 9, 0, 6, 0, 9],     # City 6
    [12, 0, 0, 10, 7, 9, 0]    # City 7
]

# Create a graph object
G = nx.Graph()

# Add edges to the graph
num_cities = len(graph)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        if graph[i][j] != 0:  # Only add edges with distances > 0
            G.add_edge(i + 1, j + 1, weight=graph[i][j])  # Cities are 1-indexed

# Draw the graph
pos = nx.spring_layout(G)  # Layout for visualization
plt.figure(figsize=(8, 6))

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1000, font_size=12, font_weight="bold", edge_color="gray")
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10, font_color="red")

# Show the plot
plt.title("Graph Representation of the TSP Problem")
plt.show()
