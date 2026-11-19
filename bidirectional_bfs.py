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

def reconstruct_path(meeting_state, parent_start, parent_goal):

    # Reconstruct the path from the initial state
    path_start = []
    state = meeting_state

    while state is not None:
        path_start.append(state)
        state = parent_start[state]

    path_start.reverse()

    # Reconstruct the path from the meeting state to the goal
    path_goal = []
    state = parent_goal[meeting_state]

    while state is not None:
        path_goal.append(state)
        state = parent_goal[state]

    # Combine both paths
    return path_start + path_goal

def bidirectional_bfs(initial_state, max_states=10000000):

    # Search forward from the initial state
    frontier_start = deque([initial_state])
    parent_start = {initial_state: None}

    # Search backward from the goal state
    frontier_goal = deque([GOAL_STATE])
    parent_goal = {GOAL_STATE: None}

    states_explored = 0
    depth_start = 0
    depth_goal = 0

    moves = [move_up, move_down, move_left, move_right]

    if initial_state == GOAL_STATE:
        return [initial_state], 0

    while frontier_start and frontier_goal:

        # Expand the smaller frontier, one complete level at a time
        if len(frontier_start) <= len(frontier_goal):
            frontier = frontier_start
            parents = parent_start
            opposite_parents = parent_goal
        else:
            frontier = frontier_goal
            parents = parent_goal
            opposite_parents = parent_start

        # Number of states in the current search level
        level_size = len(frontier)

        if frontier is frontier_start:
            print("Forward depth:", depth_start)
            depth_start += 1
        else:
            print("Backward depth:", depth_goal)
            depth_goal += 1

        for _ in range(level_size):
            current_state = frontier.popleft()
            states_explored += 1

            if states_explored >= max_states:
                print("Search stopped: state limit reached.")
                return None, states_explored

            for move in moves:
                neighbor = move(current_state)

                if neighbor is not None and neighbor not in parents:
                    parents[neighbor] = current_state
                    frontier.append(neighbor)

                    # Check whether the two searches have met
                    if neighbor in opposite_parents:
                        print("Searches met!")

                        solution = reconstruct_path(
                            neighbor,
                            parent_start,
                            parent_goal
                        )

                        return solution, states_explored

    return None, states_explored

if __name__ == "__main__":
    start_time = time.perf_counter()

    solution, states_explored = bidirectional_bfs(INITIAL_STATE)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if solution is not None:
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)
        print("Solution path:")

        for state in solution:
            print(state)
    else:
        print("No solution found within the search limit.")

    print("States explored:", states_explored)
    print("Execution time:", elapsed_time, "seconds")