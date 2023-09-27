# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 9/26/2023
# Instructor: Professor Silveyra
# Description: Students will implement a simple adjacency list
# Errors:

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class AdjList:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def insert(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = Node(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # print a single  vertice
    def print_Vertice(self):
        print("Enter vertice to show vertices connceted to it:")
        verticeNum = int(input())

        vertice = self.graph[verticeNum]
        print("Vertex " + str(verticeNum) + ":", end="")
        while vertice:
            print(" -> {}".format(vertice.data), end="")
            vertice =  vertice.next

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")

if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = AdjList(V)
    graph.insert(0, 1)
    graph.insert(0, 2)
    graph.insert(0, 3)
    graph.insert(1, 2)

    graph.print_agraph()
    graph.print_Vertice()


