import random

def estimate_pi(trials):
    count = 0
    for trial in range(trials):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1.0:
            count += 1
    return (count / trials) * 4

def main():
    
    for trials in [10, 100, 1000, 10000, 100000]:
        result = estimate_pi(trials)
        print(result)

main()
