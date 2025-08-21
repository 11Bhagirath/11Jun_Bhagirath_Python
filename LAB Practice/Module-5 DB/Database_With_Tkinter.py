import tkinter
from tkinter import ttk
import sqlite3


windows = tkinter.Tk()
windows.title("Studets Informationn")
windows.geometry("500x500")
windows.config(bg="skyblue")


tkinter.Label(text="Enter Your Name:",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=0,column=0,sticky="w")
tkinter.Label(text="Enter Your City:",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=1,column=0,sticky="w")

nvalue = tkinter.Entry(font="Calibri 10 bold")
nvalue.grid(row=0,column=1,sticky="w")
cvalue = tkinter.Entry(font="Calibri 10 bold")
cvalue.grid(row=1,column=1,sticky="w")

re = tkinter.Label(text="*Inserted Data*",bg="white",fg="black",
font="Calibri 15 bold")
re.place(x=165,y=150)


def subclick():
    name = nvalue.get()
    city = cvalue.get()
    re.config(text=f"Name:{name}\nCity:{city}")

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

    #Inserted Data

        try:
            db.execute(f"insert into studinfo(name,city)values('{name}','{city}')")
            db.commit()
            print("Data Inserted!")
        except Exception as e:
            print("Error:",e)

tkinter.Button(text="Submit",font="Calibri 14 bold",
command=subclick).place(x=200,y=100)

windows.mainloop()