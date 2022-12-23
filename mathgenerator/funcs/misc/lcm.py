import random


def lcm(maxVal=20):
    """LCM (Least Common Multiple)"""
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    c = a * b
    x, y = a, b

    while y:
        x, y = y, x % y
    d = c // x

    problem = f"LCM of ${a}$ and ${b} =$"
    solution = f'${d}$'
    return problem, solution
