from tkinter import *
box=Tk()
box.geometry('600x400')
lf1=LabelFrame(box,text='Positive comments')
lf1.pack(fill='both',expand='yes')

top=Label(lf1,text='Add positive comments here...')
top.pack()

lf2=LabelFrame(box,text='Negative comments')
lf2.pack(fill='both',expand='yes')

btm=Label(lf2,text='Add negative comments here...')
btm.pack()

box.mainloop()