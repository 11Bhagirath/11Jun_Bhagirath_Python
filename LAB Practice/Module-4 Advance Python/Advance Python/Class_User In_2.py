class studinfo:
    def printdata(self,stid,stnm):
        print("ID: ",stid)
        print("Name: ",stnm)

st = studinfo()
stid = input("Enter An ID: ")
stnm = input("Enter An Name: ")

st.printdata(stid,stnm)