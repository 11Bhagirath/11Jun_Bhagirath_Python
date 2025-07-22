import datetime
import random
from storage import save_customers

def add_customer(customers):
    now = datetime.datetime.now()
    acc = str(random.randint(1000000, 9999999))
    name = input("Enter Customer Name: ").strip()
    acc_type = input("Enter Account Type: ").strip()
    balance = float(input("Enter Opening Balance (Min ₹2000): "))
    customers[acc] = {
        "time": now,
        "name": name,
        "type": acc_type,
        "balance": balance
    }
    print(f"\nAccount Created: {acc} - {name} - ₹{balance}")
    save_customers(customers)

def view_customer(customers):
    acc = input("Enter Account Number: ").strip()
    cust = customers.get(acc)
    if cust:
        print(f"\nAccount #: {acc}")
        print(f"Name:      {cust['name']}")
        print(f"Type:      {cust['type']}")
        print(f"Balance:   ₹{cust['balance']}")
        print(f"Joined:    {cust['time']}")
    else:
        print("Account not found.")

def search_customer(customers):
    query = input("Enter Account # or Name: ").strip().lower()
    for acc, cust in customers.items():
        if query == acc or query in cust["name"].lower():
            print(f"\nFound: {acc} - {cust['name']} - ₹{cust['balance']}")
            return
    print("No match found.")

def view_all(customers):
    if not customers:
        print("(No accounts found.)")
        return
    for acc, cust in customers.items():
        print(f"{acc}: {cust['name']} - ₹{cust['balance']}")

def total_balance(customers):
    total = sum(c["balance"] for c in customers.values())
    print(f"\nTotal Bank Balance: ₹{total}")

def withdraw(customers):
    acc = input("Enter Account Number: ").strip()
    cust = customers.get(acc)
    if not cust:
        print("Account not found.")
        return
    amt = float(input("Enter Amount to Withdraw: "))
    if amt <= cust["balance"]:
        cust["balance"] -= amt
        print(f"Withdrawn ₹{amt}. New Balance: ₹{cust['balance']}")
        save_customers(customers)
    else:
        print("Insufficient funds.")

def deposit(customers):
    acc = input("Enter Account Number: ").strip()
    cust = customers.get(acc)
    if not cust:
        print("Account not found.")
        return
    amt = float(input("Enter Amount to Deposit: "))
    cust["balance"] += amt
    print(f"Deposited ₹{amt}. New Balance: ₹{cust['balance']}")
    save_customers(customers)

def view_balance(customers):
    acc = input("Enter Account Number: ").strip()
    cust = customers.get(acc)
    if cust:
        print(f"\nBalance: ₹{cust['balance']}")
    else:
        print("Account not found.")