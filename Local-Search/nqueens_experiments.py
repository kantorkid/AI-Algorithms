
import os
import matplotlib.pyplot as plt

from nqueens import hill_climbing_nqueens


def plot_board(ax, board, title):
    """Draw an N-Queens board on a Matplotlib axis."""
    n = len(board)

    for row in range(n):
        for col in range(n):
            color = "#EEEED2" if (row + col) % 2 == 0 else "#769656"

            ax.add_patch(
                plt.Rectangle((col, row), 1, 1, color=color)
            )

    for col, row in enumerate(board):
        ax.text(
            col + 0.5,
            row + 0.5,
            "Q",
            ha="center",
            va="center",
            fontsize=max(6, 24 - n // 2),
            fontweight="bold",
            color="black"
        )

    ax.set_xlim(0, n)
    ax.set_ylim(n, 0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=10)


def run_experiments(n, num_runs=100):
    """Run Hill Climbing and record its success rate."""
    successes = 0
    results = []

    os.makedirs("nqueens_plots", exist_ok=True)

    for run in range(num_runs):
        result = hill_climbing_nqueens(n)
        results.append(result)

        if result["success"]:
            successes += 1

        print(
            f"N={n}, Run {run + 1:3d}: "
            f"Initial attacks={result['initial_attacks']:3d}, "
            f"Final attacks={result['final_attacks']:3d}, "
            f"Steps={result['steps']:3d}, "
            f"Success={result['success']}"
        )

        # Plot the initial and final boards for the first 10 runs
        if run < 10:
            fig, axes = plt.subplots(1, 2, figsize=(12, 6))

            plot_board(
                axes[0],
                result["initial_board"],
                f"Initial: {result['initial_attacks']} attacks"
            )

            plot_board(
                axes[1],
                result["final_board"],
                f"Final: {result['final_attacks']} attacks"
            )

            fig.suptitle(f"N={n}, Run {run + 1}")
            plt.tight_layout()

            filename = f"nqueens_plots/n{n}_run{run + 1:02d}.png"
            plt.savefig(filename, dpi=200)
            plt.close(fig)

    success_rate = successes / num_runs * 100

    print(f"\nN={n} Summary")
    print(f"Successful solutions: {successes}/{num_runs}")
    print(f"Success rate: {success_rate:.1f}%\n")

    return results


if __name__ == "__main__":
    for n in [8, 16, 32]:
        run_experiments(n)
