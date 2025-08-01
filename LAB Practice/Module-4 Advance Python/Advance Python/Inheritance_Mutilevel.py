class bhagirath:
    bid:int
    btech:str

    def b_getdata(self):
        self.bid = input("Enter Bhagirath's Id: ")
        self.btech = input("Enter Bhagirath's Tech: ")

class hardikjiju(bhagirath):
    hid:int
    htech:str

    def h_getdata(self):
        self.hid = input("Enter Hardik Jiju's Id: ")
        self.htech = input("Enter Hardik Jiju's Tech: ")


class alpeshbhai(hardikjiju):
    aid:int
    atech:str

    def a_getdata(self):
        self.aid = input("Enter Alpeshbhai's Id: ")
        self.atech = input("Enter Alpeshbhai's Tech: ")

class tops(hardikjiju):

    def printdata(self):
        print("-----Bhagirath's Data-----")
        print("Bhagirath's ID: ",self.bid)
        print("Bhagirath's Tech: ",self.btech)
        print("-----Hardik jiju's Data-----")
        print("Hardik Jiju's ID: ",self.hid)
        print("Hardik Jiju's Tech: ",self.htech)
        print("-----Alpeshbhai's Data-----")
        print("Alpeshbhai's ID: ",self.aid)
        print("Alpeshbhai's Tech: ",self.atech)
        

tp = tops()
tp.b_getdata()
tp.h_getdata()
tp.a_getdata()
tp.printdata()