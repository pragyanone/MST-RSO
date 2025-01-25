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
    [5, 101, 26111],
    [101, 13, 56],
    [101, 108, 17997],
    [108, 109, 237],
    [109, 15, 59],
    [109, 110, 10146],
    [110, 103, 5981],
    [103, 104, 5056],
    [104, 105, 79],
    [105, 106, 18],
    [106, 12, 13],
    [108, 114, 928],
    [114, 115, 2254],
    [115, 122, 6142],
    [122, 11, 205],
    [122, 123, 3033],
    [123, 124, 4626],
    [124, 116, 10803],
    [116, 117, 4836],
    [117, 3, 59],
    [117, 118, 1123],
    [118, 120, 10051],
    [120, 121, 1470],
    [121, 4, 1159],
    [123, 125, 7054],
    [125, 126, 302],
    [126, 2, 67],
    [126, 127, 9433],
    [127, 133, 5812],
    [133, 99, 108],
    [133, 132, 681],
    [132, 14, 18],
    [132, 131, 1627],
    [131, 130, 6757],
    [130, 129, 2650],
    [129, 128, 691],
    [128, 1, 3241],
    [130, 6, 6242]
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
with open('mstmatrix.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write headers
    writer.writerow([''] + nodes)
    
    # Write data
    for i, row in enumerate(matrix):
        writer.writerow([nodes[i]] + row)
        
print("CSV file 'mstmatrix.csv' has been created successfully!")
