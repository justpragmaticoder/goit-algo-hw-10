import random


def f(x):
    return x**2


def monte_carlo_simulation(a, b, num_experiments):
    points_under_curve = 0

    for _ in range(num_experiments):
        x = random.uniform(a, b)
        y = random.uniform(0, f(b))
        if y <= f(x):
            points_under_curve += 1

    return (points_under_curve / num_experiments) * (b - a) * f(b)
