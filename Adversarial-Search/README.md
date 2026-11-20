# Othello AI — Adversarial Search

## Overview

This project implements the classic Othello (Reversi) board game using Python and Tkinter. A human player competes against an AI opponent that uses Minimax with Alpha-Beta Pruning.

The project demonstrates adversarial search, heuristic evaluation, and decision-making in a two-player, zero-sum game.

## Features

- Interactive 8×8 Othello board
- Human (Black) versus AI (White)
- Legal move indicators displayed as yellow dots
- Automatic disk flipping
- Real-time disk counts
- Automatic turn passing when no legal moves are available
- Game-over detection and winner announcement
- Balanced heuristic evaluation
- Minimax and Alpha-Beta Pruning algorithms
- Adjustable AI search depth

## Project Structure

```text
Adversarial-Search/
├── othello.py        # Game rules and board operations
├── heuristic.py      # Balanced heuristic evaluation
├── minimax.py        # Minimax and Alpha-Beta algorithms
├── gui.py            # Tkinter graphical interface
├── test_othello.py   # Automated unit tests
├── DESIGN.md         # Algorithm and heuristic documentation
└── README.md         # Project instructions
```

## Requirements

- Python 3.9 or newer
- Tkinter graphical toolkit

The project uses Python's standard library and does not require additional Python packages.

Tkinter must be available in the Python installation. On some macOS systems, Python may need to be installed or rebuilt with Tcl/Tk support.

## Running the Game

Open a terminal in the `Adversarial-Search` directory.

Run:

```bash
python3 gui.py
```

A graphical Othello board will open.

### How to Play

1. The human controls Black and moves first.
2. Yellow dots indicate available legal moves.
3. Click a yellow dot to place a black disk.
4. Captured white disks automatically flip to black.
5. The AI calculates its response using Alpha-Beta Pruning.
6. Continue alternating turns until neither player has a legal move.
7. The player with the most disks wins.

If a player cannot make a legal move, their turn is automatically skipped.

## AI Implementation

The AI uses a balanced heuristic consisting of four components:

- Disk advantage
- Positional advantage
- Frontier disk advantage
- Mobility advantage

The heuristic evaluates nonterminal board positions using:

\[
H(s,p) = 10D + 10P + 10F + 10M
\]

Minimax searches possible future moves while assuming the opponent will make the strongest available response.

Alpha-Beta Pruning improves search efficiency by skipping branches that cannot change the final decision.

The default AI search depth is four.

To change the difficulty, edit the following line in `gui.py`:

```python
self.ai_depth = 4
```

Increasing the depth generally improves search quality but also increases computation time.

## Running Tests

Execute:

```bash
python3 test_othello.py -v
```

The automated tests check game initialization, legal moves, disk flipping, heuristic symmetry, AI move legality, Minimax/Alpha-Beta agreement on the starting board, and game termination on a full board.

## Performance

In an initial benchmark at search depth four:

| Algorithm | Execution time |
|---|---:|
| Minimax | 0.0707 seconds |
| Alpha-Beta Pruning | 0.0286 seconds |

Both algorithms selected the same opening move.

Alpha-Beta Pruning was approximately 2.47 times faster in this test. Actual performance varies by board position and computer.

## Additional Documentation

See `DESIGN.md` for a detailed explanation of the heuristic function, Minimax algorithm, Alpha-Beta Pruning, and initial testing results.
