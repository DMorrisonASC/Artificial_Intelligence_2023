from Queue import MyQueue
from Stack import Stack
from Heap import MinHeap
import random
import math
from Updated_Vacuum_Agent import Agent
random.seed(10)

class Graph:
    def __init__(self):
        # init dictionary
        self.graph = {}
        self.agent = Agent()

    def create_ran_graph(self):
        #y values
        adjMat = [[],[],[],[],[],[],[],[],[],[]]
        for y in range (10):
            for x in range (10):
            #x values
                newMat = []
                if x < 1:
                    if y < 1:
                        newMat.append((y*10) + (x + 1))
                        newMat.append(((y+1)*10) + x)
                        adjMat[y].append(newMat)
                    elif y > 8:
                        newMat.append(((y-1)*10) + x)
                        newMat.append((y*10) + (x + 1))
                        adjMat[y].append(newMat)
                    else:
                        newMat.append(((y-1)*10) + x)
                        newMat.append((y*10) + (x + 1))
                        newMat.append(((y+1)*10) + x)
                        adjMat[y].append(newMat)
                elif x > 8:
                    if y < 1:
                        newMat.append((y*10) + (x - 1))
                        newMat.append(((y+1)*10) + x)
                        adjMat[y].append(newMat)
                    elif y > 8:
                        newMat.append(((y-1)*10) + x)
                        newMat.append((y*10) + (x - 1))
                        adjMat[y].append(newMat)
                    else:
                        newMat.append(((y-1)*10) + x)
                        newMat.append((y*10) + (x - 1))
                        newMat.append(((y+1)*10) + x)
                        adjMat[y].append(newMat)
                else:
                    if y < 1:
                        newMat.append((y*10) + (x - 1))
                        newMat.append((y*10) + (x + 1))
                        newMat.append(((y+1)*10) + x)
                        adjMat[y].append(newMat)
                    elif y > 8:
                        newMat.append(((y-1)*10) + x)
                        newMat.append((y*10) + (x - 1))
                        newMat.append((y*10) + (x + 1))
                        adjMat[y].append(newMat)
                    else:
                        newMat.append(((y-1)*10) + x)
                        newMat.append((y*10) + (x - 1))
                        newMat.append((y*10) + (x + 1))
                        newMat.append(((y+1)*10) + x)
                        adjMat[y].append(newMat)
        index = 0
        for x in range (len(adjMat)):
            for currentRow in range (len(adjMat[x])):   
                for connection in adjMat[x][currentRow]:
                    randCost = random.randint(0, 20)
                    self.add_edge(index, connection, randCost)
                index += 1

    def get_graph_size(self):
        return len(self.graph)
    
    def add_edge(self, start, end, cost):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append([end, cost])

    def get_states(self):
        walls = []
        goal = 0
        index = 0
        for x in self.agent.playGround.envy:
            for y in x:
                if y == 1:
                    walls.append(index)
                elif y == 3:
                    goal = index
                index += 1
        return walls, goal

    def set_heuristic(self):

        states = self.get_states()
        heur = [[],[],[],[],[],[],[],[],[],[]]
        index = 0
        exit = states[1]
        for x in range (len(heur)):
            for y in range (10):
                value = math.sqrt((((exit//10) - y)**2)+(((exit % 10) - x)**2))
                heur[x].append(value)
                index += 1
        # print(heur)
        return heur

    def DFS(self, start):
        stack = Stack()
        # Add the start node and an empty path
        stack.push((start, []))
        # Set prevents duplicates
        visited = set()

        states = self.get_states()
        walls = states[0]
        exit = states[1]

        while not stack.is_empty():
            node, path = stack.pop()
            
            if node in visited or node in walls:
                continue
            
            visited.add(node)
            path = path + [node]
            
            if node == exit:
                # print(str(path))
                return path
            
            if node in self.graph:
                for neighbor in self.graph[node]:
                    # print("Node " + str(neighbor[0]))
                    if neighbor[0] not in visited:
                        stack.push((neighbor[0], path))
        return None

    def BFS(self, start):
        num = self.get_graph_size()
        queue = MyQueue(num) 
        # Enqueue the start node and an empty path
        queue.enque((start, [])) 
        visited = set()

        states = self.get_states()
        walls = states[0]
        exit = states[1]
        
        while not queue.is_empty():
            node, path = queue.deque()
            
            if node in visited or node in walls:
                continue
            
            visited.add(node)
            path = path + [node]
            
            if node == exit:
                return path
            
            if node in self.graph:
                for neighbor, _ in self.graph[node]:
                    if neighbor not in visited:
                        queue.enque((neighbor, path))
        return None

    def uniform_cost_search(self, start):
        visited = set()
        heap = MinHeap()
        heap.push((0, start, []))  # Push the start node, cost, and an empty path

        states = self.get_states()
        walls = states[0]
        exit = states[1]
        
        while heap.size() > 0:
            cost, node, path = heap.pop()
            
            if node in visited or node in walls:
                continue
            
            visited.add(node)
            path = path + [node]
            
            if node == exit:
                return path
            
            if node in self.graph:
                for neighbor, neighbor_cost in self.graph[node]:
                    if neighbor not in visited:
                        heap.push((cost + neighbor_cost, neighbor, path))
        
        return None
    
    def greedy_best_first_search(self, start):
        visited = set()
        queue = MinHeap() 
        heuristic = self.set_heuristic()
        queue.push((heuristic[start], start, []))  # Push the heuristic, start node, and an empty path

        states = self.get_states()
        walls = states[0]
        exit = states[1]
        
        while queue.size() > 0:
            _, node, path = queue.pop()
            
            if node in visited or node in walls:
                continue
            
            visited.add(node)
            path = path + [node]
            
            if node == exit:
                return path
            
            if node in self.graph:
                for neighbor, _ in self.graph[node]:
                    if neighbor not in visited:
                        queue.push((heuristic[neighbor//10][neighbor%10], neighbor, path))
        
        return None

    def a_star_search(self, start):
        visited = set()
        queue = MinHeap()
        heuristic = self.set_heuristic()
        # Push the f = g + h, g, start node, and an empty path
        queue.push((heuristic[start], 0, start, []))  

        states = self.get_states()
        walls = states[0]
        exit = states[1]
        
        while queue.size() > 0:
            _, g, node, path = queue.pop()
            
            if node in visited or node in walls:
                continue
            
            visited.add(node)
            path = path + [node]
            
            if node == exit:
                return path
            
            if node in self.graph:
                for neighbor, neighbor_cost in self.graph[node]:
                    if neighbor not in visited:
                        queue.push((g + neighbor_cost + heuristic[neighbor//10][neighbor%10], g + neighbor_cost, neighbor, path))
        return None

    def print_graph(self):
        # for node, neighbors in self.graph.items():
        #     # neighbor_str = ', '.join([f'{neighbor} ({cost})' for neighbor, cost in neighbors])
        #     # print(f'{node}: {neighbor_str}')
        #     print(str(node) + ": " + str(neighbors))
            for node, neighbors in self.graph.items():
                print(str(node) + ":")
                print(neighbors)


# Create a graph
g = Graph()

g.create_ran_graph()
start_node = 0

# g.print_graph()

# DFS
DFS_path = g.DFS(start_node)
print(DFS_path)
# print(f"DFS Path from {start_node} to {goal_node}: {' -> '.join(str(DFS_path))}")

# BFS
BFS_path = g.BFS(start_node)
print(BFS_path)
# if BFS_path:
#     print(f"BFS Path from {start_node} to {goal_node}: {' -> '.join(BFS_path)}")
# else:
#     print(f"No path found from {start_node} to {goal_node}")

# # Uniform Cost Search
ucs_path = g.uniform_cost_search(start_node)
print(ucs_path)
# if ucs_path:
#     print(f"Uniform Cost Search Path from {start_node} to {goal_node}: {' -> '.join(ucs_path)}")
# else:
#     print(f"No path found from {start_node} to {goal_node}")
g.set_heuristic()
# Greedy Best-First Search
gbfs_path = g.greedy_best_first_search(start_node)
print(gbfs_path)
# if gbfs_path:
#     print(f"Greedy Best-First Search Path from {start_node} to {goal_node}: {' -> '.join(gbfs_path)}")
# else:
#     print(f"No path found from {start_node} to {goal_node}")

# # A* Search with Heuristic
astar_path = g.a_star_search(start_node)
print(astar_path)
# if astar_path:
#     print(f"A* Search Path from {start_node} to {goal_node}: {' -> '.join(astar_path)}")
# else:
#     print(f"No path found from {start_node} to {goal_node}")
