fl=open("temp.txt","r+")

print(fl.readlines()[1:5])

fl.write("\nHello")