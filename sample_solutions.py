
import time

from puzzle import GOAL_STATE
from bfs import bfs
from dfs import dfs


# A 24-puzzle configuration two moves from the goal
SAMPLE_STATE = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    16, 17, 18, 19, 20,
    21, 22, 0, 23, 24
)


def run_search(name, search_function):
    print(f"\n{'=' * 40}")
    print(name)
    print("=" * 40)

    start_time = time.perf_counter()
    solution, states_explored = search_function(SAMPLE_STATE)
    elapsed_time = time.perf_counter() - start_time

    if solution is not None:
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)

        print("\nSolution path:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            for row in range(0, 25, 5):
                print(state[row:row + 5])
            print()
    else:
        print("No solution found within search limits.")

    print("States explored:", states_explored)
    print(f"Execution time: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    run_search("Breadth-First Search (BFS)", bfs)

    run_search(
        "Depth-First Search (DFS)",
        lambda state: dfs(state, max_depth=2, max_states=100000)
    )
