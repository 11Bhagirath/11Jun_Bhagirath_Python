#Write a Python program to search for a word in a string using re.search().
# Write a Python program to match a word in a string using re.match().  

#Using re.match() Function.

import re

text = "hello world"
pattern = "hello"

result = re.match(pattern, text)

if result:
    print("Match found at the beginning!")
else:
    print("No match at the beginning.")


#Using Search() Function.

import re

text = "say hello to the world"
pattern = "hello"

result = re.search(pattern, text)

if result:
    print("Match found somewhere in the string!")
else:
    print("No match found.")