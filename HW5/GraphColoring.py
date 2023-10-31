# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 10/22/2023
# Instructor: Professor Silveyra
# Description: Tester file
# Errors:

from AdjList import GraphColoring
import random

avg_recur_count = 0
avg_recur_count_BC = 0
avg_recur_count_CD = 0
avg_recur_count_None = 0
testRuns = 100

def randomAdjList():
    n = 6

    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Creates a adjacency matrix with a 60% chance of placing a 1
    for i in range(n):
        for j in range(i+1, n):
            if random.random() <= 0.60:
                adjacency_matrix[i][j] = 1
                adjacency_matrix[j][i] = 1
    return adjacency_matrix

for x in range(testRuns):
    # A 6x6 adjacency matrix with a 60% chance of placing a 1(adding a connection)
    adjacency_matrix = randomAdjList()
    colors = ["red", "green", "blue"]

    solver = GraphColoring(adjacency_matrix, colors)
    solutions = solver.solve()
    avg_recur_count += solver.recur_count
    avg_recur_count_BC += solver.recur_count_BC
    avg_recur_count_CD += solver.recur_count_CD
    avg_recur_count_None += solver.recur_count_None

# print the connections for the last random graph
solver.print_graph()
# print the solutions for the last random graph
if solutions:
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}: {solution}")
else:
    print("No solution found.")
# print the average recursion counters
print("Avg recursions for all improvements: " + str(avg_recur_count / testRuns))
print("Avg recursions without `least_constraining_value(): " + str(avg_recur_count_BC / testRuns))
print("Avg recursions without `most_constraining_variable()`: " + str(avg_recur_count_CD / testRuns))
print("Avg recursions for no improvements: " + str(avg_recur_count_None / testRuns))
