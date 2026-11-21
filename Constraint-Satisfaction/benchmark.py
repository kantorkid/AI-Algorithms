
"""
CS480 Module 4 - Constraint Satisfaction Problems

Task 3: Sudoku Performance Analysis

Compare Naive Backtracking and Smart Backtracking.
"""

import time

from sudoku import solve_naive
from smart_sudoku import solve_smart



def benchmark_solver(solver, puzzle):
    """
    Measure execution time, recursive calls,
    and backtracking operations.
    """

    board = [row[:] for row in puzzle]

    stats = {
        "calls": 0,
        "backtracks": 0
    }

    start_time = time.perf_counter()

    solved = solver(board, stats)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    return solved, elapsed_time, board, stats



if __name__ == "__main__":

    puzzles = {
        "Easy": [
            [1, 8, 5, 0, 0, 6, 4, 3, 9],
            [0, 0, 0, 5, 0, 0, 2, 0, 0],
            [0, 7, 4, 3, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 8, 0, 9, 0],
            [4, 2, 0, 0, 1, 0, 0, 6, 5],
            [0, 9, 0, 7, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 0, 9, 6, 7, 0],
            [0, 0, 8, 0, 0, 5, 0, 0, 0],
            [9, 1, 2, 6, 0, 0, 3, 5, 8]
        ],

        "Medium": [
            [7, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 4, 9, 1, 0, 0, 7],
            [0, 0, 4, 0, 0, 0, 6, 0, 2],
            [0, 0, 0, 0, 6, 0, 0, 7, 3],
            [0, 3, 8, 0, 0, 0, 9, 1, 0],
            [6, 1, 0, 0, 2, 0, 0, 0, 0],
            [4, 0, 2, 0, 0, 0, 8, 0, 0],
            [8, 0, 0, 2, 7, 3, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 5]
        ],

        "Hard": [
            [1, 0, 0, 0, 8, 0, 0, 9, 0],
            [0, 0, 0, 0, 0, 3, 5, 0, 0],
            [0, 0, 4, 6, 0, 9, 1, 0, 0],
            [8, 0, 0, 0, 9, 0, 0, 2, 0],
            [0, 7, 0, 0, 4, 0, 0, 8, 0],
            [0, 6, 0, 0, 3, 0, 0, 0, 4],
            [0, 0, 3, 9, 0, 8, 7, 0, 0],
            [0, 0, 8, 3, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 6, 0, 0, 0, 1]
        ],

        "Evil": [
            [2, 8, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 7, 2, 0, 0, 0, 0],
            [4, 6, 0, 0, 0, 1, 0, 0, 0],
            [8, 0, 0, 0, 0, 4, 1, 0, 0],
            [0, 0, 3, 0, 1, 0, 6, 0, 0],
            [0, 0, 5, 6, 0, 0, 0, 0, 2],
            [0, 0, 0, 1, 0, 0, 0, 4, 5],
            [0, 0, 0, 0, 3, 2, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 6, 8]
        ]
    }


    
    print("Sudoku Performance Comparison\n")


    for difficulty, puzzle in puzzles.items():

        print(f"\nDifficulty: {difficulty}")

        naive_solved, naive_time, naive_board, naive_stats = benchmark_solver(
            solve_naive, puzzle
        )

        smart_solved, smart_time, smart_board, smart_stats = benchmark_solver(
            solve_smart, puzzle
        )

        print("\nNaive Backtracking:")
        print(f"  Time: {naive_time:.6f} seconds")
        print(f"  Recursive calls: {naive_stats['calls']}")
        print(f"  Backtracks: {naive_stats['backtracks']}")

        print("\nSmart Backtracking:")
        print(f"  Time: {smart_time:.6f} seconds")
        print(f"  Recursive calls: {smart_stats['calls']}")
        print(f"  Backtracks: {smart_stats['backtracks']}")

        print(f"\nNaive solved: {naive_solved}")
        print(f"Smart solved: {smart_solved}")
        print(f"Solutions match: {naive_board == smart_board}")

        print("-" * 45)

