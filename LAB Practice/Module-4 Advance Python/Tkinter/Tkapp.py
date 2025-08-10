import tkinter
from tkinter import ttk

windows = tkinter.Tk()
windows.title("")
windows.geometry("400x400")
windows.config(bg="skyblue")

"""tkinter.Label(text="Firstname:").pack()
tkinter.Label(text="Lastname:").pack()"""


"""tkinter.Label(text="Firstname:",bg='lightblue', fg='purple', font='Fixedsys 18 bold').place(x=0,y=0)
tkinter.Label(text="Lastname:",bg='lightblue', fg='purple', font='Fixedsys 18 bold').place(x=0,y=30)"""

"""tkinter.Label(text="Firstname:",bg='lightblue', fg='purple', font='Fixedsys 18 bold').place(x=0,y=0)
tkinter.Label(text="Lastname:",bg='lightblue', fg='purple', font='Fixedsys 18 bold').place(x=0,y=30)"""

tkinter.Label(text="First Name:,",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=0,column=0,sticky="w")
tkinter.Label(text="Last Name:,",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=1,column=0,sticky="w")

fnm = tkinter.Entry(font="Calibri 10 bold")
fnm.grid(row=0,column=1,sticky="w")
lnm = tkinter.Entry(font="Calibri 10 bold")
lnm.grid(row=1,column=1,sticky="w")

tkinter.Radiobutton(value=0,text="Male",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=2,column=0,sticky="w")
tkinter.Radiobutton(value=1,text="Female",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=2,column=1,sticky="w")

tkinter.Checkbutton(text="Gujarati",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=3,column=0,sticky="w")
tkinter.Checkbutton(text="Hindi",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=4,column=0,sticky="w")
tkinter.Checkbutton(text="English",bg="skyblue",fg="black",
font="Calibri 15 bold").grid(row=5,column=0,sticky="w")

city = ["junagadh","Rajkot"]

ttk.Combobox(values=city).grid(row=6,column=0)

def btnclick():
    #print("Button Clicked")
    print("First Name:",fnm.get())
    print("Last Name:",lnm.get())

tkinter.Button(text="Submit",font="Calibri 14 bold",
command=btnclick).place(x=180,y=250)

windows.mainloop()