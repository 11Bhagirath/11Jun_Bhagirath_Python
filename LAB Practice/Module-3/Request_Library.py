import requests
import pandas

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()
x=pandas.DataFrame(data)
print(x)