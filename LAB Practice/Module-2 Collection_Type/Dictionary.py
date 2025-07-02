stdata={'id':101,'name':'Bhagirath','sub':'python'}
'''print(stdata)
print(stdata['name'])
print(stdata.get('sub'))
print(stdata.keys())
print(stdata.values())'''


'''print(stdata)
stdata['city']='rajkot' # To add a new pair
stdata['id']=102 #To Update the value
print(stdata)'''

stdata={'id':101,
        'name':'sanket',
        'sub':'python'}

"""print(stdata)
print(stdata['name'])
print(stdata.get("sub"))
print(stdata.keys())
print(stdata.values())
print(len(stdata))"""

"""if 'name' in stdata:
    print("Yes..")
else:
    print("Noo")"""

"""if 'sanket' in stdata.values():
    print("Yes..")
else:
    print("Noo")"""

# -------------------------------- #
#print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

# --------------------------------------- #

print(stdata)

#stdata['city']='rajkot' #add a new pair
#stdata['id']=102
#stdata.pop('sub')
#stdata.clear()
#del stdata['city']
#del stdata
#print(stdata)


newstdata=stdata.copy()
print(newstdata)