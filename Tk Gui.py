from tkinter import *
window=Tk()
name=Label(window, text='Tkinter GUI',font=('courier',20))
name.grid(column=0,row=0)
bt=Button(window,text="Enter",font=('courier',15),bg='blue',fg='white')
bt2=Button(window,text="OK!",font=('courier',15),bg='Red',fg='gold')
bt2.grid(column=0,row=1)
bt.grid(column=0,row=2)
window.geometry('350x350')
window.mainloop()