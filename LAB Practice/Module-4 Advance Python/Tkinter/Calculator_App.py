import tkinter
from tkinter import ttk

windows = tkinter.Tk()
windows.title("Calculator")
windows.geometry("500x600")
windows.config(bg="skyblue")

tkinter.Label(text="Enter First Value:",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=0,column=0,sticky="w")
tkinter.Label(text="Enter Second Value:",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=1,column=0,sticky="w")

fvalue = tkinter.Entry(font="Calibri 10 bold")
fvalue.grid(row=0,column=1,sticky="w")
svalue = tkinter.Entry(font="Calibri 10 bold")
svalue.grid(row=1,column=1,sticky="w")

re = tkinter.Label(text="Result",bg="white",fg="black",
font="Calibri 15 bold")
re.place(x=20,y=150)


def addclick():
        result = int(fvalue.get()) + int(svalue.get())
        re.config(text=f"{fvalue.get()} + {svalue.get()} = {result}")

tkinter.Button(text="Add +",font="Calibri 14 bold",
command=addclick).place(x=20,y=80)

def subclick():
    result = int(fvalue.get()) - int(svalue.get())
    re.config(text=f"{fvalue.get()} - {svalue.get()} = {result}")
    
tkinter.Button(text="Sub -",font="Calibri 14 bold",
command=subclick).place(x=100,y=80)

def mulclick():
    result = int(fvalue.get()) * int(svalue.get())
    re.config(text=f"{fvalue.get()} * {svalue.get()} = {result}")
    
tkinter.Button(text="Mul *",font="Calibri 14 bold",
command=mulclick).place(x=180,y=80)

def divclick():
    result = int(fvalue.get()) / int(svalue.get())
    re.config(text=f"{fvalue.get()} / {svalue.get()} = {result}")

tkinter.Button(text="Div /",font="Calibri 14 bold",
command=divclick).place(x=260,y=80)

windows.mainloop()