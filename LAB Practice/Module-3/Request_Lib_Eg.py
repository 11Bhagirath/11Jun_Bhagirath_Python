import requests

url="https://fakestoreapi.com/products/"

req=requests.get(url)

data=req.json()

#print(data)

for i in data:
    print(f"Product ID:{i["id"]}")
    print(f"Product Name:{i["title"]}")
    print(f"Product Price:{i["price"]}")
    print(f"Product Rating:{i["rating"]["rate"]}")
    print("-------------------------------")