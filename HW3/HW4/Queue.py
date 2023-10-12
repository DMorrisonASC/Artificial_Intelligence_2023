# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: 
# Errors:
from collections import deque

class MyQueue:
    def __init__(self, size):
        self.size = size
        self.queueList = deque([], maxlen=self.size)

    def deque(self):
        return self.queueList.popleft()
    
    def enque(self, value):
        self.queueList.append(value)

    def size(self):
        return self.size

    # Return `True` when list is empty
    def is_empty(self):
        if bool(self.queueList) == False:
            return True
        else:
            return False



