# Probability that the median of 5 samples falls a middle quartile
from random import sample
from statistics import median

n = 100000

trial = lambda : n // 4 < median(sample(range(n), 5)) <= 3 * n // 4

print(sum(trial() for i in range(n)) / n)