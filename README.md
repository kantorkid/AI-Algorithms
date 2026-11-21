
# Artificial Intelligence Algorithms

Python implementations of classical artificial intelligence algorithms, developed for **CS480 — Introduction to Artificial Intelligence** at **Old Dominion University**.

This repository explores how different AI search strategies solve puzzles, optimize objective functions, satisfy constraints, and make decisions in competitive environments. Each project includes its own implementation and documentation.

## Projects

| Project | Algorithms | Application |
|---|---|---|
| Uninformed Search | BFS, DFS, Bidirectional BFS, Bidirectional DFS | 24-Puzzle |
| Informed Search | A*, Iterative Deepening A* (IDA*) | 24-Puzzle |
| Local Search | Hill Climbing, Steepest-Descent Hill Climbing | Eggholder Function, N-Queens |
| Adversarial Search | Minimax, Alpha-Beta Pruning | Othello (Reversi) |
| Constraint Satisfaction | Naïve Backtracking, MRV, LCV, Forward Checking | Sudoku |

---

## 1. Uninformed Search — 24-Puzzle

[Explore project](./Uninformed-Search/)

Solves a 5×5 sliding-tile puzzle containing 24 numbered tiles and one blank space, using search methods that do not rely on heuristic estimates of distance to the goal.

### Algorithms

- **Breadth-First Search (BFS):** Explores states by increasing depth and finds a shortest solution under uniform move costs when the search completes.
- **Depth-First Search (DFS):** Explores paths depth-first, with limits to constrain exploration.
- **Bidirectional BFS:** Searches forward from the initial state and backward from the goal.
- **Bidirectional DFS:** An additional experimental search implementation.

The project includes puzzle-state handling, sample solutions, and a PDF analysis of algorithm behavior and performance.

### Run

```bash
cd Uninformed-Search
python3 sample_solutions.py
```

See the Uninformed Search README and analysis for additional details.

---

## 2. Informed Search — 24-Puzzle

[Explore project](./Informed-Search/)

Applies heuristic-guided search to the 24-puzzle, comparing two algorithms and two admissible heuristics.

### Algorithms

**A* Search**

Prioritizes states using the evaluation function:

\[
f(n) = g(n) + h(n)
\]

Where:
- `g(n)` represents the cost from the initial state.
- `h(n)` estimates the remaining cost to the goal.

**Iterative Deepening A* (IDA*)**

Uses repeated depth-first searches with increasing estimated-cost thresholds, typically reducing memory requirements compared with A*.

### Heuristics

- **Misplaced Tiles:** Counts numbered tiles outside their goal positions.
- **Manhattan Distance:** Sums the horizontal and vertical distances of numbered tiles from their goal positions.

The interactive program accepts custom puzzle configurations, validates input, and reports execution time, explored states, and solution length.

### Run

```bash
cd Informed-Search
python3 main.py
```

See the Informed Search README and analysis for additional details.

---

## 3. Local Search — Eggholder and N-Queens

[Explore project](./Local-Search/)

Investigates how Hill Climbing improves candidate solutions and why greedy optimization can become trapped in local minima.

### Eggholder Function

The Eggholder function is a nonlinear optimization problem with numerous local minima.

The objective is to minimize the function over the domain:

\[
-512 \leq x,y \leq 512
\]

In 100 runs from randomized starting positions, the best observed objective value was **−959.628317**, close to the known global minimum of approximately **−959.640663**.

Other runs converged to less favorable local minima, demonstrating the limitations of greedy optimization.

### N-Queens

Uses Steepest-Descent Hill Climbing to minimize the number of attacking queen pairs on an N×N chessboard.

#### Experimental Results

| Board Size | Successful Runs | Trials | Success Rate |
|---|---:|---:|---:|
| 8 Queens | 11 | 100 | 11% |
| 16 Queens | 2 | 100 | 2% |
| 32 Queens | 1 | 100 | 1% |

The project includes experimental results, an Eggholder outcome distribution, and 30 initial/final N-Queens board visualizations.

### Run

```bash
cd Local-Search
python3 -m pip install matplotlib
python3 eggholder_experiments.py
python3 nqueens_experiments.py
```

