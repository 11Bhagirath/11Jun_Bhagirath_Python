print("1. Area Of Circle")
print("2. Area Of Square")
print("3. Area Of Rectangle")
choice=int(input("Enter Your Choice Between 1-3: "))

def circle():
    pi=3.14
    r=int(input("Enter Radius Of Circle: "))
    cr=pi*r*r
    print("Area Of Circle Is: ",cr)

def square():
    s=int(input("Enter Square Area: "))
    sq=s*s
    print("Area Of Square Is: ",sq)

def rectangle():
    l=int(input("Enter Length Of Rectangle: "))
    w=int(input("Enter Width Of Rectangle: "))
    rc=l*w
    print("Area Of Rectangle Is: ",rc)
if choice==1:
    circle()
elif choice==2:
    square()
elif choice==3:
    rectangle()
else:
    print("INVALID Choice Error!")
