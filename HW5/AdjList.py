# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 10/22/2023
# Instructor: Professor Silveyra
# Description: Implement the Graph coloring search. The program should 
# receive an adjacency matrix as input and return a 
# solution or determine that no solutions are found. You are required to implement three out of the four improvements presented in class.
# Errors:
import random
import copy

class GraphColoring:
    def __init__(self, adjacency_matrix, colors):
        self.adjacency_matrix = adjacency_matrix
        self.colors = colors
        self.solutions = []
        self.solution = [-1] * len(adjacency_matrix)
        # recursive calls counters
        self.recur_count = 0
        self.recur_count_CD = 0
        self.recur_count_BC = 0
        self.recur_count_None = 0

    # Check if it's safe to assign a certain color to a node without the constraints.
    def is_safe(self, vertex, color):
        # Loop through list and check if the current node is adjacent other nodes + has the same color.  Return `false` if placing adjacent nodes share the same color
        for i in range(len(self.adjacency_matrix)):
            if self.adjacency_matrix[vertex][i] == 1 and self.solution[i] == color:
                return False
        return True

    # Find the uncolored node with the most adjacent neighbors and return its index
    def most_constraining_variable(self):
        max_constrained = -1
        selected = -1
        for i in range(len(self.solution)):
            if self.solution[i] == -1:
                # Find sum of constraints. Since `0` = no connections and `1` = a connection
                num_constraints = sum(self.adjacency_matrix[i])
                if num_constraints > max_constrained:
                    max_constrained = num_constraints
                    selected = i
        return selected

    def forward_check(self, vertex, color):
        remaining_colors = copy.deepcopy(self.colors)
        for i in range(len(self.adjacency_matrix)):
            # Check if adj nodes are uncolored
            if self.adjacency_matrix[vertex][i] == 1 and self.solution[i] == -1:
                if color in remaining_colors:
                    remaining_colors.remove(color)
        return remaining_colors

    def least_constraining_value(self, vertex):
        color_count = {color: 0 for color in self.colors}
        for color in self.colors:
            for i in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[vertex][i] == 1 and self.solution[i] == -1:
                    if color in self.forward_check(i, color):
                        color_count[color] += 1
        # Get a list sorted by the least count/number in each key
        sorted_colors = sorted(self.colors, key=lambda x: color_count[x])
        return sorted_colors

    def solve(self):
        self.backtrack()
        self.backtrack_CD()
        self.backtrack_BC()
        self.backtrack_None()
        return self.solutions

    #   If all vertices have been colored(there are no `-1` values left), append the current solution and brake out of the method
    def backtrack(self):
        if all(color != -1 for color in self.solution):
            self.solutions.append(self.solution.copy())
            return

        vertex = self.most_constraining_variable()
        if vertex == -1:
            return # Backtrack is broken if list broken

        for color in self.least_constraining_value(vertex):
            if self.is_safe(vertex, color):
                self.solution[vertex] = color
                self.recur_count += 1
                self.backtrack()
                self.solution[vertex] = -1  # Backtrack when constraint is broken

    # Without `least_constraining_value()`
    def backtrack_BC(self):
        if all(color != -1 for color in self.solution):
            self.solutions.append(self.solution.copy())
            return

        vertex = self.most_constraining_variable()
        if vertex == -1:
            return # Backtrack is broken if list broken

        for color in self.colors:
            if self.is_safe(vertex, color):
                self.solution[vertex] = color
                self.recur_count_BC += 1
                self.backtrack_BC()
                self.solution[vertex] = -1  # Backtrack when constraint is broken


    # Without `most_constraining_variable()`
    def backtrack_CD(self):
        if all(color != -1 for color in self.solution):
            self.solutions.append(self.solution.copy())
            return

        vertex = 0
        for x in range(len(self.solution)):
            if self.solution[x] == -1:
                vertex = x
                break

        if vertex == -1:
            return # Backtrack is broken if list broken

        for color in self.least_constraining_value(vertex):
            if self.is_safe(vertex, color):
                self.solution[vertex] = color
                self.recur_count_CD += 1
                self.backtrack_CD()
                self.solution[vertex] = -1  # Backtrack when constraint is broken

    # No improvements
    def backtrack_None(self):
        if all(color != -1 for color in self.solution):
            self.solutions.append(self.solution.copy())
            return

        vertex = 0
        for x in range(len(self.solution)):
            if self.solution[x] == -1:
                vertex = x
                break

        if vertex == -1:
            return # Backtrack is broken if list broken
        for color in self.colors:
            if self.is_safe(vertex, color):
                self.solution[vertex] = color
                self.recur_count_None += 1
                self.backtrack_None()
                self.solution[vertex] = -1  # Backtrack when constraint is broken

    def print_graph(self):
        for x in range(len(self.adjacency_matrix)):
            print("Node " + str(x) + ":", end="")
            for y in range(len(self.adjacency_matrix[x])):
                if (self.adjacency_matrix[x][y] == 1) :
                    print(" -> " + str(y), end="")
            print()


# # australian coloring coloring graph given in class:
# adjacency_matrix = [
#     [0, 1, 1, 0, 0, 0],
#     [1, 0, 1, 1, 0, 0],
#     [1, 1, 1, 1, 1, 1],
#     [0, 1, 1, 0, 1, 0],
#     [0, 0, 1, 1, 0, 1],
#     [0, 0, 1, 0, 1, 0]
# ]

# colors = ["red", "green", "blue"]

# solver = GraphColoring(adjacency_matrix, colors)
# solutions = solver.solve()

# if solutions:
#     for i, solution in enumerate(solutions):
#         print(f"Solution {i + 1}: {solution}")
# else:
#     print("No solution found.")

# print(solver.recur_count, solver.recur_count_BC, solver.recur_count_CD, solver.recur_count_None)
