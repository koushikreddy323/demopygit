from tkinter import *
box=Tk()
box.geometry('200x200')
cb1=IntVar()
cb2=IntVar()
cb3=IntVar()
chbt1=Checkbutton(box,text='C',variable=cb1,onvalue=1,offvalue=0)
chbt2=Checkbutton(box,text='Java',variable=cb2,onvalue=1,offvalue=0)
chbt3=Checkbutton(box,text='Python',variable=cb3,onvalue=1,offvalue=0)
chbt1.place(x=20,y=10)
chbt2.place(x=20,y=30)
chbt3.place(x=20,y=50)
box.mainloop()