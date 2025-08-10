#Write a Python program to show method overloading. 

# Python Is Not Supporting Overloading Method!

class studinfo:
    #Method Overloading
    def getdata(self,id):
        print("ID:",id)
    
    def getdata(self,name):
        print("Name:",name)

st=studinfo()
st.getdata(11)
st.getdata("Bhagirath")