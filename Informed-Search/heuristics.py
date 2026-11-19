
from puzzle import INITIAL_STATE, GOAL_STATE


# h1: Number of misplaced tiles
def misplaced_tiles(state):
    count = 0

    for i in range(len(state)):
        if state[i] != 0 and state[i] != GOAL_STATE[i]:
            count += 1

    return count


# h2: Manhattan distance
def manhattan_distance(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        current_row = i // 5
        current_col = i % 5

        goal_index = tile - 1
        goal_row = goal_index // 5
        goal_col = goal_index % 5

        distance += (
            abs(current_row - goal_row)
            + abs(current_col - goal_col)
        )

    return distance


if __name__ == "__main__":
    print("Initial State:")
    print(INITIAL_STATE)

    print("\nh1 - Misplaced Tiles:", misplaced_tiles(INITIAL_STATE))
    print("h2 - Manhattan Distance:", manhattan_distance(INITIAL_STATE))

    print("\nGoal State Tests:")
    print("h1:", misplaced_tiles(GOAL_STATE))
    print("h2:", manhattan_distance(GOAL_STATE))
