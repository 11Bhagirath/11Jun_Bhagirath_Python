#Write a Python program to demonstrate the use of local and global variables in a class.
str = "My Name Is Bhagirath!"
class mydata:
    def data(self):
        n1:int
        n2:float

        n1 = int(input("Enter Num1:"))
        n2 = int(input("Enter Num2:"))

        add = n1+n2
        print(f"Sum Of {n1} + {n2} = {add}")
        print(f"Using Global Variable {str}")

my = mydata()
my.data()
