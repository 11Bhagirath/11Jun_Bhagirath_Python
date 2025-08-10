#Write a Python program to write multiple strings into a file. 
fl = open("Temp.txt","a")

lists = ["\nMy Name Is Bhagirath\n",
         "My Age Is 28\n",
         "My Height Is 5.11\n"]

fl.writelines(lists)

