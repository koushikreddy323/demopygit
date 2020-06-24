from tkinter import *
from tkinter import messagebox
box=Tk()
box.geometry('350x350')
tx1=Label(box,text='Name',font=('courier',15)).place(x=30,y=50)
tx=Label(box,text='Email',font=('courier',15)).place(x=30,y=90)
tx3=Label(box,text='password',font=('courier',15)).place(x=30,y=130)
bt1=Button(box,text='Sign up',font=('courier',13),fg='white',bg='blue').place(x=120,y=180)
ent1=Entry(box).place(x=180,y=50)
ent2=Entry(box).place(x=180,y=90)
ent3=Entry(box).place(x=180,y=130)

if messagebox.askyesno('Login','Do you continue to signup?')==TRUE:
     print('Yes')
     messagebox.showinfo('Login', 'Sign up success')

else:
    print('No')
    messagebox.showerror('Login','Signup terminated')


box.mainloop()

