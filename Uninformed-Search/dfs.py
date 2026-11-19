import time
from collections import deque

from puzzle import (
    INITIAL_STATE,
    GOAL_STATE,
    move_up,
    move_down,
    move_left,
    move_right
)


# start puzzle
def dfs(initial_state, max_depth=30, max_states=1000000):
    frontier = deque([(initial_state, [initial_state])])
    states_explored = 0

    # Try all four possible movements
    moves = [move_up, move_down, move_left, move_right]

    while frontier:
        current_state, path = frontier.pop()
        current_depth = len(path) - 1

        states_explored += 1
        
        if current_state == GOAL_STATE:
            print("Goal found!")
            return path, states_explored

        # print("Exploring:", current_state)
        if states_explored >= max_states:
            print("Search stopped: state limit reached.")
            return None, states_explored

        if current_depth >= max_depth:
            continue

        for move in moves:
            neighbor = move(current_state)

            if neighbor is not None and neighbor not in path:
                new_path = path + [neighbor]
                frontier.append((neighbor, new_path))
    return None, states_explored


if __name__ == "__main__":
    start_time = time.perf_counter()

    solution, states_explored = dfs(INITIAL_STATE)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if solution is not None:
        print("Solution:", solution)
        print("Number of moves:", len(solution) - 1)
    else:
        print("No solution found within the search limit.")
        
    print("States explored:", states_explored)
    print("Execution time:", elapsed_time, "seconds")


