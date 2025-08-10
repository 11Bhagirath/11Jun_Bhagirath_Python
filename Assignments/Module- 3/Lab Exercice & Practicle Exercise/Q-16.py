# Write a Python program to demonstrate the use of super() in inheritance.

class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):
        super().show()  # Call the parent method
        print("This is the Child class.")

# Test
c = Child()
c.show()                                              