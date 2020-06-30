from tkinter import *
box=Tk()
box.geometry('350x350')
mb=Menubutton(box,text='Fuel of your vehicle')
mb.menu=Menu(mb)
mb['menu'] = mb.menu
mb.menu.add_command(label='Petrol',command=lambda:print('it is petrol'))
mb.menu.add_command(label='Diesel',command=lambda:print('it is diesel'))
mb.menu.add_command(label='Cng',command=lambda:print('it is cng'))
mb.pack()
box.mainloop()
