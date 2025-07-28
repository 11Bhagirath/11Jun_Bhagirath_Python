class studinfo:
    def userdata(self):
        self.stid = int(input("Enter Your ID: "))
        self.stnm = input("Enter Your Name: ")
   
    def data(self):
        print("Your ID: ",self.stid)
        print("Your Name Is: ",self.stnm)


st = studinfo()
st.userdata()
st.data()
