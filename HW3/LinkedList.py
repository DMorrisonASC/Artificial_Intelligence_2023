# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: 
# Errors:

from Node import Node

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Adds a node at begin of the LinkedList

    def getHead(self):
        return self.head

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Adds a node at any index
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Update node of a linked list at specified index
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list
    def remove_begin(self):
        if(self.head == None):
            return

        self.head = self.head.next


    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_begin()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        while (current_node != None):

            if (current_node.data == data):
                self.remove_begin()
                return
            if (current_node.next != None):
                print("Node does not exist")
                return

            elif (current_node.next.data != data):
                current_node = current_node.next
            else:
                print(data, " was successfully removed")
                current_node.next = current_node.next.next
                return

        print("Node does not exist")

    # Print the size of linked list
    def sizeOfList(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printList(self):
        current_node = self.head
        while(current_node):
            print(" -> {}".format(current_node.data), end="")
            current_node =  current_node.next
