#Write a Python program to demonstrate handling multiple exceptions.

n1 = int(input("Enter Num1:"))
n2 = int(input("Enter Num2:"))

choose = input("Choose Operation(+, -, *, /) Sign:")

try:
    if choose == '+':
        add = n1+n2 
        print(f"Sum Of {n1} + {n2} = {add}")
    elif choose == '-':
        sub = n1+n2
        print(f"Sum Of {n1} - {n2} = {sub}")
    elif choose == '*':
        mul = n1*n2
        print(f"Sum Of {n1} * {n2} = {mul}")
    else:
        div = n1/n2
        print(f"Sum Of {n1} / {n2} = {div}")
except Exception as e:
    print(e)