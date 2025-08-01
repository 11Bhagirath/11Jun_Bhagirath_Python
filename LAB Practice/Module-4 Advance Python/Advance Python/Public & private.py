#Private

class studinfo:
    __stid=12
    __stnm="Bhagirath"

    def __getdata(self):#Private
        print("This is getdata")
        print("ID: ",self.__stid)
        print("Name:",self.__stnm)

    def printdata(self):
        self.__getdata()

st=studinfo()
st.printdata()