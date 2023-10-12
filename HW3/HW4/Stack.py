# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 9/27
# Instructor: Professor Silveyra
# Description: 
# Errors:

class Stack:
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        element = self.list.pop()
        return element

    def top(self):
        element =  self.list[-1]
        return element
    
    def is_empty(self):
        return len(self.list) == 0
