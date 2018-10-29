from collections import Counter

'''
https://docs.python.org/3/library/collections.html?highlight=collections#collections.Counter
'''

# Works like a dictionary but won't give key error
d = Counter()
print(d['dragons'])
d['dragons'] += 1
print(d['dragons'])

# Initialize a counter with string
c = Counter('red green blue red green green'.split())
print(c)

# Get most common
print(c.most_common(1))
print(c.most_common(2))

# Elements
print(list(c.elements()))
print(list(c.values()))
print(list(c.items()))