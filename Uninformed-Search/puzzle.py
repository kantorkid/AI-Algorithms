# Initial 8-puzzle configuration
# INITIAL_STATE = (
#    1, 2, 3,
#    4, 0, 6,
#    7, 5, 8
# )

# 24-puzzle
INITIAL_STATE = (
    9, 24, 3, 5, 17,
    6, 0, 13, 19, 10,
    11, 21, 22, 1, 20,
    16, 4, 14, 12, 15,
    8, 18, 23, 2, 7
)

# Initial 8-puzzle Goal configuration
# GOAL_STATE = (
#    1, 2, 3,
#    4, 5, 6,
#    7, 8, 0
# )

# 24-puzzle
GOAL_STATE = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    16, 17, 18, 19, 20,
    21, 22, 23, 24, 0
)

# Find the blank tile
def find_blank(state):
    return state.index(0)

# Check whether the blank can move up
def can_move_up(state):
    blank = find_blank(state)

    # if blank >= 3: # 8-puzzle
    if blank >= 5: # 24-puzzle

        return True
    else:
        return False

# Check whether the blank can move down
def can_move_down(state):
    blank = find_blank(state)

    # if blank < 6: # 8-puzzle
    if blank < 20: # 24-puzzle

        return True
    else:
        return False


def can_move_left(state):
    blank = find_blank(state)

    # if blank % 3 != 0: # 8-puzzle
    if blank % 5 != 0: # 24-puzzle

        return True
    else:
        return False

def can_move_right(state):
    blank = find_blank(state)

    # if blank % 3 != 2: # 8-puzzle
    if blank % 5 != 4: # 24-puzzle

        return True
    else:
        return False

def move_up(state):
    if not can_move_up(state):
        return None

    blank = find_blank(state)
    # new_position = blank - 3 # 8-puzzle
    new_position = blank - 5 # 24-puzzle
    new_state = list(state)

    new_state[blank], new_state[new_position] = (
        new_state[new_position], new_state[blank]
    )

    return tuple(new_state)

def move_down(state):
    if not can_move_down(state):
        return None

    blank = find_blank(state)
    # new_position = blank + 3 # 8-puzzle
    new_position = blank + 5 # 24-puzzle
    new_state = list(state)

    new_state[blank], new_state[new_position] = (
        new_state[new_position], new_state[blank]
        )

    return tuple(new_state)

def move_left(state):
    if not can_move_left(state):
        return None

    blank = find_blank(state)
    new_position = blank - 1 
    new_state = list(state)

    new_state[blank], new_state[new_position] = (
        new_state[new_position], new_state[blank]
        )

    return tuple(new_state)

def move_right(state):
    if not can_move_right(state):
        return None

    blank = find_blank(state)
    new_position = blank + 1 
    new_state = list(state)

    new_state[blank], new_state[new_position] = (
        new_state[new_position], new_state[blank]
        )

    return tuple(new_state)

def is_solvable(state):
    tiles = [tile for tile in state if tile != 0]

    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    # For a 5x5 puzzle, solvability requires even inversions
    return inversions % 2 == 0

if __name__ == "__main__":
    print("Original:", INITIAL_STATE)
    print("Moving up:", move_up(INITIAL_STATE))
    print("Moving down:", move_down(INITIAL_STATE))
    print("Moving right:", move_right(INITIAL_STATE))
    print("Puzzle solvable:", is_solvable(INITIAL_STATE))
