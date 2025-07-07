# 1) Account Opening
    # A/c Number
    # A/c holder name
    # A/c type
# 2) deposite
    #min 2000/-
# 3) Withdrawal
# 4) Statements
#   A/c number
#   A/c holder name
#   A/c type
#   balance

balance=0.0

anum=int(input("Enter Account Number: "))
aname=input("Enter Your Name: ")
atype=input("Enter Your Account Type (Saving Or Current): ")

# ----Account Open----

def acc(anum,aname,atype="Saving"):
    return anum,aname,atype

def accopen():
    a=acc(anum,aname,atype="Saving")
    print("----Statement Details----")
    print("Account Number: ",a[0])
    print("Account Name: ",a[1])
    print("Account Type: ",a[2])
    print("Available Balance Is: ",balance)

# ----Deposite----

def deposite():
    global balance
    balance=float(input("Enter Deposite Value (Min Balance 2000): "))
    if balance>=2000:
        print("Available Blanace Is: ",balance)   
    else:
        print("Minimum Deposite Amount Should Be 2000 Or More!")
        exit()    

# ----Withdrawal----  
        
def withdraw():
    global balance
    w=int(input("Enter Withdrawal Amount: "))
    if balance <= w:
        print("Insufficient Balance!")
        exit()
    else:
        balance-=w
    print("Available Balance is: ",balance)

# ----Statements----

def statements():
    deposite()
    withdraw()
    accopen()

# ----Calling Function----

statements()