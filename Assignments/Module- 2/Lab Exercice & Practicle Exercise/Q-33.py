#  Write a Python program to create a lambda function with two expressions.

process = lambda x: (x * x, x + 10)

square, increment = process(5)
print("Square:", square)
print("Incremented:", increment)