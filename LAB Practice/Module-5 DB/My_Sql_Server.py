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

insert_data = "insert into studinfo(name,city)values('Bhagirath','Rajkot'),('Janki','Dhoraji'),('Alpeshbhai','Rajkot'),('Hardikjiju','Junagadh')"

try:
    cr.execute(insert_data)
    db.commit()
    print("Table Inserted!")
except Exception as e:
    print(e)