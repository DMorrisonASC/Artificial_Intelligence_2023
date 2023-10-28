class GraphColoring:
    def __init__(self, adjacency_matrix, colors):
        self.adjacency_matrix = adjacency_matrix
        self.colors = colors
        self.solutions = []
        self.solution = [-1] * len(adjacency_matrix)

    def is_safe(self, vertex, color):
        for i in range(len(self.adjacency_matrix)):
            if self.adjacency_matrix[vertex][i] == 1 and self.solution[i] == color:
                return False
        return True

    def solve(self):
        pass

    def forward_Checking(self):
        pass

# Example usage:
adjacency_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0]
]
colors = ["red", "green", "blue"]

solver = GraphColoring(adjacency_matrix, colors)
# solutions = solver.solve()

if solutions:
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}: {solution}")
