# Write a Python program to print custom exceptions.

class MyError(Exception):
    pass

# Use the custom exception
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise MyError("Negative number not allowed.")
    print("You entered:", num)
except MyError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Please enter a valid number.")