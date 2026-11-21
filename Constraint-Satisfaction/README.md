# Constraint Satisfaction — Sudoku Solvers

**CS480 | Module 4: Constraint Satisfaction Problems**

This project implements and compares two Python solvers for 9×9 Sudoku:

1. **Naïve backtracking:** fills the first available empty cell, trying digits 1–9 in ascending order.
2. **Smart backtracking:** uses Minimum Remaining Values (MRV), Least Constraining Value (LCV), and Forward Checking (FC) to guide recursive search.

Sudoku is modeled as a **constraint satisfaction problem (CSP)**: each cell is a variable, its domain is the digits 1–9 (restricted by the givens), and the constraints require unique digits within each row, column, and 3×3 box. Empty cells are represented by `0` in Python lists.

## Project files

| File | Description |
| --- | --- |
| `sudoku.py` | Naïve solver, Sudoku validity checks, and board display |
| `smart_sudoku.py` | MRV, LCV, Forward Checking, and smart solver |
| `benchmark.py` | Runs both solvers against Easy, Medium, Hard, and Evil puzzles; measures time, recursive calls, and backtracks |

## Requirements

- Python 3 (standard library only; no third-party packages required)
- Run commands from the directory containing all three Python files.

## Running the programs

```bash
python3 sudoku.py
python3 smart_sudoku.py
python3 benchmark.py
```

The first two commands solve the included demonstration puzzle. The benchmark runs both solvers on four Web Sudoku puzzles and reports their results and performance. Exact timings vary between runs and machines.

## Algorithms

### Naïve backtracking (`solve_naive`)

1. Find the first empty cell in row-major order.
2. Try digits 1–9 in ascending order.
3. Assign a digit if it satisfies row, column, and box constraints.
4. Recurse; if the branch fails, reset the cell to `0` and try the next digit.

### Smart backtracking (`solve_smart`)

1. **MRV:** select the empty cell with the smallest number of legal values.
2. **LCV:** try legal values in order of how few options they remove from neighboring empty cells.
3. **Forward Checking:** after each assignment, verify that every remaining empty cell has at least one legal value; reject branches that fail this check.
4. Recurse or undo the assignment and try another candidate.

The FC implementation recomputes legal domains rather than maintaining incremental domain updates. This simplifies the implementation but adds runtime overhead.

## Benchmark methodology

Both algorithms receive separate copies of the same puzzle. `benchmark.py` uses `time.perf_counter()` and optionally passes a `stats` dictionary to each solver:

- **Time:** wall-clock seconds spent in the solver.
- **Recursive calls:** entries into the recursive solver function, including the successful base case.
- **Backtracks:** tentative assignments that are undone after unsuccessful branches.

The puzzles were transcribed from [Web Sudoku](https://www.websudoku.com/) screenshots:

| Difficulty | Puzzle ID |
| --- | --- |
| Easy | 787419292 |
| Medium | 7903024807 |
| Hard | 1921529445 |
| Evil | 749559569 |

### Recorded results (one benchmark run)

| Difficulty | Naïve time (s) | Smart time (s) | Naïve calls | Smart calls | Naïve backtracks | Smart backtracks |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Easy | 0.001393 | 0.016685 | 218 | 47 | 171 | 0 |
| Medium | 0.007198 | 0.025314 | 1245 | 56 | 1191 | 3 |
| Hard | 0.034405 | 0.164365 | 5528 | 276 | 5473 | 243 |
| Evil | 0.032863 | 0.266907 | 5055 | 448 | 4998 | 420 |

Both solvers returned `True` and produced matching solutions on all four puzzles.

**Interpretation:** the smart solver used far fewer recursive calls and backtracks, but the naïve solver finished faster in these tests. The repeated domain computations for MRV, LCV, and FC cost more time than they saved on this set of puzzles. Human-rated Sudoku difficulty does not necessarily correspond to computational difficulty for either algorithm.

## Limitations and possible improvements

- Four puzzles and one recorded timing per puzzle are not sufficient for broad performance conclusions. Repeat runs and report summary statistics for stronger evidence.
- Domain recomputation is relatively expensive; incremental domains and checking only affected neighbors could improve smart-solver runtime.
- Both solvers stop at the first solution and assume a well-formed puzzle with consistent givens; they do not independently verify uniqueness or fully validate malformed starting boards.
- Equal solutions on the benchmark are a useful consistency check, not a proof that every possible input is handled correctly.

## Assignment coverage

- **Task 1:** Naïve Backtracking Sudoku Solver (`sudoku.py`)
- **Task 2:** Smart Backtracking using MRV, LCV, and FC (`smart_sudoku.py`)
- **Task 3:** Performance comparison across four difficulty levels (`benchmark.py`)

## Source

[Web Sudoku](https://www.websudoku.com/) — source of the four benchmark puzzles.
