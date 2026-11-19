from bfs import bfs
from dfs import dfs
from puzzle import INITIAL_STATE

def main():
    print("24-Puzzle Solver")
    print("1. Breadth-First Search")
    print("2. Depth-First Search")

    choice = input("Select algorithm: ")

    if choice == "1":
        solution = bfs(INITIAL_STATE)
    elif choice == "2":
        solution = dfs(INITIAL_STATE)
    else:
        print("Invalid selection")
        return

    if solution:
        print("Solution found!")
    else:
        print("No solution found within search limits.")

if __name__ == "__main__":
    main()