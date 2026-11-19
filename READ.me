# CS480 Module 3 — Uninformed Search

## Overview

This project implements uninformed search algorithms for the 24-puzzle, a 5×5 sliding puzzle containing 24 numbered tiles and one blank space (represented by 0).

The two required algorithms are:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Two additional algorithms were implemented for experimentation:

- Bidirectional Breadth-First Search
- Bidirectional Depth-First Search

The objective is to transform the initial puzzle configuration into the goal configuration by moving the blank space up, down, left, or right.

## Initial State

```text
 9 24  3  5 17
 6  0 13 19 10
11 21 22  1 20
16  4 14 12 15
 8 18 23  2  7
```

## Goal State

```text
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24  0
```

## Project Files

| File | Description |
|---|---|
| `puzzle.py` | Defines the initial and goal states, movement functions, and solvability check. |
| `bfs.py` | Implements breadth-first search using a FIFO queue. |
| `dfs.py` | Implements depth-limited depth-first search using a LIFO stack. |
| `bidirectional_bfs.py` | Performs BFS from the initial and goal states simultaneously. |
| `bidirectional_dfs.py` | Experimental bidirectional depth-first search implementation. |
| `sample_solutions.py` | Runs BFS and DFS on a simplified, solvable 24-puzzle configuration. |
| `sample_solutions.txt` | Contains successful solution paths and performance results. |
| `CS480_Uninformed_Search_Analysis.pdf` | Documents the implementation, experimental results, and analysis. |

## Requirements

- Python 3
- No external dependencies

The project uses Python's standard library.

## Running the Programs

Open a terminal in the project directory.

**Breadth-First Search**

```bash
python3 bfs.py
```

**Depth-First Search**

```bash
python3 dfs.py
```

**Bidirectional BFS**

```bash
python3 bidirectional_bfs.py
```

**Bidirectional DFS**

```bash
python3 bidirectional_dfs.py
```

**Successful BFS and DFS Sample Solutions**

```bash
python3 sample_solutions.py
```

To save the sample solutions to a text file:

```bash
python3 sample_solutions.py > sample_solutions.txt
```

## Algorithm Implementations

### Breadth-First Search (BFS)

BFS explores states in order of increasing depth using a FIFO queue.

A visited-state set prevents duplicate exploration, while a parent dictionary allows reconstruction of the solution path.

BFS finds a shortest solution when the search completes successfully because every move has equal cost.

### Depth-First Search (DFS)

DFS explores paths using a LIFO stack.

The implementation avoids revisiting configurations already present in the current solution path.

A maximum depth of 30 and a state limit of 1,000,000 were used for the original configuration.

DFS does not guarantee the shortest solution.

### Bidirectional BFS

Bidirectional BFS searches from the initial configuration and the goal configuration.

The implementation expands the smaller frontier and checks whether the two searches intersect.

It can reduce the search effort compared with conventional BFS, although the implemented stopping strategy does not independently guarantee a shortest solution.

### Bidirectional DFS

Bidirectional DFS explores the puzzle from both directions using LIFO stacks.

Each search has a maximum depth of 30.

This experimental implementation uses global visited-state tracking, which can prevent revisiting states through shallower paths. Therefore, it is not guaranteed to find every solution within its configured depth limits.

## Successful Sample Solutions

To demonstrate that BFS and DFS can successfully solve the puzzle, both algorithms were tested on a configuration two moves away from the goal.

**Sample Initial State**

```text
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22  0 23 24
```

**Sample Results**

| Metric | BFS | DFS |
|---|---|---|
| Solution found | Yes | Yes |
| Solution length | 2 moves | 2 moves |
| States explored | 11 | 3 |
| Execution time | 0.000064 seconds | 0.000015 seconds |

Both algorithms produced the same solution:

1. Move the blank space right.
2. Move the blank space right again.

DFS was limited to a maximum depth of 2 for this sample test.

The complete solution paths are provided in `sample_solutions.txt`.

## Original 24-Puzzle Results

The algorithms were also tested against the original initial configuration specified in the assignment.

| Algorithm | States Explored | Execution Time | Solution Found |
|---|---|---|---|
| BFS | 1,000,000 | 5.601 seconds | No |
| DFS | 1,000,000 | 2.822 seconds | No |
| Bidirectional BFS | 10,000,000 | 98.988 seconds | No |
| Bidirectional DFS | 1,000,000 | 2.314 seconds | No |

All four searches reached their configured state limits without finding a solution.

The original configuration passed the solvability parity check, but the algorithms did not reach the goal within the tested resource limits.

## Computational Analysis

The 24-puzzle has a very large state space, making uninformed search computationally expensive.

BFS systematically explores configurations by depth but requires substantial memory to maintain its frontier and visited states.

DFS generally requires less search-frontier memory, but it can spend considerable time exploring paths that do not lead to the goal. The implementation also stores the current path for each frontier entry.

Bidirectional BFS attempts to reduce the search space by searching from both ends. However, even after exploring 10 million states, it did not find a solution to the original configuration.

Bidirectional DFS completed its one-million-state experiment faster than the other tested algorithms at the same state limit, but execution time alone does not establish overall algorithm superiority.

The results demonstrate the limitations of uninformed search for large, heavily scrambled sliding puzzles.

## Conclusion

BFS and DFS were successfully implemented and validated using a two-move 24-puzzle test configuration.

Both algorithms found valid solutions without repeating states in their returned paths.

Neither algorithm solved the original assignment configuration within the imposed search limits.

The additional bidirectional experiments further demonstrated the computational challenges associated with uninformed search.

For a more detailed discussion, see `CS480_Uninformed_Search_Analysis.pdf`.