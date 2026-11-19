
import random


def random_board(n):
    """
    Generate a random N-Queens board.
    One queen is placed in each column.
    """
    return [random.randrange(n) for _ in range(n)]


def attacking_pairs(board):
    """
    Count the number of pairs of queens
    attacking each other.
    """
    n = len(board)
    attacks = 0

    for i in range(n):
        for j in range(i + 1, n):

            # Same row
            if board[i] == board[j]:
                attacks += 1

            # Same diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                attacks += 1

    return attacks


def hill_climbing_nqueens(n):
    """
    Minimize attacking pairs using steepest-ascent
    hill climbing (minimizing the objective).
    """
    board = random_board(n)
    initial_board = board.copy()

    current_attacks = attacking_pairs(board)
    steps = 0

    while True:
        best_board = None
        best_attacks = current_attacks

        # Examine every possible queen move
        for col in range(n):
            original_row = board[col]

            for row in range(n):
                if row == original_row:
                    continue

                neighbor = board.copy()
                neighbor[col] = row

                attacks = attacking_pairs(neighbor)

                if attacks < best_attacks:
                    best_attacks = attacks
                    best_board = neighbor

        # No improving neighbor: local minimum
        if best_board is None:
            break

        board = best_board
        current_attacks = best_attacks
        steps += 1

        # Found a valid solution
        if current_attacks == 0:
            break

    return {
        "initial_board": initial_board,
        "final_board": board,
        "initial_attacks": attacking_pairs(initial_board),
        "final_attacks": current_attacks,
        "steps": steps,
        "success": current_attacks == 0
    }


if __name__ == "__main__":
    result = hill_climbing_nqueens(8)

    print("N-Queens Hill Climbing")
    print("----------------------")
    print(f"Initial board: {result['initial_board']}")
    print(f"Final board:   {result['final_board']}")
    print(f"Initial attacking pairs: {result['initial_attacks']}")
    print(f"Final attacking pairs:   {result['final_attacks']}")
    print(f"Steps: {result['steps']}")
    print(f"Solution found: {result['success']}")
