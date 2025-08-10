import re

mystr="This is Python!1465"

x=re.match("This",mystr)
print(x)

if x: #True
    print("Match Found!")
else:
    print("Error!")