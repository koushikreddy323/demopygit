from tkinter import *
box=Tk()
box.geometry('350x350')
v=DoubleVar()
scale=Scale(box,variable=v,from_=1,to=50,orient=HORIZONTAL).pack(anchor=CENTER)
btn=Button(box,text='value',command=lambda :print(v.get())).pack(anchor=CENTER)
box.mainloop()