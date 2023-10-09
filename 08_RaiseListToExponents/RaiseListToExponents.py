# Project 008: Raise List Items To Exponents

# Your code below:
single_digits = list(range(10))
print(single_digits)

# define variable 'squares'
squares = []
# square the items in the list
for n in single_digits:
  squares.append(n**2)
print(squares)

# using list comprehension, powers to third the items in the list
cubes = [n**3 for n in single_digits]
print(cubes)
