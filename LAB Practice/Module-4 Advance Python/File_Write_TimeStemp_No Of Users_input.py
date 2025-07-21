import datetime
import random

#fl = open("Temp.txt","w")
fl = open("Temp.txt","a")

n=int(input("Enter Number Of Students: "))

def stdata():
    x=datetime.datetime.now()
    id=random.randrange(100,999,1)
    name=input("Enter An Name: ")
    city=input("Enter An City: ")

    fl.write(f"Date & Time: {x}\nID: {id}\nName: {name}\nCity: {city}\n---------------------------\n")

for i in range(n):
    stdata()

