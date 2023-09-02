import time
import matplotlib.pyplot as plt
import pandas as pd
import math

# Implement a depth first search algorithm with a start and a stop.
def dfs(graph, start, stop):
    # Define and initialize the visited list and the stack.
    visited = []
    stack = [start]

    # Check if the stack is not empty.
    while stack:

        # Delete and assigne the top element of the stack. 
        node = stack.pop()

        # Check if the current node is the one you are looking for.
        if node == stop:
            visited.append(node)
            return visited
        
        # Check if the current node was visited before.
        if node not in visited:
            # Add the node to the visited list if it is not there.
            visited.append(node)

            # Get the neighbors of the current node and add them to the stack.
            neighbours = graph[node]
            for neighbor in neighbours:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

# Implement the breadth first search algorithm.
def bfs(graph, start, stop):
    # Define and initialize the visited list and the queue.
    visited = []
    queue = [start]

    # Check if the queue is not empty.
    while queue:
        # Delete and assigne the first element of the queue.
        node = queue.pop(0)

        # Check if the current node was visited before.
        if node not in visited:

            # Add the node to the visited list, if it is not there.
            visited.append(node)

            # Check if the current node is the one you are looking for.
            if node == stop:
                break

            # Get the neighbors of the current node and add them to the queue.
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited


balanced_dict = {25: [30, 42], 30: [10, 6, 25], 10: [9, 27, 30], 9: [37, 29, 10], 37: [48, 7, 9], 48: [37], 7: [37], 29: [20, 9], 20: [29], 27: [23, 36, 10], 23: [24, 27], 24: [23], 36: [8, 27], 8: [36], 6: [14, 43, 30], 14: [15, 22, 6], 15: [17, 38, 14], 17: [15], 38: [15], 22: [21, 14], 21: [22], 43: [31, 4, 6], 31: [3, 43], 3: [31], 4: [26, 43], 26: [4], 42: [41, 46, 25], 41: [45, 39, 42], 45: [18, 47, 41], 18: [32, 16, 45], 32: [18], 16: [18], 47: [13, 45], 13: [47], 39: [2, 1, 41], 2: [12, 39], 12: [2], 1: [44, 39], 44: [1], 46: [28, 33, 42], 28: [40, 35, 46], 40: [11, 28], 11: [40], 35: [34, 28], 34: [35], 33: [19, 50, 46], 19: [49, 33], 49: [19], 50: [5, 33], 5: [50]}
unbalanced_dict = {25: [30, 42, 45, 43], 30: [10, 6, 25], 10: [9, 27, 15, 30], 9: [37, 29, 10], 37: [9], 48: [20], 7: [20], 29: [20, 9], 20: [48, 7, 29], 27: [23, 36, 10], 23: [24, 27], 24: [23], 36: [8, 27], 8: [36], 6: [14, 43, 30], 14: [15, 22, 6], 15: [10, 14], 17: [21], 38: [21], 22: [21, 14], 21: [17, 38, 22], 43: [31, 4, 25, 6], 31: [3, 43], 3: [31], 4: [26, 43, 18], 26: [4], 42: [41, 46, 25], 41: [45, 39, 42], 45: [18, 47, 25, 41], 18: [32, 16, 4, 45], 32: [18], 16: [18], 47: [13, 45], 13: [47], 39: [2, 1, 41], 2: [12, 39], 12: [2], 1: [44, 39, 46], 44: [1], 46: [28, 33, 1, 42], 28: [40, 35, 46], 40: [11, 28], 11: [40], 35: [34, 28], 34: [35], 33: [19, 50, 46], 19: [49, 33], 49: [19], 50: [5, 33], 5: [50]}

dfs_balanced_time = [0]
for node in range(1, 51):
    start = time.time()
    dfs(balanced_dict, 25, node)
    end = time.time()
    ms = (end - start) * 1000
    dfs_balanced_time.append(dfs_balanced_time[node - 1] + round(ms, 3))

dfs_unbalanced_time = [0]
for node in range(1, 51):
    start = time.time()
    dfs(unbalanced_dict, 25, node)
    end = time.time()
    ms = (end - start) * 1000
    dfs_unbalanced_time.append(dfs_unbalanced_time[node - 1] + round(ms, 3))

bfs_balanced_time = [0]
for node in range(1, 51):
    start = time.time()
    bfs(balanced_dict, 25, node)
    end = time.time()
    ms = (end - start) * 1000
    bfs_balanced_time.append(bfs_balanced_time[node - 1] + round(ms, 3))

bfs_unbalanced_time = [0]
for node in range(1, 51):
    start = time.time()
    bfs(unbalanced_dict, 25, node)
    end = time.time()
    ms = (end - start) * 1000
    bfs_unbalanced_time.append(bfs_unbalanced_time[node - 1] + round(ms, 3))

x = [i for i in range(0, 51)]
plt.plot(x, dfs_balanced_time, label = 'Balanced DFS')
plt.plot(x, dfs_unbalanced_time, label = 'Unbalanced DFS')
plt.plot(x, bfs_balanced_time, label = 'Balanced BFS')
plt.plot(x, bfs_unbalanced_time, label = 'Unbalanced BFS')
plt.xlabel('First n nodes')
plt.ylabel('Time (ms)')
plt.legend(loc = 'upper left')
plt.show()