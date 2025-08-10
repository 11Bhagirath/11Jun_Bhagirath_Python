#Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel)

#Single inheritance

'''class parent():
    def data(self):
        print("This is Parent Class")

class child(parent):
    def cdata(self):
        print("This is Child Class")

cd = child()
cd.data()
cd.cdata()'''

#Multiple Inheritance

'''class father():
    def fdata(self):
        print("This is Father Class")

class mother():
    def mdata(self):
        print("This is Mother Class")

class child(father,mother):
    def cdata(self):
        print("This is child Class")

cd = child()
cd.fdata()
cd.mdata()
cd.cdata()'''

#multilevel Inheritance

class father():
    def fdata(self):
        print("This is Father Class")

class mother(father):
    def mdata(self):
        print("This is Mother Class")

class child(mother):
    def cdata(self):
        print("This is child Class")

cd = child()
cd.fdata()
cd.mdata()
cd.cdata()