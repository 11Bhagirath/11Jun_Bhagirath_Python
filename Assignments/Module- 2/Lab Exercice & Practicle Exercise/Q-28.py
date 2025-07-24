# Write a Python program to count how many times each character appears in a string.

dict1 = {1 : 'Bhagirath', 2 :'502', 3 :'11.06', 4 :'Gajera', 5 :'Shagun', 6 :'Ridhan'}

text = ''
for value in dict1.values():
    text += str(value)

# Count characters
count = {}
for char in text:
    count[char] = count.get(char, 0) + 1

# Show result
print(count)
