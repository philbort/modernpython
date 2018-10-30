from random import choice, choices, sample, shuffle
from collections import Counter

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']

# Choose 1
print(choice(outcomes))

# Choose k
print(Counter(choices(outcomes, k=10000)))

# Choose k with defined ratio
print(Counter(choices(outcomes, [5, 4, 3, 2, 1], k=10000)))

# Shuffle works in place
shuffle(outcomes)
print(outcomes)

# Sample without duplicates
print(sample(outcomes, k=4))

# Simulates a lottery outcome
print(sorted(sample(range(1, 57), k=6)))

# These two are the same
print(sample(outcomes, k=1)[0])
print(choice(outcomes))

# These two are the same as well
shuffle(outcomes); print(outcomes)
print(sample(outcomes, k=len(outcomes)))