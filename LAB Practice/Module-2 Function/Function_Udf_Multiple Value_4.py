n=int(input("Enter Number Of Student: "))
def getdata():
    stid=input("Enter an ID: ")
    stnm=input("Enter an Name: ")
    stct=input("Enter an City: ")
    print("ID: ",stid)
    print("Name: ",stnm)
    print("City: ",stct)
    print("  ")
    
for i in range(n):
    getdata()
