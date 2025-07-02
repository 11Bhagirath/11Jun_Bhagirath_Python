mydic={}

n=int(input("Enter Number Of Pair: "))

for i in range(n):
    x=int(input(f"Enter {i+1} ID: "))
    y=input(f"Enter {i+1} Name: ")

    mydic[x] = y
    
print(mydic)