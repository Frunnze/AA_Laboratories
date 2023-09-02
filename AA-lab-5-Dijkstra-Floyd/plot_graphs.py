import networkx as nx
import matplotlib.pyplot as plt

n = 50

# Create a new empty graph
G = nx.Graph()

# Add the nodes to the graph
for i in range(n):
    G.add_node(i)

# Add the edges to the graph based on the adjacency matrix
for i in range(n):
    for j in range(i + 1, n):
        if adj_matrix[i][j] > 0:
            G.add_edge(i, j, weight=adj_matrix[i][j])

# Set up the layout of the graph
pos = nx.spring_layout(G)

# Draw the nodes of the graph
nx.draw_networkx_nodes(G, pos)

# Draw the edges of the graph
nx.draw_networkx_edges(G, pos)

# Draw the edge weights of the graph
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=6)

# Display the graph
plt.axis('off')
plt.show()