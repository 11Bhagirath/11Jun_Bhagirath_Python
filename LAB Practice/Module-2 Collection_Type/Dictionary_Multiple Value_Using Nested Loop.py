mydic=[]
table=['Id','Name','Add']

n=int(input("Enter Number Of Pairs: "))

for i in range(n):
    dic={}
    for j in table:
        value=input(f"Enter Value Of {j} Of {i+1}: ")
        dic[j]=value
    mydic.append(dic)

for i in mydic:
    print(i)
