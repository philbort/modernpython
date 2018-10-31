# 5 or more heads from 7 spins of a biased coin
from random import choices

# Population
pop = ['heads', 'tails']

# Weights
wgt = [6, 4]

# Cumulative weights
cumwgt = [0.60, 1.00]

# 7 spins
print(choices(pop, cum_weights=cumwgt, k=7))

# 5 or more
print(choices(pop, cum_weights=cumwgt, k=7).count('heads') >= 5)

# Define the experinment
trial = lambda : choices(pop, cum_weights=cumwgt, k=7).count('heads') >= 5

# Simulation
n = 100000
print(sum(trial() for i in range(n))/n)

# Compare to the analytic solution
from math import factorial

def comb(n, r):
    assert(n >= r)
    return factorial(n) // factorial(r) // factorial(n - r)

ph = 0.6
print(ph ** 5 * (1 - ph) ** 2 * comb(7, 5) + \
      ph ** 6 * (1 - ph) ** 1 * comb(7, 6) + \
      ph ** 7 * (1 - ph) ** 0 * comb(7, 7))