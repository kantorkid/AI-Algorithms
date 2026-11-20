BOARD_SIZE = 8
EMPTY = 0
BLACK = 1
WHITE = -1

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]


def create_board():
    """Create an 8x8 Othello board."""
    board = [
        [EMPTY for _ in range(BOARD_SIZE)]
        for _ in range(BOARD_SIZE)
    ]

    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE

    return board

def inside_board(row, col):
    """Check whether a position is on the board."""
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE


def get_flips(board, row, col, player):
    """Return opponent disks captured by a move."""
    if not inside_board(row, col):
        return []

    if board[row][col] != EMPTY:
        return []

    flips = []
    opponent = -player

    for dr, dc in DIRECTIONS:
        r = row + dr
        c = col + dc
        direction_flips = []

        while inside_board(r, c) and board[r][c] == opponent:
            direction_flips.append((r, c))
            r += dr
            c += dc

        if (
            direction_flips
            and inside_board(r, c)
            and board[r][c] == player
        ):
            flips.extend(direction_flips)

    return flips


def valid_moves(board, player):
    """Find every legal move for a player."""
    moves = []

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if get_flips(board, row, col, player):
                moves.append((row, col))

    return moves


def make_move(board, row, col, player):
    """Apply a legal move and return a new board."""
    flips = get_flips(board, row, col, player)

    if not flips:
        return None

    new_board = [line.copy() for line in board]

    new_board[row][col] = player

    for r, c in flips:
        new_board[r][c] = player

    return new_board


def game_over(board):
    """Game ends when neither player has a legal move."""
    return (
        not valid_moves(board, BLACK)
        and not valid_moves(board, WHITE)
    )


def count_disks(board):
    """Count black and white disks."""
    black = sum(row.count(BLACK) for row in board)
    white = sum(row.count(WHITE) for row in board)

    return black, white


def print_board(board):
    """Display the board in the terminal."""
    symbols = {
        EMPTY: ".",
        BLACK: "B",
        WHITE: "W"
    }

    print("  0 1 2 3 4 5 6 7")

    for row_index, row in enumerate(board):
        print(
            row_index,
            " ".join(symbols[cell] for cell in row)
        )


if __name__ == "__main__":
    board = create_board()

    print("Initial Othello Board:")
    print_board(board)

    print("\nBlack valid moves:")
    print(valid_moves(board, BLACK))

    print("\nWhite valid moves:")
    print(valid_moves(board, WHITE))

    print("\nBlack plays at (2, 3):")
    board = make_move(board, 2, 3, BLACK)
    print_board(board)

    print("\nDisk counts:")
    print(count_disks(board))
