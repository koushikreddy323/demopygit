from tkinter import *
box=Tk()
box.geometry('200x200')
tx1=Label(box,text='List of country')
lst=Listbox(box)
lst.insert(1,'India')
lst.insert(2,'Australia')
lst.insert(3,'USA')
btn=Button(box,text='Delete',command=lambda function =lst:lst.delete(ANCHOR))
tx1.pack()
lst.pack()
btn.pack()

box.mainloop()
