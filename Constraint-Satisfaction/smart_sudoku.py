
"""
CS480 Module 4 - Constraint Satisfaction Problems

Task 2: Smart Backtracking Sudoku Solver

Strategies:
1. Minimum Remaining Values (MRV)
2. Least Constraining Value (LCV)
3. Forward Checking (FC)
"""

from sudoku import (
    SIZE,
    is_valid,
    print_board
)


def get_domain(board, row, col):
    """Return all legal values for an empty cell."""

    if board[row][col] != 0:
        return []

    return [
        number
        for number in range(1, 10)
        if is_valid(board, row, col, number)
    ]


def select_mrv(board):
    """
    Select the empty cell with the fewest legal values.

    This is the Minimum Remaining Values heuristic.
    """

    best_cell = None
    smallest_domain = 10

    for row in range(SIZE):
        for col in range(SIZE):

            if board[row][col] != 0:
                continue

            domain = get_domain(board, row, col)

            if len(domain) < smallest_domain:
                smallest_domain = len(domain)
                best_cell = (row, col)

    return best_cell


def get_neighbors(board, row, col):
    """
    Return empty cells sharing a row, column,
    or 3x3 box with the selected cell.
    """

    neighbors = set()

    # Same row and column
    for i in range(SIZE):
        if board[row][i] == 0 and i != col:
            neighbors.add((row, i))

        if board[i][col] == 0 and i != row:
            neighbors.add((i, col))

    # Same 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == 0 and (r, c) != (row, col):
                neighbors.add((r, c))

    return neighbors


def order_lcv(board, row, col):
    """
    Order legal values by how few possibilities
    they eliminate from neighboring cells.
    """

    domain = get_domain(board, row, col)
    neighbors = get_neighbors(board, row, col)

    def constraint_count(number):
        count = 0

        for r, c in neighbors:
            if number in get_domain(board, r, c):
                count += 1

        return count

    return sorted(domain, key=constraint_count)


def forward_check(board):
    """
    Check that every remaining empty cell
    has at least one legal value.

    Return False if any empty cell has
    an empty domain.
    """

    for row in range(SIZE):
        for col in range(SIZE):

            if board[row][col] == 0:

                domain = get_domain(board, row, col)

                if len(domain) == 0:
                    return False

    return True


def solve_smart(board, stats=None):
    """
    Solve Sudoku using smart backtracking.

    Strategies:
    - MRV: Select the most constrained variable.
    - LCV: Try the least constraining value first.
    - FC: Reject assignments that empty a remaining domain.
    """

    if stats is not None:
        stats["calls"] += 1

    # MRV: Select the empty cell with the fewest options.
    cell = select_mrv(board)

    # No empty cells remain.
    if cell is None:
        return True

    row, col = cell

    # LCV: Try values in least-constraining order.
    for number in order_lcv(board, row, col):

        # Assign the candidate value.
        board[row][col] = number

        # FC: Continue only if remaining domains are nonempty.
        if forward_check(board):

            if solve_smart(board, stats):
                return True

        # Undo the assignment if this branch fails.
        board[row][col] = 0
            
        if stats is not None:
            stats["backtracks"] += 1

    return False


    
if __name__ == "__main__":

    puzzle = [
        [0, 0, 3, 0, 2, 0, 6, 0, 0],
        [9, 0, 0, 3, 0, 5, 0, 0, 1],
        [0, 0, 1, 8, 0, 6, 4, 0, 0],
        [0, 0, 8, 1, 0, 2, 9, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 6, 7, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 9],
        [0, 0, 5, 0, 1, 0, 3, 0, 0]
    ]

    print("Original Sudoku:")
    print_board(puzzle)

    print("\nMRV selected cell:", select_mrv(puzzle))

    cell = select_mrv(puzzle)

    if cell is not None:
        row, col = cell
        print("Legal values:", get_domain(puzzle, row, col))
        print("LCV ordered values:", order_lcv(puzzle, row, col))

    print("\nForward Checking:", forward_check(puzzle))

    print("\nSolving Sudoku with Smart Backtracking:")

    smart_board = [row[:] for row in puzzle]

    if solve_smart(smart_board):
        print("\nSolved Sudoku:")
        print_board(smart_board)
    else:
        print("\nNo solution exists.")
