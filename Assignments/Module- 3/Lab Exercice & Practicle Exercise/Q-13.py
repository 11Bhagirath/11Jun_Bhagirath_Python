#Write a Python program to create a class and access its properties using an object. 

class mydata:
    def data(self):
        n1 = int(input("Enter Num1:"))
        n2 = int(input("Enter Num2:"))

        add = n1+n2
        print(f"Sum Of {n1} + {n2} = {add}")

m = mydata
m.data()