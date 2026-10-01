# Simulate dice rolling experiment
import numpy as np

def roll_dice(trials: int):
    """Simulate rolling two fair dice, return sum of each trial"""
    die1 = np.random.randint(1,7, size=trials)
    die2 = np.random.randint(1,7, size=trials)
    return die1 + die2

if __name__ == "__main__":
    experiment_times = 10000
    result = roll_dice(experiment_times)
    print(f"Finished {experiment_times} dice rolling simulation.")
    print(f"Mean value: {np.mean(result):.2f}")
