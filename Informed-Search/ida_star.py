
import math
import time

from puzzle import INITIAL_STATE, GOAL_STATE, get_neighbors
from heuristics import misplaced_tiles, manhattan_distance


def ida_star(initial_state, heuristic, max_states=1000000):
    threshold = heuristic(initial_state)
    path = [initial_state]
    path_set = {initial_state}
    states_explored = 0

    def search(g, threshold):
        nonlocal states_explored

        state = path[-1]
        f = g + heuristic(state)

        if f > threshold:
            return f

        if state == GOAL_STATE:
            return "FOUND"

        if states_explored >= max_states:
            return "LIMIT"

        states_explored += 1
        minimum = math.inf

        for neighbor in get_neighbors(state):
            # Avoid repeated states on the current path
            if neighbor in path_set:
                continue

            path.append(neighbor)
            path_set.add(neighbor)

            result = search(g + 1, threshold)

            if result == "FOUND":
                return "FOUND"

            path.pop()
            path_set.remove(neighbor)

            if result == "LIMIT":
                return "LIMIT"

            minimum = min(minimum, result)

        return minimum

    while True:
        result = search(0, threshold)

        if result == "FOUND":
            return path.copy(), states_explored

        if result == "LIMIT" or result == math.inf:
            return None, states_explored

        threshold = result


def run_search(name, heuristic, initial_state=INITIAL_STATE):
    print(f"\n{'=' * 40}")
    print(name)
    print("=" * 40)

    start_time = time.perf_counter()

    solution, states_explored = ida_star(
        initial_state,
        heuristic
    )

    elapsed_time = time.perf_counter() - start_time

    if solution is not None:
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)

        for state in solution:
            print(state)
    else:
        print("No solution found within the search limit.")

    print("States explored:", states_explored)
    print(f"Execution time: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    run_search(
        "IDA* with h1 - Misplaced Tiles",
        misplaced_tiles
    )

    run_search(
        "IDA* with h2 - Manhattan Distance",
        manhattan_distance
    )