# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 9/26/2023
# Instructor: Professor Silveyra
# Description: Students will implement a simple adjacency list
# Errors:

# from Node import Node
# from Stack import Stack
# from Queue import MyQueue
# from LinkedList import LinkedList
# from Heap import MinHeap

class AdjList:
    def __init__(self):
        self.graph = {}

    def get_List_Size(self):
        return len(self.graph)

    # Add edges
    def insert(self, index, name):
        try:
            selectedLinkedList = self.graph[index] 
            selectedLinkedList.insertAtBegin(name)
        except KeyError:
            print("Not in graph!")

    # print a single  vertice
    def print_Vertice(self, index):
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

    bigGraph = AdjList()

    bigGraph.insert("start", "A")
