'''
f-strings are introduced with Python 3.6 (https://www.python.org/dev/peps/pep-0498/)
'''

x = 10

# Traditional ways to print: 1. %-formatting and 2. str.format()
print("The answer is %d" % x)
print("The answer is {x}".format(x=x))

# With f-string
print(f"The answer is {x}")
print(F"The answer is {x}")  # Can also use a captital letter F

# f-string supports format
print(f'The answer is {x: 08d}')

# Do math with f-string
print(f'The answer is {x**2:08d}')

# Call function with f-string
def add_five(input):
    return input + 5

print(f'The answer plus 5 is {add_five(x)}')

# Call method directly with f-string
name = 'Phil'
print(f'hello {name.lower()}')

# Even work with lambda function
print(f'{(lambda x: x*2)(3)}')

# Really nice way to implement exception messages with f-string
# Note: by default, f-strings will use __str__(), 
# but you can make sure they use __repr__() if you include the conversion flag !r:
raise ValueError(f'Expected {x!r} to a float not a {type(x).__name__}')

