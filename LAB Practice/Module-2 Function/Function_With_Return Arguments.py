'''def getsum(a,b):
    #print("Sum:",a+b)
    return a+b
    

x=getsum(43,56)
print(x)'''

#--------------------------

def getsum(a,b):
    return a,b

def getvalue():
    x=getsum(23,45)
    print("A:",x[0])
    print("B:",x[1])

getvalue()