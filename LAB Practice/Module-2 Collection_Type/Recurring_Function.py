# creating a function
def factorial(x):
    if x==1:
        return 1
    else:
        # calling a recursion function 
        return(x*factorial(x-1))
    
n=int(input("Enter Any Nymber: "))
print(f"The Factorial of {n} Is: ",factorial(n))