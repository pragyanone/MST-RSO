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

# Write matrix to CSV file, truncated at node 99
def write_matrix_truncated(file_path, nodes, matrix):
    # Find the index of node 99
    node_99_index = nodes.index(99)
    # Truncate nodes and matrix
    truncated_nodes = nodes[:node_99_index + 1]
    truncated_matrix = matrix[:node_99_index + 1, :node_99_index + 1]
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write headers
        writer.writerow([''] + [node for node in truncated_nodes])
        # Write data
        for i, row in enumerate(truncated_matrix):
            writer.writerow([truncated_nodes[i]] + list(row))

# Floyd-Warshall algorithm to find the shortest paths
def floyd_warshall(nodes, distances):
    num_nodes = len(nodes)
    # Initialize the shortest path matrix with the same distances
    shortest_paths = np.array(distances)
    # Update shortest paths using dynamic programming
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                shortest_paths[i][j] = min(shortest_paths[i][j], shortest_paths[i][k] + shortest_paths[k][j])
    # Set diagonal elements to 0
    np.fill_diagonal(shortest_paths, 0)
    return shortest_paths

# Read the matrix from CSV file
nodes, distances = read_matrix('matrix.csv')

# Find the shortest paths using Floyd-Warshall algorithm
shortest_paths = floyd_warshall(nodes, distances)

# Write the truncated shortest path matrix to a CSV file
write_matrix_truncated('shortdist.csv', nodes, shortest_paths)

print("Shortpath matrix has been written to 'shortdist.csv'")
