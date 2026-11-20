# Artificial Intelligence Algorithms

Python implementations of classical artificial intelligence search algorithms, developed for **CS480 — Introduction to Artificial Intelligence** at Old Dominion University.

This repository explores how different search strategies solve puzzles, optimize objective functions, and make decisions in competitive environments. Each project includes its own implementation and documentation.

## Projects

| Project | Algorithms | Application |
|---|---|---|
| [Uninformed Search](./Uninformed-Search/) | Breadth-First Search (BFS), Depth-First Search (DFS), Bidirectional BFS, Bidirectional DFS | 24-Puzzle |
| [Informed Search](./Informed-Search/) | A*, Iterative Deepening A* (IDA*) | 24-Puzzle |
| [Local Search](./Local-Search/) | Hill Climbing, steepest-descent Hill Climbing | Eggholder function, N-Queens |
| [Adversarial Search](./Adversarial-Search/) | Minimax, Alpha-Beta Pruning | Othello (Reversi) |

## 1. Uninformed Search — 24-Puzzle

**[Explore project](./Uninformed-Search/)**

Solves a 5×5 sliding-tile puzzle containing 24 numbered tiles and one blank space, using search methods that do not rely on a heuristic estimate of distance to the goal.

- **BFS:** Explores states by increasing depth; finds a shortest solution when search completes under uniform move costs.
- **DFS:** Explores paths depth-first, with limits to constrain exploration.
- **Bidirectional BFS:** Searches forward from the start and backward from the goal.
- **Bidirectional DFS:** An additional experimental search implementation.

The project includes puzzle-state handling, sample solutions, and a PDF analysis of algorithm behavior and performance.

**Try it:**

```bash
cd Uninformed-Search
python3 sample_solutions.py
```

See the [Uninformed Search README](./Uninformed-Search/README.md) and [analysis](./Uninformed-Search/CS480_Uninformed_Search_Analysis.pdf).

## 2. Informed Search — 24-Puzzle

**[Explore project](./Informed-Search/)**

Applies heuristic-guided search to the same 24-puzzle, comparing two algorithms and two admissible heuristics.

**Algorithms**
- **A\*:** Prioritizes states using `f(n) = g(n) + h(n)`.
- **IDA\*:** Uses repeated depth-first searches with increasing estimated-cost thresholds, typically reducing memory usage relative to A*.

**Heuristics**
- **Misplaced Tiles:** Counts numbered tiles outside their goal positions.
- **Manhattan Distance:** Sums the horizontal and vertical distances of numbered tiles from their goal positions.

The interactive program accepts custom configurations, validates input, and reports search metrics such as execution time, explored states, and solution length.

**Try it:**

```bash
cd Informed-Search
python3 main.py
```

See the [Informed Search README](./Informed-Search/README.md) and [analysis](./Informed-Search/CS480_Informed_Search_Analysis.pdf).

## 3. Local Search — Eggholder and N-Queens

**[Explore project](./Local-Search/)**

Investigates how Hill Climbing improves candidate solutions and why greedy optimization can become trapped in local minima.

### Eggholder Function

Minimizes a nonlinear function over `[-512, 512]` in each dimension. In 100 runs from randomized starting positions, the best observed objective value was **−959.628317**, close to the known global minimum of approximately **−959.640663**. Other runs converged to less favorable local minima.

### N-Queens

Uses steepest-descent Hill Climbing to reduce the number of attacking queen pairs on an N×N chessboard.

| Board size | Successful runs | Trials | Success rate |
|---|---:|---:|---:|
| 8 queens | 11 | 100 | 11% |
| 16 queens | 2 | 100 | 2% |
| 32 queens | 1 | 100 | 1% |

The project includes experimental results, an Eggholder outcome distribution, and 30 initial/final N-Queens board visualizations.

**Try it:**

```bash
cd Local-Search
python3 -m pip install matplotlib
python3 eggholder_experiments.py
python3 nqueens_experiments.py
```

See the [Local Search README](./Local-Search/README.md) and [analysis](./Local-Search/analysis.md).

## 4. Adversarial Search — Othello AI

**[Explore project](./Adversarial-Search/)**

A playable 8×8 Othello (Reversi) game with a **Tkinter** interface. The human plays Black against an AI playing White.

The AI implements both **Minimax** and **Alpha-Beta Pruning**. Its heuristic evaluates four strategic factors:

- **Disk advantage:** Relative number of pieces controlled.
- **Positional advantage:** Value of occupied squares, especially corners.
- **Frontier advantage:** Exposure of pieces adjacent to empty squares.
- **Mobility advantage:** Number of legal moves available.

The interface highlights legal moves, flips captured disks, handles passes, updates scores, and announces the winner. The default AI search depth is four.

In one opening-position benchmark at depth four, Minimax took **0.0707 s** and Alpha-Beta took **0.0286 s**, selecting the same move. These timings are illustrative and depend on the machine and board state.

**Play the game:**

```bash
cd Adversarial-Search
python3 gui.py
```

**Run automated tests:**

```bash
python3 test_othello.py -v
```

Eight initial unit tests passed, covering rules, heuristic symmetry, move selection, algorithm agreement on the opening board, and pass/game-over conditions.

See the [Othello README](./Adversarial-Search/README.md) and [design document](./Adversarial-Search/DESIGN.md).

## Repository Structure

```text
AI-Algorithms/
├── README.md
├── Uninformed-Search/       # BFS, DFS, bidirectional search, 24-puzzle
├── Informed-Search/         # A*, IDA*, heuristics, 24-puzzle
├── Local-Search/            # Eggholder, N-Queens, Hill Climbing
└── Adversarial-Search/      # Othello, Minimax, Alpha-Beta, Tkinter
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/kantorkid/AI-Algorithms.git
cd AI-Algorithms
```

The projects use **Python 3**. Uninformed and Informed Search use Python's standard library; Local Search uses **Matplotlib** for visualization; and the Othello GUI requires a Python installation with **Tkinter** support. Refer to each project's README for details.

## Concepts Demonstrated

- State-space representation and exploration
- Completeness, optimality, time, and memory tradeoffs
- Heuristic design and informed search
- Local minima and optimization through neighborhood search
- Adversarial decision-making with Minimax
- Search-space reduction through Alpha-Beta Pruning
- Experimentation, performance measurement, and automated testing

## Author

**Jake Kantor**  
M.S. Cybersecurity — AI Security Concentration, Old Dominion University  
[Portfolio](https://jakekantor.io) · [GitHub](https://github.com/kantorkid)
