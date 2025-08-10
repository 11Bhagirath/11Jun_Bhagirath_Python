'''Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue 
statement. List1 = ['apple', 'banana', 'mango']'''

list1 = ['apple', 'banana', 'mango']

'''for fruit in list1:
    if fruit == 'banana':
        continue
    print(fruit)'''

'''Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using 
the break statement. '''

for fruit in list1:
    if fruit == 'banana':
        break
    print(fruit)