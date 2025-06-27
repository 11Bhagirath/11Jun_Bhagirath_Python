data=["python","java","php","html","css"]
#print(data)

'''print(data[0])
print(data[-1])
print(data[0:3]) #range
print(data[2:1])
print(data[:3])
print(len(data))'''

'''
if 'php' in data: #case sensitive
    print("YES......")
else:
    print("NO......")'''

'''for i in data:
    print(data.index(i),"-",i)'''

'''for i in data:
    print(f"{data.index(i)} - {i}")'''

'''data[2]='android' #For updating value
print(data) '''

print(data)
#data[2]='android' # for updating value
#data.append("react")
#data.insert(2,'css')
#data.remove('java')
#data.pop() # for delete pop is used it deletes last value
#data.pop(1)
#data.clear()
#del data[3]
#del data
#data.sort()
#data.reverse()
#print(data.count('php'))
#newdata=data.copy()
#print(newdata)

newdata=['html','css','js']
print(newdata)

#print(data+newdata)
data.extend(newdata)

#print(data+newdata)
data.extend(newdata)
print(data)