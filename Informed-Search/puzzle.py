
# Initial configuration from the Informed Search assignment
INITIAL_STATE = (
    3, 17, 9, 5, 21,
    11, 0, 13, 19, 10,
    6, 24, 22, 1, 20,
    16, 14, 4, 12, 15,
    18, 8, 23, 2, 7
)

# Goal configuration
GOAL_STATE = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    16, 17, 18, 19, 20,
    21, 22, 23, 24, 0
)


def find_blank(state):
    return state.index(0)


def swap_tiles(state, index1, index2):
    new_state = list(state)

    new_state[index1], new_state[index2] = (
        new_state[index2], new_state[index1]
    )

    return tuple(new_state)


def move_up(state):
    blank = find_blank(state)

    if blank < 5:
        return None

    return swap_tiles(state, blank, blank - 5)


def move_down(state):
    blank = find_blank(state)

    if blank >= 20:
        return None

    return swap_tiles(state, blank, blank + 5)


def move_left(state):
    blank = find_blank(state)

    if blank % 5 == 0:
        return None

    return swap_tiles(state, blank, blank - 1)


def move_right(state):
    blank = find_blank(state)

    if blank % 5 == 4:
        return None

    return swap_tiles(state, blank, blank + 1)


def get_neighbors(state):
    moves = [move_up, move_down, move_left, move_right]

    neighbors = []

    for move in moves:
        neighbor = move(state)

        if neighbor is not None:
            neighbors.append(neighbor)

    return neighbors


def is_solvable(state):
    tiles = [tile for tile in state if tile != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    # For a 5x5 puzzle, the inversion count must be even.
    return inversions % 2 == 0


def print_puzzle(state):
    for row in range(0, 25, 5):
        print(*[f"{tile:2}" for tile in state[row:row + 5]])
    print()


if __name__ == "__main__":
    print("Initial State:")
    print_puzzle(INITIAL_STATE)

    print("Goal State:")
    print_puzzle(GOAL_STATE)

    print("Solvable:", is_solvable(INITIAL_STATE))
    print("Available moves:", len(get_neighbors(INITIAL_STATE)))
