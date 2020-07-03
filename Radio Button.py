from tkinter import *
box=Tk()
box.geometry('300x250')
lbl=Label(box,text='Select the language',fg='blue').pack()
v=IntVar()
rb1=Radiobutton(box,text='C',variable=v,value=1,command=lambda :print('selected value is',v.get())).place(x=50,y=50)
rb1=Radiobutton(box,text='Java',variable=v,value=2,command=lambda :print('selected value is',v.get())).place(x=50,y=80)
rb1=Radiobutton(box,text='Python',variable=v,value=3,command=lambda :print('selected value is',v.get())).place(x=50,y=110)
box.mainloop()