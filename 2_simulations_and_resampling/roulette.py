from random import choices
from collections import Counter

# Six roulette wheel -- 18 red, 18 black, 2 green slots
population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
print(Counter(choices(population, k=6)))

# Better with weights directly
print(Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6)))