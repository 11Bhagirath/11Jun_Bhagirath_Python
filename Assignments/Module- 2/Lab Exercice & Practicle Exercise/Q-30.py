# Write a Python program to create a calculator using functions. 

def calc():
    x = int(input("Eneter 1st Value: "))
    y = int(input("Eneter 2nd Value: "))

    print(f"Sum Of {x} + {y} Is: {x+y}")
    print(f"Mul Of {x} * {y} Is: {x*y}")
    print(f"Sub Of {x} - {y} Is: {x-y}")
    print(f"Sum Of {x} / {y} Is: {x/y}")

calc()