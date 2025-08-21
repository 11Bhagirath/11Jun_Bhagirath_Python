import sqlite3

try:
    db = sqlite3.connect("temp.db")
    db.commit()
    print("Database Connected!")
except Exception as e:
    print(e)

#Table Created

tbl_create = "create table studinfo(id integer primary key autoincrement," 
"name text, city text)"

try:
    db.execute(tbl_create)
    print("Table Created!0")
except Exception as e:
    print(e)


#Inserted Data
"""insert_data = "insert into studinfo(name,city)values('Bhagirath','Rajkot'),('Janki','Dhoraji'),('Alpeshbhai','Rajkot'),('Hardikjiju','Junagadh')"

try:
    db.execute(insert_data)
    db.commit()
    print("Table Created!")
except Exception as e:
    print(e)"""


#Update Data
"""update_data="update studinfo set name='harsh', city='baroda' where id=7"
try:
    db.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=8"
try:
    db.execute(delete_data)
    db.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""

#Show Data
cr = db.cursor()
show_data = "select * from studinfo"
try:
    cr.execute(show_data)
    data = cr.fetchall()
    #data.cr.fetchmany(2)
    #data.cr.fetchone()
    #print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)