#Q1
from tkinter import *
top=Tk()
lbl=Label(top,text='hello world')
lbl.pack()
btn=Button(top,text='exit',command=" ")
btn.pack()
top.mainloop()



#ques2
item=tkinter.Tk()
def close():
    item.destroy()
def write():
    x=Label(item,text="you clicked write button")
    x.pack()
item.title("GUI")
item.geometry("100x200")
b1=tkinter.Button(item,text="exit",command=close)
b1.pack()
b2=tkinter.Button(item,text="write",command=write)
b2.pack()
b1.place(x=40,y=100)
b2.place(x=40,y=40)
item.mainloop()




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

