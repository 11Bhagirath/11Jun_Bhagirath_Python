# Write a Python program to merge two lists into one dictionary using a loop.

key = ['Name','Date', "Sur", 'Nephew']

values = ['Bhagirath'
          ,'11.06','Gajera','Shagun']

dict = {}

for i in range(len(key)):
    dict[key[i]] = values[i]

print(dict)

