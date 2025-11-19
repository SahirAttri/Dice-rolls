import random

def simulate_flips(n, p_heads):
    results = {"Heads": 0, "Tails": 0}

    for _ in range(n):
        
        if random.random() < p_heads:
            results["Heads"] += 1
        else:
            results["Tails"] += 1

    return results

num_flips = int(input("How many coin flips do you want to simulate? "))
p_heads = float(input("Probability of Heads (0 to 1): "))

print(f"\nSimulating {num_flips} coin flips with Heads probability = {p_heads}:")
print(simulate_flips(num_flips, p_heads))
