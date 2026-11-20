
import unittest

from othello import (
    BLACK, WHITE, EMPTY,
    create_board, valid_moves,
    make_move, count_disks, game_over
)

from heuristic import evaluate_board

from minimax import (
    get_best_move,
    get_best_move_alpha_beta
)


class TestOthello(unittest.TestCase):

    def test_initial_board(self):
        board = create_board()

        self.assertEqual(count_disks(board), (2, 2))
        self.assertFalse(game_over(board))

    def test_initial_legal_moves(self):
        board = create_board()

        expected = {
            (2, 3), (3, 2),
            (4, 5), (5, 4)
        }

        self.assertEqual(
            set(valid_moves(board, BLACK)),
            expected
        )

    def test_move_flips_disks(self):
        board = create_board()

        new_board = make_move(
            board, 2, 3, BLACK
        )

        self.assertEqual(
            count_disks(new_board),
            (4, 1)
        )

        # Original board should remain unchanged.
        self.assertEqual(
            count_disks(board),
            (2, 2)
        )

    def test_heuristic_symmetry(self):
        board = create_board()

        black_score = evaluate_board(
            board, BLACK
        )

        white_score = evaluate_board(
            board, WHITE
        )

        self.assertAlmostEqual(
            black_score,
            -white_score
        )

    def test_ai_selects_legal_move(self):
        board = create_board()

        move = get_best_move_alpha_beta(
            board, BLACK, depth=4
        )

        self.assertIn(
            move,
            valid_moves(board, BLACK)
        )

    def test_minimax_matches_alpha_beta(self):
        board = create_board()

        minimax_move = get_best_move(
            board, BLACK, depth=4
        )

        alpha_beta_move = get_best_move_alpha_beta(
            board, BLACK, depth=4
        )

        self.assertEqual(
            minimax_move,
            alpha_beta_move
        )

    def test_game_over_on_full_board(self):
        board = [
            [BLACK for _ in range(8)]
            for _ in range(8)
        ]

        self.assertTrue(game_over(board))
        self.assertEqual(
            count_disks(board),
            (64, 0)
        )


    def test_player_must_pass(self):
        """A player can have no moves while the game continues."""

        board = [
            [BLACK for _ in range(8)]
            for _ in range(8)
        ]

        board[0][0] = EMPTY
        board[0][1] = WHITE

        # Black can capture White at (0, 0).
        self.assertIn(
            (0, 0),
            valid_moves(board, BLACK)
        )

        # White has no legal moves and must pass.
        self.assertEqual(
            valid_moves(board, WHITE),
            []
        )

        # The game is not finished because Black can move.
        self.assertFalse(game_over(board))


if __name__ == "__main__":
    unittest.main()
