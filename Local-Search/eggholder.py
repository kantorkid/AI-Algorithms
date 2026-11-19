import math
import random

def eggholder(x, y):
    term1 = -(y + 47) * math.sin(
        math.sqrt(abs(x / 2 + y + 47))
    )

    term2 = -x * math.sin(
        math.sqrt(abs(x - (y + 47)))
    )

    return term1 + term2

def hill_climbing(max_no_improvement=100):
    x = random.uniform(-512, 512)
    y = random.uniform(-512, 512)

    initial_position = (x, y)
    current_value = eggholder(x, y)

    no_improvement = 0
    steps = 0

    while no_improvement < max_no_improvement:
        new_x = x + (random.random() - 0.5) * 1.0
        new_y = y + (random.random() - 0.5) * 1.0

        if not (-512 <= new_x <= 512 and
                -512 <= new_y <= 512):
            no_improvement += 1
            steps += 1
            continue

        new_value = eggholder(new_x, new_y)

        if new_value < current_value:
            x = new_x
            y = new_y
            current_value = new_value
            no_improvement = 0
        else:
            no_improvement += 1

        steps += 1

    return {
        "initial_position": initial_position,
        "final_position": (x, y),
        "minimum": current_value,
        "steps": steps
}


if __name__ == "__main__":
    result = hill_climbing()

    print(f"Initial position: {result['initial_position']}")
    print(f"Final position:   {result['final_position']}")
    print(f"Minimum found:    {result['minimum']:.6f}")
    print(f"Total steps:      {result['steps']}")