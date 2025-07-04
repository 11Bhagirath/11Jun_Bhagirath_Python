s1=int(input("Enter English Marks:  "))
s2=int(input("Enter Hindi Marks:  "))
s3=int(input("Enter Science Marks:  "))
s4=int(input("Enter Maths Marks:  "))

total=s1+s2+s3+s4
print("Total Marks: ",total)

pr=total/4
print("PR: ",pr)

if pr>=70: 
    print("Result: Distinction")
elif pr>=60: 
    print("Result: First Class")
elif pr>=50: 
    print("Result: Second Class")
elif pr>=40: 
    print("Result: Pass Class")
else:
    print("Result: FAIL")