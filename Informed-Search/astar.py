
import time
import heapq
from itertools import count

from puzzle import INITIAL_STATE, GOAL_STATE, get_neighbors
from heuristics import misplaced_tiles, manhattan_distance


def reconstruct_path(parent, state):
    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()
    return path


def astar(initial_state, heuristic, max_states=1000000):
    # Priority queue stores (f, g, order, state)
    frontier = []
    order = count()

    # Best known cost to reach each state
    g_score = {initial_state: 0}

    # Parent dictionary for reconstructing the solution
    parent = {initial_state: None}

    initial_h = heuristic(initial_state)

    heapq.heappush(
        frontier,
        (initial_h, 0, next(order), initial_state)
    )

    states_explored = 0

    while frontier:
        f, g, _, current_state = heapq.heappop(frontier)

        # Skip outdated queue entries
        if g != g_score[current_state]:
            continue

        states_explored += 1

        if current_state == GOAL_STATE:
            print("Goal found!")
            return reconstruct_path(parent, current_state), states_explored

        if states_explored >= max_states:
            print("Search stopped: state limit reached.")
            return None, states_explored

        for neighbor in get_neighbors(current_state):
            new_g = g + 1

            # Only update when a better path is found
            if new_g < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = new_g
                parent[neighbor] = current_state

                h = heuristic(neighbor)
                new_f = new_g + h

                heapq.heappush(
                    frontier,
                    (new_f, new_g, next(order), neighbor)
                )

    return None, states_explored


def run_search(name, heuristic, initial_state=INITIAL_STATE):
    print(f"\n{'=' * 40}")
    print(name)
    print("=" * 40)

    start_time = time.perf_counter()

    solution, states_explored = astar(
        initial_state,
        heuristic
    )

    elapsed_time = time.perf_counter() - start_time

    if solution is not None:
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)
        print("Solution path:")

        for state in solution:
            print(state)
    else:
        print("No solution found within the search limit.")

    print("States explored:", states_explored)
    print(f"Execution time: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    run_search("A* with h1 - Misplaced Tiles", misplaced_tiles)
    run_search("A* with h2 - Manhattan Distance", manhattan_distance)