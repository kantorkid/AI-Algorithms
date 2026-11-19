
from puzzle import INITIAL_STATE, is_solvable, print_puzzle


def get_puzzle_input():
    print("24-Puzzle Input")
    print("Enter 25 numbers from 0 to 24.")
    print("Use 0 to represent the blank tile.")
    print("Separate numbers with spaces.")
    print("Press Enter to use the assignment's initial state.\n")

    user_input = input("Puzzle: ").strip()

    if not user_input:
        return INITIAL_STATE

    try:
        state = tuple(int(value) for value in user_input.split())
    except ValueError:
        raise ValueError("All puzzle values must be integers.")

    if len(state) != 25:
        raise ValueError("The puzzle must contain exactly 25 numbers.")

    if set(state) != set(range(25)):
        raise ValueError("The puzzle must contain each number from 0 to 24 exactly once.")

    if not is_solvable(state):
        raise ValueError("This puzzle configuration is not solvable.")

    return state


if __name__ == "__main__":
    try:
        state = get_puzzle_input()

        print("\nSelected Puzzle:")
        print_puzzle(state)

    except ValueError as error:
        print("Invalid input:", error)
