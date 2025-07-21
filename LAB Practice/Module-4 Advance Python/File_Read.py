fl=open('temp.txt','r')
#print(fl.read()) #Reads Full File
#print(fl.readline()) #First Line of file 
#print(fl.readlines()) #It reads in list
#print(fl.readlines()[0:5]) #Double colon is used when to jump to other value

'''for i in fl:
    print(i)'''

if fl.readable():
    print("Yes.....")
else:
    print("No......!")

