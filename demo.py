from tkinter import *
box=Tk()
txt1=Label(box,text="GUI created succesfully", font=("courier",20))
txt1.grid(column=1,row=0)
bt1=Button(box,text='Button 1',font=("courier",15),bg='Blue',fg='white')
bt1.grid(column=1,row=2)
bt2=Button(box,text='Button 2',font=("courier",15),bg='Blue',fg='white')
bt2.grid(column=1,row=4)
box.geometry('450x200')
box.mainloop()
