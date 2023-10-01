# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: 
# Errors:

from AdjList import AdjList

def load_file():
    file_path = input("Enter file path: ")
    f =  open(file_path, 'r')
    size = int(f.readline())
    adjL = AdjList(size)

    # Open the file to read lines
    try:
        with open(file_path, 'r') as file:
            file.readline()
            for line in file:
                points = line.split()
                adjL.insert(int(points[0]) + 1, int(points[1]) + 1)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return adjL

if __name__ == "__main__":

    Adjacency_List = load_file()

    while True:
        print("Menu:")
        print("1. Show all vertices that a node is connected to")
        print("2. Print Graph")
        print("3. Add connection")
        print("4. Store to file")
        print("5. Exit")
        print("6. Breadth First Search")
        print("7. Depth First Search")
        print("8. Remove Connection")
        print("9. Shortest Path")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            index1 = int(input("Enter the index: ").strip())
            Adjacency_List.print_Vertice(index1)
            print()
        elif choice == '2':
            Adjacency_List.print_graph()
        elif choice == '3':
            Adjacency_List.insert(1, 1)
        elif choice == '4':
            Adjacency_List.write_to_file()
        elif choice == '5':
            print("Exiting the menu...")
            break
        elif choice == '6':
            print("Loading DFS results.....\n---------------------")
            DFS_results = Adjacency_List.DFS(0)

        elif choice == '7':
            print("Loading DFS results.....\n---------------------")
            BFS_results = Adjacency_List.BFS(0)
        elif choice == '8':
            index = int(input("Enter the index: ").strip())
            connect_P = int(input("Enter the connection:").strip())
            Adjacency_List.remove_connect(index, connect_P)
        elif choice == '9':
            index9 = int(input("Enter the index: ").strip())
            destination = int(input("Enter the destination:").strip())
            Adjacency_List.Dijkstras(index9, destination)
        else:
            print("Invalid choice. Please enter a valid option (1-9).")  
