#Implementation of the GUI for the students table
from db import *
from tkinter import *
from tkinter import ttk

def addStudentHandler(first,last,phone,major):  # This expects 4 stringVar
    insertStudent(first,last,major,phone)

def addStudent(root):
    add =  Toplevel(root)
    add.grid()
    add.transient(root) 
    add.grab_set() 
    Label(add, text="First Name").grid(column=0, row=0)
    first=StringVar()
    Entry(add,textvariable=first).grid(column=1,row=0)

    Label(add, text="Last Name").grid(column=0, row=1)
    last=StringVar()
    Entry(add,textvariable=last).grid(column=1,row=1)

    Label(add, text="Phone").grid(column=0, row=2)
    phone=StringVar()
    Entry(add,textvariable=phone).grid(column=1,row=2)

    Label(add, text="Major").grid(column=0, row=3)
    major=StringVar()
    Entry(add,textvariable=major).grid(column=1,row=3)
    Button(add, text="Add Student", command=lambda :addStudentHandler(
        first.get(),
        last.get(),
        phone.get(),
        major.get())).grid(column=0, row=5)
    Button(add, text="Cancel", command=add.destroy).grid(column=1, row=5)

def refresh(text):
    textStr=showStudentsStr()
    text.delete("1.0", "end")
    text.insert("end", textStr)

root = Tk()
frm = Frame(root)
frm.grid()

Label(frm, text="Current Students:").grid(column=0, row=0)

students=Text(frm,height=20, width=80)
students.grid(column=0,row=1,columnspan=4)
refresh(students)
Button(frm, text="Add", command=lambda :addStudent(root)).grid(column=0, row=2)
Button(frm, text="Delete", command=quit).grid(column=1, row=2)
Button(frm, text="Update", command=quit).grid(column=2, row=2)
Button(frm, text="Find", command=quit).grid(column=3, row=2)

Button(frm, text="Refresh", command=lambda :refresh(students)).grid(column=0, row=3)
Button(frm, text="Done", command=quit).grid(column=3, row=3)

root.mainloop()

