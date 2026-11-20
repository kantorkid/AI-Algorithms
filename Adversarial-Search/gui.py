from minimax import get_best_move_alpha_beta

import tkinter as tk
from tkinter import messagebox

from othello import (
    BLACK, WHITE,
    create_board,
    valid_moves,
    make_move,
    count_disks,
    game_over
)

CELL_SIZE = 70
BOARD_SIZE = 8


class OthelloGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Othello - Human vs AI")

        self.board = create_board()

        self.human_player = BLACK
        self.ai_player = WHITE
        self.ai_depth = 4

        self.current_player = self.human_player

        self.status = tk.Label(
            root,
            text="Black's Turn",
            font=("Arial", 16)
        )
        self.status.pack(pady=10)

        self.canvas = tk.Canvas(
            root,
            width=BOARD_SIZE * CELL_SIZE,
            height=BOARD_SIZE * CELL_SIZE,
            bg="darkgreen"
        )
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.handle_click)

        self.score = tk.Label(
            root,
            text="Black: 2 | White: 2",
            font=("Arial", 14)
        )
        self.score.pack(pady=10)

        self.draw_board()

    def draw_board(self):
        """Draw squares, disks, and legal moves."""
        self.canvas.delete("all")

        moves = (
            valid_moves(self.board, self.human_player)
            if self.current_player == self.human_player
            and not game_over(self.board)
            else []
        )

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill="#228B22",
                    outline="black"
                )

                piece = self.board[row][col]

                if piece != 0:
                    color = "black" if piece == BLACK else "white"

                    self.canvas.create_oval(
                        x1 + 7, y1 + 7,
                        x2 - 7, y2 - 7,
                        fill=color
                    )

                elif (row, col) in moves:
                    self.canvas.create_oval(
                        x1 + 28, y1 + 28,
                        x2 - 28, y2 - 28,
                        fill="yellow",
                        outline=""
                    )

        black, white = count_disks(self.board)

        self.score.config(
            text=f"Black: {black} | White: {white}"
        )

    def handle_click(self, event):
        """Respond when the human clicks a square."""

        if self.current_player != self.human_player:
            return

        if game_over(self.board):
            return

        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        if (row, col) not in valid_moves(
            self.board, self.current_player
        ):
            return

        self.board = make_move(
            self.board, row, col, self.current_player
        )

        if game_over(self.board):
            self.draw_board()
            self.show_winner()
            return

        
        # Switch from the human to the AI.
        self.current_player = self.ai_player

        self.status.config(text="AI thinking...")
        self.draw_board()

        # Allow Tkinter to update before the AI moves.
        self.root.after(200, self.ai_move)


    def show_winner(self):
        """Display the final result."""
        black, white = count_disks(self.board)

        if black > white:
            result = "Black wins!"
        elif white > black:
            result = "White wins!"
        else:
            result = "It's a tie!"

        self.status.config(text="Game Over")

        messagebox.showinfo(
            "Game Over",
            f"{result}\nBlack: {black}\nWhite: {white}"
        )


    def ai_move(self):
        """Let the AI select and execute a move."""

        if game_over(self.board):
            self.show_winner()
            return

        if self.current_player != self.ai_player:
            return

        move = get_best_move_alpha_beta(
            self.board,
            self.ai_player,
            depth=self.ai_depth
        )

        if move is None:
            # White has no legal moves and must pass.
            self.current_player = self.human_player
            self.status.config(text="White passes - Black's Turn")
            self.draw_board()
            return

        row, col = move

        self.board = make_move(
            self.board,
            row,
            col,
            self.ai_player
        )

        if game_over(self.board):
            self.draw_board()
            self.show_winner()
            return

        # Return control to the human.
        self.current_player = self.human_player

        # If the human cannot move, the AI plays again.
        if not valid_moves(self.board, self.human_player):

            if game_over(self.board):
                self.draw_board()
                self.show_winner()
                return

            self.current_player = self.ai_player
            self.status.config(
                text="Black has no legal moves. AI plays again..."
            )
            self.draw_board()
            self.root.after(200, self.ai_move)
            return

        self.status.config(text="Black's Turn")
        self.draw_board()


if __name__ == "__main__":
    root = tk.Tk()
    app = OthelloGUI(root)
    root.mainloop()
