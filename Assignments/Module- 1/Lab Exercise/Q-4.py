"""Practical Example 5: Write a Python program to find greater and less than a number using 
if_else. """

'''num1=int(input("Enter A Num1: "))
num2=int(input("Enter A Num2: "))

if num1>num2:
    print("Number is Greater Than.")
elif num1==num2:
    print("Both Are SAME.")
else:
    print("Number is Smaller Than.")'''


# Practical Example 6: Write a Python program to check if a number is prime using if_else. 

'''num=int(input("Enter a Number: "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is Not A Prime.")
            break
    else:
        print(f"{num} Is a PRIME NUMBER.")
else:
    print(f"{num} is NOT a Prime Number.")'''

"""Practical Example 7: Write a Python program to calculate grades based on percentage using 
if-else ladder.""" 
    
'''s1 = int(input("Enter s1 Marks: "))
s2 = int(input("Enter s2 Marks: "))
s3 = int(input("Enter s3 Marks: "))
s4 = int(input("Enter s4 Marks: "))

total=s1+s2+s3+s4
print("Total: ",total)

pr=total/4
print("PR: ",pr)

if pr>=90:
    print("Grade is A+.")
elif pr>=80:
    print("Grade is A.")
elif pr>=70:
    print("Grade is B.")
elif pr>=60:
    print("Grade is C.")
elif pr>=50:
    print("Grade is D.")
else:
    print("F (FAIL!)")  '''


'''Practical Example 8: Write a Python program to check if a person is eligible to donate blood 
using a nested if.''' 

age = int(input("Enter Your Age: "))
weight  = float(input("Enter Your Weight: "))

if age>=18:
    if weight >=50:
        print("You Are ELIGIBLE To Donate BLOOD.")
    else:
        print("You Are NOT Eligible To Donate BLOOD Due To Insufficient WEIGHT!")
else:
    print("Your Age Must Be ABOVE 18!")


