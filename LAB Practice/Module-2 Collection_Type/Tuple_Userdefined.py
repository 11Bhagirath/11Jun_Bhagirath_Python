data=[]
n=int(input("Enter Number Of City List: "))

for i in range(n):
    j=i+1
    city=(input(f"Enter {j} City Name: "))
    data.append(city)

print(tuple(data))
      