# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: 
# Errors:

from AdjList import AdjList

if __name__ == "__main__":

    V = 5

    Adjacency_List = AdjList(V)
    Adjacency_List.insert(0, 1)
    Adjacency_List.insert(0, 2)
    Adjacency_List.insert(1, 0)    
    Adjacency_List.insert(1, 1)
    Adjacency_List.print_graph()