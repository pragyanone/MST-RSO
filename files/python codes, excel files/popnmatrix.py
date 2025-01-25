import csv

# Define the node values
nodes = list(range(1, 7)) + list(range(11, 16)) + [99] + list(range(101, 134))

# Define infinity as a large number
infinity = float('inf')

# Define the number of nodes
num_nodes = len(nodes)

# Initialize the matrix with infinity
matrix = [[0] * num_nodes for _ in range(num_nodes)]

# Given table data
data = [
    [5, 101, 17955],
    [101, 13, 31034],
    [101, 108, 48989],
    [108, 109, 50488],
    [109, 15, 73457],
    [109, 110, 22969],
    [110, 103, 22969],
    [103, 104, 22969],
    [104, 105, 22969],
    [105, 106, 22969],
    [106, 12, 22969],
    [108, 114, 122446],
    [114, 115, 122446],
    [115, 122, 122446],
    [122, 11, 22645],
    [122, 123, 145091],
    [123, 124, 159136],
    [124, 116, 27192],
    [116, 117, 27192],
    [117, 3, 14001],
    [117, 118, 13191],
    [118, 120, 13191],
    [120, 121, 13191],
    [121, 4, 13191],
    [123, 125, 172283],
    [125, 126, 172283],
    [126, 2, 14045],
    [126, 127, 186328],
    [127, 133, 186328],
    [133, 99, 252064],
    [133, 132, 65736],
    [132, 14, 41743],
    [132, 131, 23993],
    [131, 130, 23993],
    [130, 129, 13094],
    [129, 128, 13094],
    [128, 1, 13094],
    [130, 6, 10899]
]

# Fill in the matrix with given data and mirror distances
for row in data:
    a, b, distance = row
    a_index = nodes.index(a)
    b_index = nodes.index(b)
    matrix[a_index][b_index] = distance
    # Mirror the distance for B to A
    matrix[b_index][a_index] = distance

# Write matrix to CSV file
with open('popnmatrix.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write headers
    writer.writerow([''] + nodes)
    
    # Write data
    for i, row in enumerate(matrix):
        writer.writerow([nodes[i]] + row)
        
print("CSV file 'popnmatrix.csv' has been created successfully!")
