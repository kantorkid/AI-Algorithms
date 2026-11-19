
import time

from puzzle import (
    INITIAL_STATE,
    GOAL_STATE,
    move_up,
    move_down,
    move_left,
    move_right
)


def reconstruct_path(meeting_state, parent_start, parent_goal):
    path_start = []
    state = meeting_state

    while state is not None:
        path_start.append(state)
        state = parent_start[state]

    path_start.reverse()

    path_goal = []
    state = parent_goal[meeting_state]

    while state is not None:
        path_goal.append(state)
        state = parent_goal[state]

    return path_start + path_goal


def bidirectional_dfs(initial_state, max_depth=30, max_states=1000000):
    # Two LIFO stacks
    stack_start = [(initial_state, 0)]
    stack_goal = [(GOAL_STATE, 0)]

    # Parent dictionaries also track visited states
    parent_start = {initial_state: None}
    parent_goal = {GOAL_STATE: None}

    states_explored = 0
    moves = [move_up, move_down, move_left, move_right]

    if initial_state == GOAL_STATE:
        return [initial_state], 0

    while stack_start or stack_goal:

        # Alternate between forward and backward DFS
        for stack, parents, opposite_parents in [
            (stack_start, parent_start, parent_goal),
            (stack_goal, parent_goal, parent_start)
        ]:
            if not stack:
                continue

            current_state, depth = stack.pop()
            states_explored += 1

            if states_explored >= max_states:
                print("Search stopped: state limit reached.")
                return None, states_explored

            if depth >= max_depth:
                continue

            for move in moves:
                neighbor = move(current_state)

                if neighbor is None or neighbor in parents:
                    continue

                parents[neighbor] = current_state

                if neighbor in opposite_parents:
                    print("Searches met!")

                    solution = reconstruct_path(
                        neighbor,
                        parent_start,
                        parent_goal
                    )

                    return solution, states_explored

                stack.append((neighbor, depth + 1))

    return None, states_explored


if __name__ == "__main__":
    start_time = time.perf_counter()

    solution, states_explored = bidirectional_dfs(INITIAL_STATE)

    elapsed_time = time.perf_counter() - start_time

    if solution is not None:
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)

        print("Solution path:")
        for state in solution:
            print(state)
    else:
        print("No solution found within the search limits.")

    print("States explored:", states_explored)
    print("Execution time:", elapsed_time, "seconds")
