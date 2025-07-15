import pandas

p=pandas.read_excel('newdata.xlsx')

data=p.to_string()
print(data)