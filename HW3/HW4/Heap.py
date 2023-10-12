import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        heapq.heappush(self.heap, item)
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    def size(self):
        return len(self.heap)

# Example usage:
# min_heap = MinHeap()

# min_heap.push(5)
# min_heap.push(2)
# min_heap.push(9)
# min_heap.push(1)

# print("Min heap elements:")
# while min_heap.size() > 0:
#     print(min_heap.pop())
