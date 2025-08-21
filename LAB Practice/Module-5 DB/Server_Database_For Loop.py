import pymysql

try:
    db=pymysql.connect(host='localhost', user='root', password='',
    database='morningdb')
    print("Database Connected!")
except Exception as e:
    print("Error: ",e)

cr=db.cursor()

#Table Create

tbl_create = "create table studinfo(id integer primary key auto_increment,name text, city text)"

try:
    cr.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print("Error: ",e)

n = int(input("Enter Number Of Students:"))

for i in range(n):
    nm = input(f"Enter {i+1} Name:")
    ct = input(f"Enter {i+1} City:")

    try:
        cr.execute((f"insert into studinfo(name,city)values('{nm}','{ct}')"))
        db.commit()
        print("Record Inserted!")
    except Exception as e:
        print(e)