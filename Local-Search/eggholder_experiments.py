
import statistics
import matplotlib.pyplot as plt

from eggholder import hill_climbing


def run_experiments(num_runs=100):
    minima = []

    for run in range(num_runs):
        result = hill_climbing()
        minima.append(result["minimum"])

        print(
            f"Run {run + 1:3d}: "
            f"Minimum = {result['minimum']:.6f}, "
            f"Steps = {result['steps']}"
        )

    print("\nExperiment Summary")
    print("------------------")
    print(f"Total runs: {num_runs}")
    print(f"Best minimum: {min(minima):.6f}")
    print(f"Worst minimum: {max(minima):.6f}")
    print(f"Mean minimum: {statistics.mean(minima):.6f}")
    print(f"Median minimum: {statistics.median(minima):.6f}")

    # Plot the distribution of minima across 100 runs
    plt.figure(figsize=(10, 6))
    plt.hist(minima, bins=20, edgecolor="black")

    plt.title("Eggholder Hill Climbing: Distribution of Minima")
    plt.xlabel("Final Objective Function Value")
    plt.ylabel("Number of Runs")
    plt.grid(axis="y", alpha=0.3)

    plt.savefig("eggholder_distribution.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    run_experiments()
