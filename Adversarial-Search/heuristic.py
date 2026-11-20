from othello import (
    BLACK, WHITE, EMPTY,
    BOARD_SIZE, DIRECTIONS,
    inside_board, valid_moves,
    count_disks, game_over
)

POSITION_WEIGHTS = [
    [120, -20, 20, 5, 5, 20, -20, 120],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [20, -5, 15, 3, 3, 15, -5, 20],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [20, -5, 15, 3, 3, 15, -5, 20],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [120, -20, 20, 5, 5, 20, -20, 120]
]

def normalized_difference(a, b):
    """Compare two nonnegative quantities on a -100 to 100 scale."""
    total = a + b

    if total == 0:
        return 0

    return 100 * (a - b) / total


def disk_score(board, player):
    """Calculate normalized disk advantage."""
    black, white = count_disks(board)

    if player == BLACK:
        return normalized_difference(black, white)

    return normalized_difference(white, black)


def positional_score(board, player):
    """Calculate positional advantage."""
    score = 0
    max_absolute_score = sum(
        abs(weight)
        for row in POSITION_WEIGHTS
        for weight in row
    )

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            weight = POSITION_WEIGHTS[row][col]

            if board[row][col] == player:
                score += weight

            elif board[row][col] == -player:
                score -= weight

    return 100 * score / max_absolute_score


def count_frontier_disks(board, player):
    """Count disks adjacent to empty squares."""
    count = 0

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):

            if board[row][col] != player:
                continue

            for dr, dc in DIRECTIONS:
                r = row + dr
                c = col + dc

                if (
                    inside_board(r, c)
                    and board[r][c] == EMPTY
                ):
                    count += 1
                    break

    return count


def frontier_score(board, player):
    """Reward having fewer frontier disks."""
    player_frontier = count_frontier_disks(
        board, player
    )

    opponent_frontier = count_frontier_disks(
        board, -player
    )

    return normalized_difference(
        opponent_frontier,
        player_frontier
    )



def mobility_score(board, player):
    """Calculate advantage in available legal moves."""
    player_moves = len(valid_moves(board, player))
    opponent_moves = len(valid_moves(board, -player))

    return normalized_difference(
        player_moves,
        opponent_moves
    )


def evaluate_board(board, player):
    """Evaluate a board from the player's perspective."""

    if game_over(board):
        black, white = count_disks(board)

        player_disks = black if player == BLACK else white
        opponent_disks = white if player == BLACK else black

        if player_disks > opponent_disks:
            return 100000

        if player_disks < opponent_disks:
            return -100000

        return 0

    disk = disk_score(board, player)
    position = positional_score(board, player)
    frontier = frontier_score(board, player)
    mobility = mobility_score(board, player)

    return (
        10 * disk
        + 10 * position
        + 10 * frontier
        + 10 * mobility
    )



if __name__ == "__main__":
    from othello import create_board, make_move

    board = create_board()

    print("Initial board evaluation:")
    print("Black:", evaluate_board(board, BLACK))
    print("White:", evaluate_board(board, WHITE))

    board = make_move(board, 2, 3, BLACK)

    print("\nAfter Black moves to (2, 3):")
    print("Black:", evaluate_board(board, BLACK))
    print("White:", evaluate_board(board, WHITE))
