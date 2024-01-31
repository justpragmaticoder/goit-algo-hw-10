import numpy as np
from scipy.integrate import quad
from monte_carlo import monte_carlo_simulation


def f(x):
    return x**2


# Borders
a = 0
b = 2

analytical_result, _ = quad(f, a, b)

num_points = 10000
monte_carlo_area = monte_carlo_simulation(a, b, num_points)

print(f"Area under the curve using analitical method: {analytical_result}")
print(f"Area under the curve using Monte Carlo method: {monte_carlo_area}")
