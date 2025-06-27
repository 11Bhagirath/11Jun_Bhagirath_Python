first=input("Enter Your First Name: ")
last=input("Enter Your Last Name: ")
email=input("Enter Your Email: ")
if first.islower() and last.islower() and email.islower():
    password=(input("Enter Your Password: "))
    confirm=(input("Confirm Your Password: "))
    if len(password)<=10 and password==confirm:   
        mobile=(input("Enter Your Mobile Number: "))
        if len(mobile)==10 and mobile.isdigit():
            print("---FORM DETAILS---")
            print("First Name: ",first)
            print("Last Name: ",last)
            print("Email: ",email)
            print("Password: ",confirm)
            print("Mobile Number: ",mobile)
        else:
            print("Please Enter 10 Digit Mobile Number!")
    else:
        print("Password Is Not Matched Or Maximum 8 Length Compulsory!")
else:
    print("Please Enter Details In Lower Case!")