See the Local Search README and analysis for additional details.

---

## 4. Adversarial Search — Othello AI

[Explore project](./Adversarial-Search/)

A playable 8×8 Othello (Reversi) game with a Tkinter graphical interface.

The human plays Black against an AI playing White.

### Algorithms

**Minimax**

Evaluates possible future moves by assuming both players make strategically optimal decisions.

**Alpha-Beta Pruning**

Optimizes Minimax by eliminating branches that cannot influence the final decision.

### Evaluation Heuristic

The AI evaluates four strategic factors:

1. **Disk Advantage:** Relative number of pieces controlled.
2. **Positional Advantage:** Value of occupied squares, especially corners.
3. **Frontier Advantage:** Exposure of pieces adjacent to empty squares.
4. **Mobility Advantage:** Number of legal moves available.

### Features

- Interactive Tkinter GUI
- Legal move highlighting
- Automatic disk flipping
- Score tracking
- Pass and game-over detection
- Configurable AI search depth
- Minimax and Alpha-Beta Pruning

The default AI search depth is four.

### Performance

In one opening-position benchmark at depth four:

| Algorithm | Execution Time |
|---|---:|
| Minimax | 0.0707 seconds |
| Alpha-Beta Pruning | 0.0286 seconds |

Both algorithms selected the same move.

These timings are illustrative and depend on the machine and board state.

### Run

```bash
cd Adversarial-Search
python3 gui.py
```

### Tests

```bash
python3 test_othello.py -v
```

Eight initial unit tests passed, covering game rules, heuristic symmetry, move selection, algorithm agreement, and pass/game-over conditions.

See the Othello README and design document for additional details.

---

## 5. Constraint Satisfaction — Sudoku

[Explore project](./Constraint-Satisfaction/)

Implements and compares two Sudoku-solving algorithms using Constraint Satisfaction Problem (CSP) techniques.

Sudoku is modeled as a CSP consisting of:

- **Variables:** 81 cells in a 9×9 grid.
- **Domains:** Digits 1 through 9 for each unassigned cell.
- **Constraints:** Each row, column, and 3×3 subgrid must contain unique digits.

The objective is to solve Sudoku puzzles while comparing basic recursive backtracking against a heuristic-guided approach.

### Task 1: Naïve Backtracking

The naïve solver uses recursive depth-first search to assign values to empty Sudoku cells.

Algorithm:

1. Find the first empty cell, scanning row by row.
2. Try digits 1 through 9 in ascending order.
3. Check whether each assignment satisfies Sudoku constraints.
4. Recursively continue with valid assignments.
5. Undo assignments when a branch fails.

This approach requires no advanced variable or value ordering heuristics.

**Implementation:** `sudoku.py`

### Task 2: Smart Backtracking

The smart solver improves search efficiency using three CSP techniques.

**Minimum Remaining Values (MRV)**

Selects the unassigned cell with the fewest legal values, prioritizing the most constrained variables.

**Least Constraining Value (LCV)**

Orders candidate values according to how few possibilities they eliminate from neighboring cells.

**Forward Checking (FC)**

Checks the remaining unassigned cells after each tentative assignment. If any cell has no legal values remaining, the current branch is rejected.

The implementation recomputes legal domains rather than maintaining them incrementally.

**Implementation:** `smart_sudoku.py`

### Task 3: Performance Analysis

