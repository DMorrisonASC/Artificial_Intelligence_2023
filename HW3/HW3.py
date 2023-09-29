# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 9/26/2023
# Instructor: Professor Silveyra
# Description: Students will implement a simple adjacency list
# Errors: 1) Can NOT execute `DFS()` and `BFS()` are the same time 

# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None
from Node import Node
from Stack import Stack
from Queue import MyQueue
# from Stack import DFS

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

        if (verticeNum <= len(self.graph) - 1):
            vertice = self.graph[verticeNum]
            print("Vertex " + str(verticeNum) + ":", end="")
            while vertice:
                print(" -> {}".format(vertice.data), end="")
                vertice =  vertice.next
        else:
            print("Vertice does not exist!")

    # Print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")

    def DFS(self, startP):
        stack = Stack()
        stack.push(startP)
        visited = []

        while stack.is_empty() == False:
            eachV = stack.pop()
    
            if eachV not in visited:
                visited.append(eachV)

                while self.graph[eachV]:
                    stack.push(self.graph[eachV].data)
                    self.graph[eachV] = self.graph[eachV].next

        print("Path: ",end="")
        for i in visited:
            print(i, end=" -> ")

    def BFS(self, startP):
        queue = MyQueue(self.V)
        queue.enque(startP)
        visited = []

        while queue.is_empty() == False:
            eachV = queue.deque()

            if eachV not in visited:
                visited.append(eachV)

                while self.graph[eachV]:
                    queue.enque(self.graph[eachV].data)
                    self.graph[eachV] = self.graph[eachV].next

        print("Path: ",end="")
        for i in visited:
            print(i, end=" -> ")

    
        

if __name__ == "__main__":
    V = 5

    # Create graph and edges
    Adjacency_List = AdjList(V)
    Adjacency_List.insert(0, 1)
    Adjacency_List.insert(0, 2)
    Adjacency_List.insert(0, 3)    
    Adjacency_List.insert(1, 2)
    Adjacency_List.print_graph()
    # graph.print_Vertice()

    DFS_results = Adjacency_List.DFS(3)
    BFS_results = Adjacency_List.BFS(3)
