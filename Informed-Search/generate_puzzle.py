
import random

from puzzle import GOAL_STATE, get_neighbors, print_puzzle
from heuristics import misplaced_tiles, manhattan_distance


def generate_puzzle(moves=20, seed=42):
    random.seed(seed)

    state = GOAL_STATE
    previous_state = None

    for _ in range(moves):
        neighbors = get_neighbors(state)

        # Avoid immediately reversing the previous move
        if previous_state is not None:
            neighbors = [
                neighbor for neighbor in neighbors
                if neighbor != previous_state
            ]

        next_state = random.choice(neighbors)

        previous_state = state
        state = next_state

    return state


if __name__ == "__main__":
    puzzle = generate_puzzle()

    print("Generated 24-Puzzle:")
    print_puzzle(puzzle)

    print("Misplaced Tiles:", misplaced_tiles(puzzle))
    print("Manhattan Distance:", manhattan_distance(puzzle))
    print("Generated using 20 moves from the goal.")
