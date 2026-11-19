# 24-Puzzle Informed Search

**CS480 — Introduction to Artificial Intelligence**

## Overview

This project implements informed search algorithms to solve the 24-puzzle, a 5×5 sliding-tile puzzle containing 24 numbered tiles and one blank space.

The objective is to rearrange the tiles into ascending numerical order, with the blank tile (`0`) positioned in the bottom-right corner.

The project compares two informed search algorithms, A* and Iterative Deepening A* (IDA*), using two admissible heuristics: Misplaced Tiles and Manhattan Distance.

The implementation supports arbitrary puzzle configurations, validates input, prevents repeated states along a solution path, and measures search performance through execution time, states explored, and solution length.

## Goal Configuration

```text
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24  0
```

The blank tile can move up, down, left, or right, provided the movement remains within the puzzle boundaries.

## Search Algorithms

### A* Search

A* is a best-first search algorithm that uses a priority queue to explore states according to their estimated total cost.

The evaluation function is:

**f(n) = g(n) + h(n)**

Where:

- `g(n)` represents the number of moves from the initial state to the current state.
- `h(n)` represents the estimated number of moves remaining to reach the goal.
- `f(n)` represents the estimated total solution cost through the current state.

A* prioritizes states with the lowest estimated total cost. With an admissible heuristic and unit move costs, A* guarantees an optimal solution when the search completes successfully.

A* maintains discovered states and their associated costs, which can result in substantial memory consumption for large search spaces.

### Iterative Deepening A* (IDA*)

IDA* combines heuristic evaluation with iterative deepening depth-first search.

Rather than maintaining a large priority queue, IDA* performs repeated depth-first searches using increasing `f(n)` thresholds.

States exceeding the current threshold are pruned, and the threshold increases until a solution is found or the exploration limit is reached.

IDA* generally requires less memory than A*, although it may revisit states during successive iterations.

## Heuristics

Two admissible heuristics were implemented to estimate the remaining cost of reaching the goal.

### h1 — Misplaced Tiles

The Misplaced Tiles heuristic counts the numbered tiles that are not in their correct goal positions.

**h1(n) = Number of misplaced tiles**

For example, if five numbered tiles are not in their correct positions, the heuristic value is 5.

The blank tile is excluded from the calculation.

This heuristic is computationally inexpensive but does not account for how far individual tiles are from their goal positions.

### h2 — Manhattan Distance

The Manhattan Distance heuristic calculates the total horizontal and vertical distance between each numbered tile's current position and its goal position.

**h2(n) = Σ (|current row − goal row| + |current column − goal column|)**

The blank tile is excluded from the calculation.

Manhattan Distance generally provides a more informative estimate because it accounts for the minimum number of horizontal and vertical movements required to position each tile correctly, ignoring interactions between tiles.

For the standard sliding-tile puzzle, Manhattan Distance is at least as informative as Misplaced Tiles.

## Project Structure

```text
Informed-Search/
├── README.md
├── main.py
├── puzzle.py
├── heuristics.py
├── astar.py
├── ida_star.py
├── input_handler.py
├── generate_puzzle.py
├── sample_solutions.py
├── sample_solutions.txt
└── CS480_Informed_Search_Analysis.pdf
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Interactive program for selecting algorithms, heuristics, and puzzle configurations |
| `puzzle.py` | Defines puzzle states, valid movements, successor generation, and solvability checks |
| `heuristics.py` | Implements Misplaced Tiles and Manhattan Distance |
| `astar.py` | Implements A* search using a priority queue |
| `ida_star.py` | Implements Iterative Deepening A* search |
| `input_handler.py` | Validates user-provided puzzle configurations |
| `generate_puzzle.py` | Generates reproducible solvable puzzles using legal moves from the goal |
| `sample_solutions.py` | Executes automated tests across multiple puzzle configurations |
| `sample_solutions.txt` | Contains generated solution paths, execution times, and search statistics |
| `CS480_Informed_Search_Analysis.pdf` | Separate assignment analysis report |

## Requirements

- Python 3
- Python standard library

No third-party packages are required.

## Running the Program

Navigate to the `Informed-Search` directory.

```bash
cd Informed-Search
```

Run the interactive program:

```bash
python3 main.py
```

The program prompts the user to:

1. Enter a puzzle configuration or press Enter to use the original assignment puzzle.
2. Select A* or IDA*.
3. Select Misplaced Tiles or Manhattan Distance.

### Custom Puzzle Input

Enter 25 integers from `0` through `24`, separated by spaces.

Example:

```text
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 0 23 24
```

The program verifies that:

- Exactly 25 integers are provided.
- Every integer from 0 through 24 appears exactly once.
- The configuration satisfies the solvability condition for the 5×5 puzzle.

### Program Output

For successful searches, the program displays:

- Selected algorithm and heuristic
- Solution path, including intermediate configurations
- Solution length in moves
- Number of states explored
- Execution time

Searches that exceed the exploration limit are reported without claiming a solution was found.

## Generating Test Puzzles

The project includes a puzzle generator that creates solvable configurations by applying legal moves to the goal state.

Run:

```bash
python3 generate_puzzle.py
```

By default, the generator performs 20 legal moves using a fixed random seed.

The resulting configuration is reproducible and guaranteed to be solvable.

However, the number of moves used to generate a puzzle does not necessarily equal its optimal solution length.

## Automated Testing

Run:

```bash
python3 sample_solutions.py
```

The testing script evaluates four puzzle configurations using both search algorithms and both heuristics.

The configurations are:

1. Two-move puzzle
2. Four-move puzzle
3. Twenty-move scramble
4. Original assignment puzzle

Each configuration is tested with:

- A* using Misplaced Tiles
- A* using Manhattan Distance
- IDA* using Misplaced Tiles
- IDA* using Manhattan Distance

The results are saved to `sample_solutions.txt`, including the full solution paths for successful searches.

## Experimental Results

### Solution Length Comparison

| Puzzle Configuration | A* h1 | A* h2 | IDA* h1 | IDA* h2 |
|---|---:|---:|---:|---:|
| Two-move puzzle | 2 | 2 | 2 | 2 |
| Four-move puzzle | 4 | 4 | 4 | 4 |
| Twenty-move scramble | 20 | 20 | 20 | 20 |
| Original assignment | N/A | N/A | N/A | N/A |

All four algorithm–heuristic combinations found optimal solutions for the first three configurations.

The original assignment puzzle exceeded the exploration limit of 1,000,000 states in all four tests.

### Twenty-Move Scramble

The generated puzzle configuration was:

```text
 1  2  8 10  3
 6  7  4  9  5
