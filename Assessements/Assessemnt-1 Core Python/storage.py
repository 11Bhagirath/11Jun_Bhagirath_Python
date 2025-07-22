import os

LOG_FILE = "Log.txt"

def load_customers():
    customers = {}
    if not os.path.exists(LOG_FILE):
        return customers

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    record = {}
    for line in lines:
        line = line.strip()
        if line.startswith("Date & Time:"):
            record["time"] = line.split(":", 1)[1].strip()
        elif line.startswith("Account Number:"):
            acc = line.split(":", 1)[1].strip()
            record["acc"] = acc
        elif line.startswith("Account Name:"):
            record["name"] = line.split(":", 1)[1].strip()
        elif line.startswith("Account Type:"):
            record["type"] = line.split(":", 1)[1].strip()
        elif line.startswith("Balance:"):
            record["balance"] = float(line.split(":", 1)[1].strip())
        elif line.startswith("------------------------------------------"):
            if "acc" in record:
                customers[record["acc"]] = record
            record = {}
    return customers

def save_customers(customers):
    with open(LOG_FILE, "w") as f:
        for acc, data in customers.items():
            f.write(f"Date & Time: {data['time']}\n")
            f.write(f"Account Number: {acc}\n")
            f.write(f"Account Name: {data['name']}\n")
            f.write(f"Account Type: {data['type']}\n")
            f.write(f"Balance: {data['balance']}\n")
            f.write("------------------------------------------\n")