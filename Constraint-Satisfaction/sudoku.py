
"""
CS480 Module 4 - Constraint Satisfaction Problems

Task 1: Naive Backtracking Sudoku Solver
"""

SIZE = 9


def print_board(board):
    """Display a Sudoku board in a readable format."""
    for row in range(SIZE):
        if row > 0 and row % 3 == 0:
            print("-" * 21)

        for col in range(SIZE):
            if col > 0 and col % 3 == 0:
                print("|", end=" ")

            value = board[row][col]
            print(value if value != 0 else ".", end=" ")

        print()


def find_empty(board):
    """Find the first empty cell, scanning row by row."""
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                return row, col

    return None


def is_valid(board, row, col, number):
    """Check whether a number satisfies Sudoku constraints."""

    # Row constraint
    if number in board[row]:
        return False

    # Column constraint
    for r in range(SIZE):
        if board[r][col] == number:
            return False

    # 3x3 box constraint
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == number:
                return False

    return True


def solve_naive(board, stats=None):
    """
    Solve Sudoku using naive recursive backtracking.

    Variables: first available empty cell
    Values: digits 1 through 9 in ascending order
    """

    if stats is not None:
        stats["calls"] += 1

    empty = find_empty(board)

    if empty is None:
        return True

    row, col = empty

    for number in range(1, 10):
        if is_valid(board, row, col, number):

            # Assign a value
            board[row][col] = number

            # Continue solving
            if solve_naive(board, stats):
                return True

            # Undo assignment (backtrack)
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

    if solve_naive(puzzle):
        print("\nSolved Sudoku:")
        print_board(puzzle)
    else:
        print("\nNo solution exists.")
