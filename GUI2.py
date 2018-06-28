import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
d={'a':'8872296040',
   'b':'1234567890',
   'c':'0987654321'}


def cmd():
    x=b1.get()
    y=b2.get()
    mylist.insert(END, "name " + str(x))
    mylist.insert(END, "phone " + str(y))
    b1.delete(0,END)
    b2.delete(0,END)

#Q1

master=Tk()
frame=Frame(master)
frame.pack()
master.title("scroll bar")
master.geometry('300x200')
s=Scrollbar(master)
s.pack(side=RIGHT,fill=Y)
mylist=Listbox(master,yscrollcommand=s.set)
for i in d:
    mylist.insert(END,"name "+ str(i))
    mylist.insert(END,"phone "+str(d[i]))
mylist.pack(side=LEFT,fill=BOTH)
s.config(command=mylist.yview)


#Q2

name=Label(master,text='NAME')
name.pack()
b1=Entry(master)
b1.pack()
phone=Label(master,text='PHONE NUMBER')
phone.pack()
b2=Entry(master)
b2.pack()
x=Button(frame,text='INSERT',command=cmd)
x.pack()
mainloop()
