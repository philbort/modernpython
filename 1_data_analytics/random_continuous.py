from random import *
from statistics import mean, stdev

# Use the same random seed
seed(12345)

# Uniform distribution
print(uniform(1000, 1100))

# Triangular distribution
print(triangular(1000, 1100))

# Gaussian distribution
print(gauss(100, 15))


# Check distributions
data = [triangular(1000, 1100) for i in range(1000)]
print(mean(data))
print(stdev(data))

data = [uniform(1000, 1100) for i in range(1000)]
print(mean(data))
print(stdev(data))

data = [gauss(100, 15) for i in range(1000)]
print(mean(data))
print(stdev(data))