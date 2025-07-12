import pandas

stdata={
    "id":[1,2,3,4,5],
    "name":["sanket","gopal","ashok","mitesh","hitesh"],
    "city":["rajkot","baroda","morbi","surat","jamnagar"]
}

data=pandas.DataFrame(stdata)
print(data)