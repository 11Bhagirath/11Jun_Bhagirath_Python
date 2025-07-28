class studinfo:
    stid:int
    stnm:str

    def getdata(self):
        self.stid = input("Enter Your ID: ")
        self.stnm = input("Enter Your Name: ")

class result(studinfo):
    def printdata(self):
        print("ID: ",self.stid)
        print("Name: ",self.stnm)


rt = result()
rt.getdata()
rt.printdata()