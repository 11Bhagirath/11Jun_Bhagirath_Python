class studinfo:
    def __init__(self):
        unm=input("Enter Your Username:")
        pas=input("enter Your Password:")

        if unm == 'admin' and pas == 'admin@123':
            print("Login Successful!")
        else:
            print("Error! Invalid Username Or Password!")

s = studinfo()