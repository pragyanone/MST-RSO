import csv

# Define the node values
nodes = list(range(1, 7)) + list(range(11, 16)) + [99] + list(range(101, 134))

# Define infinity as a large number
infinity = float('inf')

# Define the number of nodes
num_nodes = len(nodes)

# Initialize the matrix with infinity
matrix = [[infinity] * num_nodes for _ in range(num_nodes)]

# Given table data
data = [
    [5, 101, 26111],
    [101, 13, 56],
    [101, 108, 17997],
    [13, 102, 560],
    [102, 106, 28971],
    [102, 103, 19526],
    [108, 109, 237],
    [108, 114, 928],
    [106, 12, 13],
    [106, 105, 18],
    [103, 110, 5981],
    [103, 104, 5056],
    [109, 15, 59],
    [109, 110, 10146],
    [114, 115, 2254],
    [114, 111, 15668],
    [105, 107, 5466],
    [105, 104, 79],
    [110, 111, 4440],
    [104, 111, 7032],
    [115, 122, 6142],
    [115, 116, 15587],
    [107, 112, 12332],
    [107, 113, 20538],
    [122, 11, 205],
    [122, 123, 3033],
    [116, 124, 10803],
    [116, 117, 4836],
    [112, 113, 10293],
    [112, 119, 13193],
    [113, 121, 10830],
    [123, 124, 4626],
    [123, 125, 7054],
    [124, 127, 3305],
    [117, 3, 59],
    [117, 118, 1123],
    [119, 118, 3885],
    [119, 120, 8230],
    [121, 120, 1470],
    [121, 4, 1159],
    [125, 126, 302],
    [125, 128, 22816],
    [127, 126, 9433],
    [127, 133, 5812],
    [118, 120, 10051],
    [126, 2, 67],
    [128, 1, 3241],
    [128, 129, 691],
    [133, 99, 108],
    [133, 132, 681],
    [129, 131, 7479],
    [129, 130, 2650],
    [132, 14, 18],
    [132, 131, 1627],
    [131, 130, 6757],
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
with open('matrix.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write headers
    writer.writerow([''] + nodes)
    
    # Write data
    for i, row in enumerate(matrix):
        writer.writerow([nodes[i]] + row)
        
print("CSV file 'matrix.csv' has been created successfully!")