11 12 13 14  0
16 17 24 19 15
21 22 18 23 20
```

Initial heuristic values:

- Misplaced Tiles: 10
- Manhattan Distance: 14

#### Performance Results

| Algorithm | Heuristic | States Explored | Execution Time | Solution Length |
|---|---|---:|---:|---:|
| A* | Misplaced Tiles | 2,017 | 0.021552 s | 20 |
| A* | Manhattan Distance | 245 | 0.004603 s | 20 |
| IDA* | Misplaced Tiles | 3,347 | 0.029305 s | 20 |
| IDA* | Manhattan Distance | 173 | 0.003072 s | 20 |

#### Heuristic Comparison

Manhattan Distance substantially reduced the number of explored states compared with Misplaced Tiles.

For A*:

- Misplaced Tiles explored 2,017 states.
- Manhattan Distance explored 245 states.
- Manhattan Distance reduced exploration by approximately **87.9%**.

For IDA*:

- Misplaced Tiles explored 3,347 states.
- Manhattan Distance explored 173 states.
- Manhattan Distance reduced exploration by approximately **94.8%**.

Both algorithms also completed the search faster using Manhattan Distance.

These results demonstrate the advantage of a more informative heuristic when solving moderately challenging puzzle configurations.

### Original Assignment Puzzle

The original assignment configuration was:

```text
 3 17  9  5 21
11  0 13 19 10
 6 24 22  1 20
16 14  4 12 15
18  8 23  2  7
```

#### Performance Results

| Algorithm | Heuristic | States Explored | Execution Time | Result |
|---|---|---:|---:|---|
| A* | Misplaced Tiles | 1,000,000 | 13.912622 s | Limit reached |
| A* | Manhattan Distance | 1,000,000 | 20.264997 s | Limit reached |
| IDA* | Misplaced Tiles | 1,000,000 | 9.321958 s | Limit reached |
| IDA* | Manhattan Distance | 1,000,000 | 16.580842 s | Limit reached |

The original configuration passed the solvability check, but none of the four searches found a solution within the exploration limit.

The solution length therefore remains undetermined.

## Performance Analysis

### Heuristic Effectiveness

The two-move and four-move puzzles were relatively simple, resulting in similar performance for both heuristics.

The twenty-move scramble provided a more meaningful comparison.

Manhattan Distance explored significantly fewer states and achieved lower execution times than Misplaced Tiles with both A* and IDA*.

This occurred because Manhattan Distance incorporates positional information that Misplaced Tiles does not capture.

Although calculating Manhattan Distance requires additional arithmetic, the reduction in unnecessary state exploration outweighed that computational overhead for the twenty-move puzzle.

### Algorithm Comparison

A* maintains a priority queue and records the best known cost for discovered states.

IDA* uses repeated depth-first searches with increasing evaluation thresholds and maintains the current search path.

For the twenty-move scramble, IDA* with Manhattan Distance explored the fewest states and achieved the lowest measured execution time.

However, the number of states explored by A* and IDA* should be interpreted carefully because IDA* may revisit states across successive iterations.

### Computational Limitations

The original assignment puzzle demonstrated the computational difficulty of solving complex 24-puzzle configurations.

The 24-puzzle has an extremely large state space, making exhaustive exploration impractical.

All four search combinations reached the configured exploration limit without finding a solution.

This does not mean the original puzzle is unsolvable. It indicates that the implemented algorithms and heuristics did not find a solution within the available search budget.

## Limitations

The implementation has several limitations:

- Search is restricted to a maximum of 1,000,000 explored states per run.
- A* can consume substantial memory because it maintains a frontier and discovered-state information.
- IDA* may revisit states across iterations.
- The implemented heuristics do not account for all interactions between tiles.
- Execution times depend on system hardware and runtime conditions.
- The original assignment configuration was not solved within the configured exploration limit.

More advanced techniques, including stronger admissible heuristics, pattern databases, and optimized state representations, could improve performance on difficult configurations.

## Conclusion

This project implemented and evaluated A* and IDA* informed search algorithms using Misplaced Tiles and Manhattan Distance heuristics.

Both algorithms successfully solved the two-move, four-move, and twenty-move configurations using both heuristics.

The twenty-move experiment demonstrated that Manhattan Distance significantly improves search efficiency, reducing explored states by approximately 87.9% for A* and 94.8% for IDA* compared with Misplaced Tiles.

The original assignment configuration remained unsolved within the one-million-state exploration limit, illustrating the computational challenges associated with large state spaces.

Overall, the experiments demonstrate the importance of heuristic quality, search strategy, memory efficiency, and computational constraints in informed search algorithms.