import random
import time
from queue import PriorityQueue
import matplotlib.pyplot as plt

class UnionFind:
    # Union-find data structure to efficiently detect cycles in the graph
    def __init__(self, n):
        self.parent = list(range(n)) # parent of each node
        self.rank = [0] * n          # rank of each node (for union-by-rank)
    
    # Find the root of the given node using path compression
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    # Union the two given nodes using union-by-rank
    # Return True if they are in different sets and were united, False otherwise
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            return False
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        return True

def kruskal(n, edges):
    # Sort edges by weight in increasing order
    edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize a union-find data structure and MST variables
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []
    
    # Iterate over edges in increasing order of weight
    for u, v, w in edges:
        # If the two endpoints are in different sets, unite them and add the edge to the MST
        if uf.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))
    
    # Return the total weight of the MST and its edges
    return mst_weight, mst_edges


def prim(edges):
    # Create a dictionary to store the graph
    graph = {}
    for edge in edges:
        u, v, weight = edge
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = weight
        graph[v][u] = weight
    
    # Create a priority queue to store the vertices and their weights
    pq = PriorityQueue()
    start_vertex = list(graph.keys())[0]
    visited = {start_vertex}
    
    for neighbor, weight in graph[start_vertex].items():
        pq.put((weight, start_vertex, neighbor))
    
    # Iterate over the priority queue and add edges to the minimum spanning tree
    total_weight = 0
    mst_edges = []
    while not pq.empty():
        weight, u, v = pq.get()
        if v not in visited:
            visited.add(v)
            total_weight += weight
            mst_edges.append((u, v, weight))
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    pq.put((weight, v, neighbor))
    
    return mst_edges, total_weight


def add_edge(edges, n, max_weight):
    # Choose a random existing node and a new node
    existing_node = random.choice(range(n))
    new_node = n

    # Create a new edge between the existing node and the new node
    weight = random.randint(1, max_weight)
    edge = (existing_node, new_node, weight)

    # Append the new edge to the list of edges and increment the number of nodes
    edges.append(edge)
    n += 1

    return edges, n

def add_mult_edges(edges, n, max_weight):
    for i in range(4):
        # Choose a random existing node and a new node
        existing_node = random.choice(range(n))
        new_node = n

        # Create a new edge between the existing node and the new node
        weight = random.randint(1, max_weight)
        edge = (existing_node, new_node, weight)

        # Append the new edge to the list of edges and increment the number of nodes
        edges.append(edge)

    n += 1
    return edges, n


n = 1
edges = []
kruskal_times = [0]
prim_times = [0]
for i in range(500):
    edges, n = add_mult_edges(edges, n, 10)

    start = time.time()
    mst_weight, mst_edges = kruskal(n, edges)
    end = time.time()
    ms = (end - start) * 1000
    kruskal_times.append(ms)

    start = time.time()
    mst, total_weight = prim(edges)
    end = time.time()
    ms = (end - start) * 1000 
    prim_times.append(ms)
                                              

# Plot the results.
x = [i for i in range(n)]
plt.plot(x, kruskal_times, label = "Kruskal's algorithm")
plt.plot(x, prim_times, label = "Prim's algorithm")
plt.xlabel('Nodes')
plt.ylabel('Time (ms)')
plt.legend(loc = 'upper left')
plt.title('Dense graph')
plt.show()
