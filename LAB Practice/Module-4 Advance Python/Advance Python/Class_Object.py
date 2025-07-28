class studinfo:
    stid = 15
    stnm = "Bhagirath"

    def myfunc(self):
        print("This is studinfo class.")

    def sum(self,a,b):
        print(f"Sum Of {a} + {b} Is: {a+b}")
    
st = studinfo()
print("Id: ",st.stid)
print("Name: ",st.stnm)
st.myfunc()
st.sum(34,66)
