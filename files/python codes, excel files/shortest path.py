import csv
import numpy as np

# Read the matrix from the CSV file
def read_matrix(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    # Extract node labels and distances
    nodes = [int(node) for node in data[0][1:]]
    distances = [[int(cell) if cell != 'inf' else float('inf') for cell in row[1:]] for row in data[1:]]
    return nodes, distances

# Floyd-Warshall algorithm to find the shortest paths
def floyd_warshall(nodes, distances):
    num_nodes = len(nodes)
    # Initialize the shortest path matrix with the same distances
    shortest_paths = np.array(distances)
    # Initialize matrix to store the intermediate nodes
    intermediate_nodes = [[-1 if distance != float('inf') else -1 for distance in row] for row in distances]
    # Update shortest paths and intermediate nodes using dynamic programming
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if shortest_paths[i][j] > shortest_paths[i][k] + shortest_paths[k][j]:
                    shortest_paths[i][j] = shortest_paths[i][k] + shortest_paths[k][j]
                    intermediate_nodes[i][j] = k
    return shortest_paths, intermediate_nodes

# Get the path from node i to node j using intermediate nodes
def get_path(i, j, intermediate_nodes, nodes):
    if intermediate_nodes[i][j] == -1:
        return [nodes[i], nodes[j]]
    else:
        k = intermediate_nodes[i][j]
        return get_path(i, k, intermediate_nodes, nodes)[:-1] + get_path(k, j, intermediate_nodes, nodes)

# Read the matrix from CSV file
nodes, distances = read_matrix('matrix.csv')

# Find the shortest paths and intermediate nodes using Floyd-Warshall algorithm
shortest_paths, intermediate_nodes = floyd_warshall(nodes, distances)

# Create a matrix to store the paths followed for each pair of nodes
paths_matrix = [['' for _ in range(len(nodes))] for _ in range(len(nodes))]
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i != j and shortest_paths[i][j] != float('inf'):
            path = get_path(i, j, intermediate_nodes, nodes)
            distance = round(shortest_paths[i][j])
            paths_matrix[i][j] = ' -> '.join(map(str, path)) + f' = {distance}'

# Truncate paths matrix after node 99
node_99_index = nodes.index(99)
paths_matrix = paths_matrix[:node_99_index + 1]
for i in range(node_99_index + 1):
    paths_matrix[i] = paths_matrix[i][:node_99_index + 1]

# Write the paths matrix to a CSV file
with open('shortpath.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write headers
    writer.writerow([''] + [node for node in nodes[:node_99_index + 1]])
    # Write data
    for i, row in enumerate(paths_matrix):
        writer.writerow([nodes[i]] + row)

print("Short path matrix has been written to 'shortpath.csv'")
