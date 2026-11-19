
import time

from input_handler import get_puzzle_input
from puzzle import print_puzzle
from heuristics import misplaced_tiles, manhattan_distance
from astar import astar
from ida_star import ida_star


def main():
    print("24-Puzzle Informed Search\n")

    try:
        initial_state = get_puzzle_input()
    except ValueError as error:
        print("Invalid input:", error)
        return

    print("\nInitial State:")
    print_puzzle(initial_state)

    print("Select Search Algorithm:")
    print("1. A*")
    print("2. IDA*")

    algorithm_choice = input("Choice (1 or 2): ").strip()

    if algorithm_choice not in ("1", "2"):
        print("Invalid algorithm choice.")
        return

    print("\nSelect Heuristic:")
    print("1. h1 - Misplaced Tiles")
    print("2. h2 - Manhattan Distance")

    heuristic_choice = input("Choice (1 or 2): ").strip()

    if heuristic_choice == "1":
        heuristic = misplaced_tiles
        heuristic_name = "Misplaced Tiles"
    elif heuristic_choice == "2":
        heuristic = manhattan_distance
        heuristic_name = "Manhattan Distance"
    else:
        print("Invalid heuristic choice.")
        return

    algorithm = astar if algorithm_choice == "1" else ida_star
    algorithm_name = "A*" if algorithm_choice == "1" else "IDA*"

    print(f"\nRunning {algorithm_name} with {heuristic_name}...")

    start_time = time.perf_counter()

    solution, states_explored = algorithm(
        initial_state,
        heuristic
    )

    elapsed_time = time.perf_counter() - start_time

    if solution is not None:
        print("\nSolution found!")
        print("Number of moves:", len(solution) - 1)

        print("\nSolution Path:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_puzzle(state)
    else:
        print("\nNo solution found within the search limit.")

    print("States explored:", states_explored)
    print(f"Execution time: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    main()
