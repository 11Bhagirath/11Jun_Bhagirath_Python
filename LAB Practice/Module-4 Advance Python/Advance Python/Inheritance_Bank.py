import random
import datetime

class accop: 
    acc_name : str
    acc_type : str
    t = datetime.datetime.now()
    acc_num = random.randrange(0000000000,1111111111,111)
    def accopen(self):
        self.acc_name = input("Enter Your Name: ")
        self.acc_type = input("Enter Your Account Type: ")
    

class deposite(accop):
    depo_balance : float
    def depositeamt(self):
        self.depo_balance = float(input("Enter Deposite Amount: "))
        if self.depo_balance <= 2000:
            print("Please Enter Rs2000 Or Greter Than 2000!")
            
        else:
            print(f"Deposited Amopunt Is: {self.depo_balance}")

class withdrawl(deposite):
    withdraw_amt : float
    total_amt : float
    def withdraw(self):
        self.withdraw_amt = float(input("Enter Withdraw Amount: "))
        self.total_amt = self.depo_balance-self.withdraw_amt
        if self.withdraw_amt >= self.depo_balance:
            print("Insufficient Balance!")
        else:
            print(f"Withdraw Amopunt Is: {self.withdraw_amt}")
            
class statement(withdrawl):

    def final_statement(self):
        print("-----Statements Details-----")
        print("Date & Time: ",self.t)
        print("Account Number: ",self.acc_num)
        print("Account Holder Name: ",self.acc_name)
        print("Account Type: ",self.acc_type)
        print("Balance: ",self.total_amt)
        

tp = statement()
tp.accopen()
tp.depositeamt()
tp.withdraw()
tp.final_statement()