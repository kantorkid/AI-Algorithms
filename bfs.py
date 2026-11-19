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
def bfs(initial_state, max_states=10000000):    
    frontier = deque([initial_state])
    visited = {initial_state}
    parent = {initial_state: None}
    states_explored = 0

    # Try all four possible movements
    moves = [move_up, move_down, move_left, move_right]

    while frontier:
        current_state = frontier.popleft()
        states_explored += 1

        
        if current_state == GOAL_STATE:
            print("Goal found!")

            path = []
            state = current_state

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()
            return path, states_explored

        if states_explored >= max_states:
            print("Search stopped: state limit reached.")
            return None, states_explored

        # print("Exploring:", current_state)

        for move in moves:
            neighbor = move(current_state)

            if neighbor is not None and neighbor not in visited:
                frontier.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current_state
        
    return None, states_explored




if __name__ == "__main__":
    start_time = time.perf_counter()

    solution, states_explored = bfs(INITIAL_STATE)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if solution is not None:
        print("Solution:", solution)
        print("Number of moves:", len(solution) - 1)
    else:
        print("No solution found within the search limit.")

    print("States explored:", states_explored)
    print("Execution time:", elapsed_time, "seconds")

