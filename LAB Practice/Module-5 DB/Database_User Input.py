import sqlite3

try:
    db = sqlite3.connect("temp.db")
    db.commit()
    print("Database Connected!")
except Exception as e:
    print(e)

#Table Created

tbl_create = "create table studinfo(id integer primary key autoincrement,name text, city text)"

try:
    db.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)

n = int(input("Enter Number Of Students:"))

for i in range(n):
    nm = input(f"Enter {i+1} Name:")
    ct = input(f"Enter {i+1} City:")

    try:
        db.execute((f"insert into studinfo(name,city)values('{nm}','{ct}')"))
        db.commit()
        print("Record Inserted!")
    except Exception as e:
        print(e)

    