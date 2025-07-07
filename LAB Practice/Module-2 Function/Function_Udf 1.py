#function defining
def myfunc():
    print("This is my function!") #statement (func.body)


def getsum(a,b):
    print("Sum:",a+b)


def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)


#function calling
myfunc()
#getsum(23,54)
no1=int(input("Enter no1:"))
no2=int(input("Enter no2:"))
getsum(no1,no2)

getdata(1,'Sanket','Python')