from bank import * 
import random
balance = 0.0

accn = random.randrange(1111111,9999999,210) #Auto Generate acc num

#User input 
name = input("Enter Your Name: ")
type = input("Enter Your Account Type: ")

# Deposite Amount 
amount = int(input("Enter Deposite Amount: "))
if amount <= 2000:
    print("Amount Should Be 2000 Or More Than 2000!")
    exit()
else:
    print("Your Deposited Amopunt Is: ", amount)

# Withdrawal Amount 
withdrawal = int(input("Enter Withdrwal Amount: ")) #Withdrawal user input
if withdrawal >= amount:
    print("Insufficient Balance!")
    exit()
else:
    balance = amount - withdrawal
    print("Your Balance Is: ", balance)

# Statement
def statement():
    print("------Account Details------")
    print("Account Number: ", )
    x=acc(name,type = "Savings")
    print("Account Holder Name: " , x[0])
    print("Account Type: ", x[1])
    deposite(amount)
    print("Deposited Amount Is: ", amount)
    withdraw(withdrawal)
    print("Withdraw Amount Is: ", withdrawal)
    print("Your Balance Is: ", balance)

# Calling
statement()

'''while True:
    t = input("Do you want to continue? (Y/N): ")
    if t == 'Y':
        statement()
    elif t == 'N':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Please enter 'Y' or 'N'.")'''