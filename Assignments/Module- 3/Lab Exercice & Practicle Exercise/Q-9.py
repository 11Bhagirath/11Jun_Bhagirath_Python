'''Write a Python program to handle exceptions in a simple calculator (division by zero, invalid 
input).'''

n1 = int(input("Enter Num1:"))
n2 = int(input("Enter Num2:"))


add = n1+n2 
print(f"Sum Of {n1} + {n2} = {add}")

sub = n1-n2
print(f"Subtraction Of {n1} - {n2} = {sub}")

mul = n1*n2
print(f"Multiplication Of {n1} * {n2} = {mul}")

try:
    div = n1/n2
    print(f"Division Of {n1} / {n2} = {div}")

except ZeroDivisionError:
    print("Error! Cannot Divide By Zero!")