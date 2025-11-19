import random

def run_binomial(n, p, experiments):
    results = []
    for _ in range(experiments):
        success = sum(1 for _ in range(n) if random.random() <= p)
        results.append(success)
    return results

n = int(input("Number of trials: "))
p = float(input("Probability of success per trial: "))
experiments = int(input("Number of experiments: "))
print(run_binomial(n,p,experiments))
                   