Both algorithms were evaluated using four puzzles from [Web Sudoku](https://www.websudoku.com/).

The difficulty levels were Easy, Medium, Hard, and Evil.

Each algorithm received an independent copy of the same starting puzzle.

#### Execution Time

| Difficulty | Naïve Backtracking | Smart Backtracking |
|---|---:|---:|
| Easy | 0.001393 s | 0.016685 s |
| Medium | 0.007198 s | 0.025314 s |
| Hard | 0.034405 s | 0.164365 s |
| Evil | 0.032863 s | 0.266907 s |

#### Recursive Calls

| Difficulty | Naïve Backtracking | Smart Backtracking | Reduction |
|---|---:|---:|---:|
| Easy | 218 | 47 | 78.4% |
| Medium | 1,245 | 56 | 95.5% |
| Hard | 5,528 | 276 | 95.0% |
| Evil | 5,055 | 448 | 91.1% |

#### Backtracking Operations

| Difficulty | Naïve Backtracking | Smart Backtracking |
|---|---:|---:|
| Easy | 171 | 0 |
| Medium | 1,191 | 3 |
| Hard | 5,473 | 243 |
| Evil | 4,998 | 420 |

### Results and Discussion

Both algorithms successfully solved all four puzzles and produced matching solutions.

**Smart Backtracking substantially reduced search effort.**

MRV, LCV, and Forward Checking reduced the number of recursive calls by approximately 78%–96% across the four difficulty levels.

The smart algorithm also performed fewer backtracking operations on every puzzle.

However, **Naïve Backtracking executed faster on all four puzzles**.

This result demonstrates the computational overhead introduced by the smart solver's heuristics.

MRV repeatedly calculates legal domains, LCV evaluates the impact of candidate assignments on neighboring cells, and Forward Checking verifies that remaining cells have legal values.

Although these techniques reduce the number of search states explored, the additional calculations can outweigh the savings in execution time for these particular puzzles.

The Evil puzzle also required fewer recursive calls than the Hard puzzle for the naïve solver, demonstrating that human-assigned difficulty levels do not necessarily predict computational difficulty.

These results illustrate an important distinction between **search efficiency** and **wall-clock execution time**.

### Limitations and Future Improvements

- Only four puzzles were evaluated.
- The reported timings represent individual benchmark measurements.
- Execution times depend on hardware, Python runtime, and implementation details.
- Incremental domain tracking could reduce repeated calculations.
- Additional puzzles and repeated benchmark runs would improve the reliability of performance comparisons.
- Constraint propagation and other CSP optimizations could further improve performance.

### Run

Navigate to the project directory:

```bash
cd Constraint-Satisfaction
```

Run Naïve Backtracking:

```bash
python3 sudoku.py
```

Run Smart Backtracking:

```bash
python3 smart_sudoku.py
```

Run the performance comparison:

```bash
python3 benchmark.py
```

All three programs use Python's standard library and require no additional packages.

See the Constraint Satisfaction README for implementation details and additional documentation.

---

## Repository Structure

```text
AI-Algorithms/
├── README.md
├── .gitignore
│
├── Uninformed-Search/
│   └── ... BFS, DFS, Bidirectional Search, 24-Puzzle
│
├── Informed-Search/
│   └── ... A*, IDA*, Heuristics, 24-Puzzle
│
├── Local-Search/
│   └── ... Eggholder, N-Queens, Hill Climbing
│
├── Adversarial-Search/
│   └── ... Othello, Minimax, Alpha-Beta, Tkinter
│
└── Constraint-Satisfaction/
    ├── README.md
    ├── sudoku.py
    ├── smart_sudoku.py
    └── benchmark.py
```

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/kantorkid/AI-Algorithms.git
cd AI-Algorithms
```

### Requirements

- Python 3
- Matplotlib for Local Search visualizations
- Tkinter for the Othello graphical interface

The Uninformed Search, Informed Search, and Constraint Satisfaction implementations use Python's standard library.

Refer to each project's README for additional setup and execution instructions.

---

## Concepts Demonstrated

This repository explores the following artificial intelligence concepts:

- State-space representation and exploration
- Breadth-First Search and Depth-First Search
- Bidirectional search
- Completeness and optimality
- Time and memory complexity
- Heuristic design and informed search
- A* and Iterative Deepening A*
- Local optimization and Hill Climbing
- Local minima and objective functions
- Adversarial decision-making with Minimax
- Alpha-Beta Pruning
- Constraint Satisfaction Problems (CSPs)
- Recursive backtracking
- Minimum Remaining Values (MRV)
- Least Constraining Value (LCV)
- Forward Checking and constraint propagation
- Search-space reduction
- Performance benchmarking and algorithm comparison
- Automated testing and experimental analysis

---

## Author

**Jake Kantor**

M.S. Cybersecurity — AI Security Concentration  
Old Dominion University

[Portfolio](https://jakekantor.io) | [GitHub](https://github.com/kantorkid)

---

## License

No license has been specified for this repository.
