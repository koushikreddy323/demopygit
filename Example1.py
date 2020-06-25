from tkinter import *
from tkinter import messagebox
box=Tk()
box.geometry('400x400')
def click():
    messagebox.showinfo('login','Login successful')

cvs=Canvas(box,bg='pink',height=400,width=400).pack()
tx1=Label(box,text='Login',font=('Arial bold',20),fg='green')
tx1.place(x=150,y=0)
tx2=Label(box,text='Email',font=('courier',15),fg='green')
tx2.place(x=40,y=50)
tx2=Label(box,text='password',font=('courier',15),fg='green')
tx2.place(x=40,y=90)
ent1=Entry(box)
ent2=Entry(box)
ent1.place(x=200,y=50)
ent2.place(x=200,y=90)
cb1=IntVar()
cbtn=Checkbutton(box,text='I Accept terms and conditions',variable=cb1,onvalue=1,offvalue=0)
cbtn.place(x=40,y=130)
bt1=Button(box,text='Login',font=('arial',15),fg='green',bg='orange',activebackground='red',command=click)
bt1.place(x=150,y=170)
box.mainloop()