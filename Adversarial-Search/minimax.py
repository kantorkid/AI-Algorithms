
from othello import (
    BLACK, WHITE,
    create_board, valid_moves,
    make_move, game_over
)

from heuristic import evaluate_board


def minimax(board, depth, current_player, ai_player):
    """
    Evaluate future moves using Minimax.

    depth: Remaining search depth.
    current_player: Player whose turn it is.
    ai_player: Player the AI is optimizing for.
    """

    # Base case: stop searching at the depth limit
    # or when the game is finished.
    if depth == 0 or game_over(board):
        return evaluate_board(board, ai_player)

    moves = valid_moves(board, current_player)

    # If this player has no legal moves, they must pass.
    if not moves:
        return minimax(
            board,
            depth - 1,
            -current_player,
            ai_player
        )

    if current_player == ai_player:
        # Maximizing player's turn.
        best_score = float("-inf")

        for row, col in moves:
            new_board = make_move(
                board, row, col, current_player
            )

            score = minimax(
                new_board,
                depth - 1,
                -current_player,
                ai_player
            )

            best_score = max(best_score, score)

        return best_score

    else:
        # Minimizing player's turn.
        best_score = float("inf")

        for row, col in moves:
            new_board = make_move(
                board, row, col, current_player
            )

            score = minimax(
                new_board,
                depth - 1,
                -current_player,
                ai_player
            )

            best_score = min(best_score, score)

        return best_score


def get_best_move(board, ai_player, depth=3):
    """Find the best move for the AI."""

    moves = valid_moves(board, ai_player)

    if not moves:
        return None

    best_move = None
    best_score = float("-inf")

    for row, col in moves:
        new_board = make_move(
            board, row, col, ai_player
        )

        score = minimax(
            new_board,
            depth - 1,
            -ai_player,
            ai_player
        )

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move

def alpha_beta(
    board, depth, alpha, beta,
    current_player, ai_player
):
    """Minimax search with Alpha-Beta Pruning."""

    if depth == 0 or game_over(board):
        return evaluate_board(board, ai_player)

    moves = valid_moves(board, current_player)

    # If no legal moves exist, the player passes.
    if not moves:
        return alpha_beta(
            board,
            depth - 1,
            alpha,
            beta,
            -current_player,
            ai_player
        )

    if current_player == ai_player:
        # Maximizing player
        best_score = float("-inf")

        for row, col in moves:
            new_board = make_move(
                board, row, col, current_player
            )

            score = alpha_beta(
                new_board,
                depth - 1,
                alpha,
                beta,
                -current_player,
                ai_player
            )

            best_score = max(best_score, score)
            alpha = max(alpha, best_score)

            if alpha >= beta:
                break  # Prune remaining moves

        return best_score

    else:
        # Minimizing player
        best_score = float("inf")

        for row, col in moves:
            new_board = make_move(
                board, row, col, current_player
            )

            score = alpha_beta(
                new_board,
                depth - 1,
                alpha,
                beta,
                -current_player,
                ai_player
            )

            best_score = min(best_score, score)
            beta = min(beta, best_score)

            if alpha >= beta:
                break  # Prune remaining moves

        return best_score


def get_best_move_alpha_beta(board, ai_player, depth=4):
    """Choose the best move using Alpha-Beta Pruning."""

    moves = valid_moves(board, ai_player)

    if not moves:
        return None

    best_move = None
    best_score = float("-inf")

    alpha = float("-inf")
    beta = float("inf")

    for row, col in moves:
        new_board = make_move(
            board, row, col, ai_player
        )

        score = alpha_beta(
            new_board,
            depth - 1,
            alpha,
            beta,
            -ai_player,
            ai_player
        )

        if score > best_score:
            best_score = score
            best_move = (row, col)

        alpha = max(alpha, best_score)

    return best_move


if __name__ == "__main__":
    import time

    board = create_board()
    depth = 4

    print("Testing Minimax vs Alpha-Beta")
    print("Search depth:", depth)

    start = time.perf_counter()
    minimax_move = get_best_move(
        board, BLACK, depth
    )
    minimax_time = time.perf_counter() - start

    start = time.perf_counter()
    alpha_beta_move = get_best_move_alpha_beta(
        board, BLACK, depth
    )
    alpha_beta_time = time.perf_counter() - start

    print("\nMinimax:")
    print("Move:", minimax_move)
    print(f"Time: {minimax_time:.4f} seconds")

    print("\nAlpha-Beta:")
    print("Move:", alpha_beta_move)
    print(f"Time: {alpha_beta_time:.4f} seconds")
