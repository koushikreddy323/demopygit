from tkinter import *
box=Tk()
txt1=Label(box,text="Login", font=("arial bold",35),fg='blue')
txt1.grid(column=1,row=0)
bt1=Label(box,text='Username',font=("courier",15))
bt1.grid(column=0,row=1)
bt2=Label(box,text='password',font=("courier",15))
bt2.grid(column=0,row=2)
bt3=Button(box,text='login',font=('courier',15),bg='black',fg='green')
bt3.grid(column=1,row=3)
ent=Entry(box).grid(column=1,row=1)
ent2=Entry(box).grid(column=1,row=2)
box.geometry('350x200')
box.mainloop()
