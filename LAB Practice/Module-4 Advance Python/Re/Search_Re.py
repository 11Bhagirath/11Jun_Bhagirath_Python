import re

mystr="This is Python!"

x=re.search("Python",mystr)
print(x)

if x: #TRUE
    print("Match Done!")
else:
    print("Error!")