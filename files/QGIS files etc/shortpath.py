import csv
import numpy as np


# Read the matrix from the CSV file
def read_matrix(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    # Extract node labels and distances
    nodes = [int(node) for node in data[0][1:]]
    distances = [
        [int(cell) if cell != "inf" else float("inf") for cell in row[1:]]
        for row in data[1:]
    ]
    return nodes, distances


# Write matrix to CSV file, truncated at node 99
def write_matrix_truncated(file_path, nodes, matrix):
    # Find the index of node 99
    node_99_index = nodes.index(7)
    # Truncate nodes and matrix
    truncated_nodes = nodes[: node_99_index + 1]
    truncated_matrix = matrix[: node_99_index + 1, : node_99_index + 1]
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write headers
        writer.writerow([""] + [node for node in truncated_nodes])
        # Write data
        for i, row in enumerate(truncated_matrix):
            writer.writerow([truncated_nodes[i]] + list(row))


# Floyd-Warshall algorithm to find the shortest paths and distances
def floyd_warshall(nodes, distances):
    num_nodes = len(nodes)
    # Initialize the shortest path matrix with the same distances
    shortest_paths = np.array(distances)
    # Initialize matrix to store the intermediate nodes
    intermediate_nodes = [
        [-1 if distance != float("inf") else -1 for distance in row]
        for row in distances
    ]
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
        return get_path(i, k, intermediate_nodes, nodes)[:-1] + get_path(
            k, j, intermediate_nodes, nodes
        )


# Read the matrix from CSV file
nodes, distances = read_matrix("matrix1_utp.csv")

# Find the shortest paths and intermediate nodes using Floyd-Warshall algorithm
shortest_paths, intermediate_nodes = floyd_warshall(nodes, distances)

# Write the truncated shortest path matrix to a CSV file
write_matrix_truncated("shortest_paths_utp.csv", nodes, shortest_paths)

print("Truncated shortest path matrix has been written to 'shortest_paths_utp.csv'")

# Create a matrix to store the paths followed for each pair of nodes
paths_matrix = [["" for _ in range(len(nodes))] for _ in range(len(nodes))]
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i != j and shortest_paths[i][j] != float("inf"):
            path = get_path(i, j, intermediate_nodes, nodes)
            distance = round(shortest_paths[i][j])
            paths_matrix[i][j] = " -> ".join(map(str, path)) + f" = {distance}"

# Truncate paths matrix after node 99
node_99_index = nodes.index(7)
paths_matrix = paths_matrix[: node_99_index + 1]
for i in range(node_99_index + 1):
    paths_matrix[i] = paths_matrix[i][: node_99_index + 1]

# Write the paths matrix to a CSV file
with open("paths_matrix_utp.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write headers
    writer.writerow([""] + [node for node in nodes[: node_99_index + 1]])
    # Write data
    for i, row in enumerate(paths_matrix):
        writer.writerow([nodes[i]] + row)

print("Paths matrix has been written to 'paths_matrix_utp.csv'")
