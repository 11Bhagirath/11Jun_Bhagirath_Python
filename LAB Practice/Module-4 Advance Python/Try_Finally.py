try:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))

    print(f"Sum Of {a} + {b} Is: {a+b}")
except Exception as e:
    print(e)
finally:
    print("There Is No Error!")