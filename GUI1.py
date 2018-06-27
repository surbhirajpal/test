#Q1
from tkinter import *
top=Tk()
lbl=Label(top,text='hello world')
lbl.pack()
btn=Button(top,text='exit',command=" ")
btn.pack()
top.mainloop()



#Q3
from tkinter import *
test=Tk()
frame=Frame(test)
frame.pack()
lbl=Label(test,text='working with frames')
lbl.pack()
button1=Button(frame,text='exit',fg='blue')
button1.pack()
button2=Button(frame,text='change label',fg='red')
button2.pack()
mainloop()



#Q4
from tkinter import *
master=Tk()
master.geometry("100x100")
Label(master,text='input').grid(row=0)
e1=Entry(master)
e1.grid(row=0,column=1)
mainloop()

