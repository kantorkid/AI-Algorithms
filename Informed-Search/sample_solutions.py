
import time

from puzzle import INITIAL_STATE, GOAL_STATE
from heuristics import misplaced_tiles, manhattan_distance
from astar import astar
from ida_star import ida_star


SAMPLE_STATES = {
    "2-Move Puzzle": (
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 0, 23, 24
    ),

    "4-Move Puzzle": (
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        0, 21, 22, 23, 24
    ),

    "20-Move Scramble": (
    1, 2, 8, 10, 3,
    6, 7, 4, 9, 5,
    11, 12, 13, 14, 0,
    16, 17, 24, 19, 15,
    21, 22, 18, 23, 20
    ),

    "Assignment Puzzle": INITIAL_STATE
}


ALGORITHMS = {
    "A*": astar,
    "IDA*": ida_star
}

HEURISTICS = {
    "h1 - Misplaced Tiles": misplaced_tiles,
    "h2 - Manhattan Distance": manhattan_distance
}


def format_state(state):
    rows = []

    for i in range(0, 25, 5):
        row = " ".join(f"{tile:2}" for tile in state[i:i + 5])
        rows.append(row)

    return "\n".join(rows)


def run_tests():
    results = []

    for puzzle_name, initial_state in SAMPLE_STATES.items():
        results.append("=" * 60)
        results.append(puzzle_name)
        results.append("=" * 60)

        results.append("\nInitial State:")
        results.append(format_state(initial_state))

        for algorithm_name, algorithm in ALGORITHMS.items():
            for heuristic_name, heuristic in HEURISTICS.items():

                start_time = time.perf_counter()

                solution, states_explored = algorithm(
                    initial_state,
                    heuristic,
                    max_states=1000000
                )

                elapsed_time = time.perf_counter() - start_time

                results.append(
                    f"\nAlgorithm: {algorithm_name}"
                    f"\nHeuristic: {heuristic_name}"
                )

                if solution is not None:
                    results.append("Result: Solution found")
                    results.append(
                        f"Solution Length: {len(solution) - 1} moves"
                    )

                    results.append("Solution Path:")

                    for step, state in enumerate(solution):
                        results.append(f"\nStep {step}:")
                        results.append(format_state(state))

                else:
                    results.append("Result: Search limit reached")
                    results.append("Solution Length: N/A")

                results.append(
                    f"States Explored: {states_explored}"
                )
                results.append(
                    f"Execution Time: {elapsed_time:.6f} seconds"
                )

        results.append("\n")

    output = "\n".join(results)

    with open("sample_solutions.txt", "w") as file:
        file.write(output)

    print(output)
    print("\nResults saved to sample_solutions.txt")


if __name__ == "__main__":
    run_tests()
