import random


def factors(maxVal=1000):
    """Factors of a number"""
    n = random.randint(1, maxVal)

    factors = []

    for i in range(1, int(n**0.5) + 1):
        if i**2 == n:
            factors.append(i)
        elif n % i == 0:
            factors.append(i)
            factors.append(n // i)
        else:
            pass

    factors.sort()

    problem = f"Factors of ${n} = $"
    solution = factors
    return problem, f'${solution}$'
