# Write a Python program to show method overriding. 

class master:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

    def production(self,x,y):
        print("Production:",x*y)

class home(master):
    def getdata(self, id, name):
        return super().getdata(id, name)
    
    def production(self, x, y):
        return super().production(x, y)

class about(master):
    def getdata(self, id, name):
        return super().getdata(id, name)
    
    def production(self, x, y):
        return super().production(x, y)
    

h=home()
h.getdata(10,'Bhagirath')
h.production(25,25)

a=about()
a.getdata(102,'Janki')
a.production(5,2)