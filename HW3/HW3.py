# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 9/26/2023
# Instructor: Professor Silveyra
# Description: Students will implement a simple adjacency list
# Errors: 1) Can NOT execute `DFS()` and `BFS()` are the same time 

from Node import Node
from Stack import Stack
from Queue import MyQueue
from LinkedList import LinkedList
# from Stack import DFS

class AdjList:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

        for x in range(self.V):
            self.graph[x] = LinkedList()

    # Add edges
    def insert(self, index, d):
        selectedLinkedList = self.graph[index]
        selectedLinkedList.insertAtBegin(d)


    # print a single  vertice
    def print_Vertice(self, index):
        # print("Enter vertice to show vertices connceted to it:")
        # verticeNum = int(input())

        # if (verticeNum <= len(self.graph) - 1):
        #     vertice = self.graph[verticeNum]
        #     print("Vertex " + str(verticeNum) + ":", end="")
        #     while vertice:
        #         print(" -> {}".format(vertice.data), end="")
        #         vertice =  vertice.next
        # else:
        #     print("Vertice does not exist!")
        selectedLinkedList = self.graph[index]
        print("Vertex " + str(index) + ":", end="")
        selectedLinkedList.printList()


    # Print the graph
    def print_graph(self):
        for index in range(self.V):
            selectedLinkedList = self.graph[index]
            print("Vertex " + str(index) + ":", end="")
            selectedLinkedList.printList()
            print()

    def DFS(self, startP):
        stack = Stack()
        stack.push(startP)
        visited = []

        while stack.is_empty() == False:
            eachV = stack.pop()
    
            if eachV not in visited:
                visited.append(eachV)
                current_node = self.graph[eachV].getHead()

                while current_node:
                    if current_node != None:
                        stack.push(current_node.data)
                        current_node = current_node.next

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
                current_node = self.graph[eachV].getHead()
                while current_node:
                    queue.enque(current_node.data)
                    current_node = current_node.next

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
    Adjacency_List.insert(1, 1)
    Adjacency_List.print_graph()
    # Adjacency_List.print_Vertice(0)

    DFS_results = Adjacency_List.DFS(0)
    BFS_results = Adjacency_List.BFS(0)
