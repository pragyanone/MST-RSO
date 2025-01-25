"""
Assignment 2
JKS, Operational Research in Transportation Engineering
Pragyan Shrestha, 079MSTrE014
==========================================================

Question:
Develop a subroutine for the following problems:
1. Short path between two nodes in a road network 
2. Minimum Spanning Tree (MST) of a road network
==========================================================

2. Answer
Minimum Spanning Tree (MST) for a road network using Prism's Algorithm in Python.

Given a road network matrix with
        nodes (places) as the ROW, COLUMN HEADERS
                        and
        road link (road) lengths as CELL VALUES,
this code gives the MST of the network.
Note: The first node is 0, not 1.
"""

# Input data
network = [
    [0, 26426, 38534, 52278, 83927, 12824, 30700, 61349, 57872, 13056, 40115, 13827],
    [26426, 0, 27747, 41491, 63888, 30619, 10661, 41310, 37833, 16011, 20076, 15420],
    [38534, 27747, 0, 13862, 67772, 40122, 23562, 36089, 41717, 25514, 23960, 24923],
    [52278, 41491, 13862, 0, 81516, 53866, 37306, 38024, 55461, 39258, 37704, 38667],
    [83927, 63888, 67772, 81516, 0, 85515, 53637, 51419, 26167, 70907, 44404, 70316],
    [12824, 30619, 40122, 53866, 85515, 0, 32288, 62937, 59460, 14644, 41703, 15415],
    [30700, 10661, 23562, 37306, 53637, 32288, 0, 31059, 27582, 17680, 9825, 17089],
    [61349, 41310, 36089, 38024, 51419, 62937, 31059, 0, 25252, 48329, 21352, 47738],
    [57872, 37833, 41717, 55461, 26167, 59460, 27582, 25252, 0, 44852, 18349, 44261],
    [13056, 16011, 25514, 39258, 70907, 14644, 17680, 48329, 44852, 0, 27095, 807],
    [40115, 20076, 23960, 37704, 44404, 41703, 9825, 21352, 18349, 27095, 0, 26504],
    [13827, 15420, 24923, 38667, 70316, 15415, 17089, 47738, 44261, 807, 26504, 0]
]

# Program
# Initialization
MST = set()
MST_lengths = set()
nodes = {}
num_vertices = len(network)

visited = {0}  # Start from the first vertex
while len(visited) < num_vertices:
    min_edge = None
    min_length = float("inf")

    for u in visited:
        for v in range(num_vertices):
            if v not in visited and network[u][v] < min_length and network[u][v] != 0:
                min_edge = (u, v)
                min_length = network[u][v]

    if min_edge:
        MST.add((min_edge, min_length))
        MST_lengths.add(min_length)
        visited.add(min_edge[1])
        print(f'\t\t{min_edge} = {min_length}')
        print(f'\t\t\t\t{visited}')


# Print the solution
print("For the network matrix:")
for row in network:
    print(row)
print("\n")
print("The MST as ((A, B), length) is:")
for item in MST:   
    print(item)
print("Total length of MST =", sum(MST_lengths))


"""
Sample output:

For the network matrix:
[0, 100, 85, 80, 90, 85]
[100, 0, 40, 150, 0, 0]
[85, 40, 0, 0, 0, 65]
[85, 150, 0, 0, 75, 0]
[80, 0, 0, 75, 0, 50]
[90, 0, 65, 0, 50, 0]


The MST as ((A, B), length) is:
{((3, 4), 75), ((2, 1), 40), ((0, 3), 80), ((5, 2), 65), ((4, 5), 50)}
Total length of MST = 310
"""
