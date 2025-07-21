fl = open("Temp.txt","w")

id = input("Enter An ID: ")
name = input("Enter An Name: ")
city = input("Enter An City: ")

'''fl.write(id)
fl.write(name)
fl.write(city)'''

fl.write(f"ID:{id}\nName:{name}\nCity:{city}")

