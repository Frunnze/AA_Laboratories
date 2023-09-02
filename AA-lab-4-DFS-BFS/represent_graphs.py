import random
import graphviz as gv

# Create a balanced graph (tree).
def build_balanced(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = {'data': arr[mid], 'neighbor': []}
    root['neighbor'].append(build_balanced(arr[:mid]))
    root['neighbor'].append(build_balanced(arr[mid+1:]))
    return root

# Get the neighbors and create the adjacency list.
def get_neighbors(node, neighbors_dict=None):
    if neighbors_dict is None:
        neighbors_dict = {}
    if node is None:
        return neighbors_dict
    data = node['data']
    neighbors = []
    for neighbor in node['neighbor']:
        if neighbor is not None:
            neighbors.append(neighbor['data'])
    neighbors_dict[data] = neighbors
    for neighbor in node['neighbor']:
        get_neighbors(neighbor, neighbors_dict)
    return neighbors_dict

def adjacency_list(dictB):
    for node in dictB:
        for neighbor in dictB[node]:
            if node not in dictB[neighbor]:
                dictB[neighbor].append(node)
    return dictB

# Draw the graph.
def create_tree_graph(neighbors_dict):
    dot = gv.Digraph()
    for node, neighbors in neighbors_dict.items():
        dot.node(str(node))
        for neighbor in neighbors:
            dot.edge(str(node), str(neighbor), arrowhead='none')
    return dot

arr = random.sample(range(1, 51), 50)
root = build_balanced(arr)
neighbors_dict = get_neighbors(root)
graph = create_tree_graph(neighbors_dict)
graph.render('graph', view=True)
neighbors_dict = adjacency_list(neighbors_dict)
print(adjacency_list(neighbors_dict))


