# Othello AI — Design Document

## 1. Project Overview

This project implements an 8×8 Othello (Reversi) game in Python with a graphical interface built using Tkinter. The human player controls Black, while the AI controls White.

The AI uses the Minimax algorithm with Alpha-Beta Pruning to select moves. A balanced heuristic evaluation function estimates the strategic value of nonterminal board positions.

## 2. Game Representation

The game board is represented as an 8×8 two-dimensional list.

- `1` represents a Black disk.
- `-1` represents a White disk.
- `0` represents an empty square.

The game engine identifies legal moves by checking all eight directions for opponent disks that can be captured. A legal move places a disk and flips the appropriate opponent disks.

When a player has no legal moves, their turn is skipped. The game ends when neither player can make a legal move. The player with the most disks wins.

## 3. Heuristic Evaluation Function

The AI uses four evaluation components:

**Disk advantage (D):** Measures the relative number of disks controlled by each player.

**Positional advantage (P):** Assigns strategic values to board squares. Corners receive high positive weights because corner disks cannot be flipped. Certain squares adjacent to corners receive negative weights because occupying them can create opportunities for the opponent.

**Frontier advantage (F):** Measures disks adjacent to empty squares. Having fewer frontier disks than the opponent is generally favorable because these disks may be more exposed to future captures.

**Mobility advantage (M):** Compares the number of legal moves available to each player. Greater mobility generally provides more strategic flexibility.

The combined heuristic is:

\[
H(s,p) = 10D + 10P + 10F + 10M
\]

Each component is normalized to a range between -100 and +100. Equal weights provide a balanced starting point rather than emphasizing only disk count or positional control.

For terminal positions, the evaluation returns +100000 for an AI victory, -100000 for a loss, and 0 for a tie. This ensures that winning takes priority over estimated strategic advantages.

## 4. Minimax Algorithm

Minimax searches possible future moves to a specified depth.

The maximizing player attempts to obtain the highest evaluation score, while the minimizing player attempts to obtain the lowest score.

At the search-depth limit, the algorithm evaluates the board using the heuristic function. At terminal positions, it evaluates the actual game result.

This approach assumes that the opponent will select the strongest available response.

## 5. Alpha-Beta Pruning

Alpha-Beta Pruning optimizes Minimax by eliminating branches that cannot influence the final decision.

Alpha represents the best score guaranteed to the maximizing player, while beta represents the best score guaranteed to the minimizing player.

A branch can be pruned when:

\[
\alpha \geq \beta
\]

Alpha-Beta Pruning preserves the Minimax result while potentially reducing the number of positions evaluated.

The graphical game uses Alpha-Beta Pruning with a default search depth of four.

## 6. Performance Evaluation

The algorithms were compared using the initial Othello board at search depth four.

| Metric | Minimax | Alpha-Beta |
|---|---:|---:|
| Selected move | (2, 3) | (2, 3) |
| Execution time | 0.0707 seconds | 0.0286 seconds |

In this test, Alpha-Beta Pruning was approximately 2.47 times faster than standard Minimax.

These measurements represent one execution and may vary depending on hardware, board position, and move ordering.

## 7. Testing

Seven automated unit tests were executed successfully.

The tests verified:

- Initial board configuration
- Initial legal moves
- Disk flipping and preservation of the original board
- Heuristic symmetry
- AI move legality
- Agreement between Minimax and Alpha-Beta on the initial board
- Game termination on a full board

All seven tests passed in approximately 0.129 seconds.

## 8. Conclusion

The project demonstrates how adversarial search can be applied to a two-player, zero-sum strategy game.

The balanced heuristic considers several strategic characteristics rather than relying solely on disk count. Minimax evaluates potential opponent responses, while Alpha-Beta Pruning reduces unnecessary search.

The resulting application allows a human player to compete against an AI opponent through a graphical Othello interface.
