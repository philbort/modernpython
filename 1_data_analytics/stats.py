from statistics import mean, median, mode, stdev, pstdev

data = [50, 51, 51, 52, 53, 53, 53]
print(f"data: {data}")

print(f"mean: {mean(data)}")
print(f"median: {median(data)}")
print(f"mode: {mode(data)}")
print(f"stdev (divide by n-1): {stdev(data)}")
print(f"pstdev (divide by n): {pstdev(data)}")

# Nice chained comparison
print(data[0] < median(data) < data[-1])