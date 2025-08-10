import re

mail = input("Enter Your Mail:")

valid = "[a-z0-9._]+[@]+[a-z]+[.com|.co.in|.in]"

x=re.findall(valid,mail)
if x:
    print("Mail Is Valid!")
else:
    print("ERROR!")