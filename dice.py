
import random

def simulate_dice(n):
    counts = {i: 0 for i in range(1, 7)}
    for _ in range(n):
        outcome = random.randint(1, 6)
        counts[outcome] += 1
    return counts

m = int(input("Amount of dice rolls: "))
print(simulate_dice(m))
