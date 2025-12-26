import random
from typing import Dict


def simulate_dice_rolls(num_rolls: int) -> Dict[int, float]:
    """
    Simulates rolling two dice 'num_rolls' times
    Returns: 
        A dictionary where keys are the sums (2-12)
        and values are the probability of that sum appearing
    """
    # counters for sums from 2 to 12
    counts = {sum_val: 0 for sum_val in range(2, 13)}

    for _ in range(num_rolls):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        roll_sum = d1 + d2
        counts[roll_sum] += 1

    probabilities = {k: v / num_rolls for k, v in counts.items()}

    return probabilities


def print_comparison_table(input_probs: Dict[int, float]):
    # theoretical probabilities for sums 2 through 12
    theoretical_probs = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    print(f"{'Sum':<5} | {'Monte Carlo':<12} | {'Theoretical':<12} | {'Difference':<12}")
    print("-" * 50)
    for sum_val in range(2, 13):
        mc_prob = input_probs.get(sum_val, 0)
        th_prob = theoretical_probs[sum_val]
        diff = abs(mc_prob - th_prob)
        print(f"{sum_val:<5} | {mc_prob:<12.4f} | {th_prob:<12.4f} | {diff:<12.4f}")
    print("-" * 50)


if __name__ == "__main__":
    simulation_counts = [100, 1000, 10_000, 1_000_000]
    for accuracy in simulation_counts:
        print(f"----- Running simulation for {accuracy} rolls -----")
        probs = simulate_dice_rolls(accuracy)
        print_comparison_table(probs)
