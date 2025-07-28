class studinfo:
    stid = 25
    stnm = "Bhagirath"

    def myfunc(self):
        print("This Is studinfo CLASS.")

    def sum(self,a,b):
        print(f"Sum Of {a} + {b} Is: {a+b}")

st = studinfo()
print("ID: ",st.stid)
print("Name: ",st.stnm)
st.myfunc()
st.sum(34,66)