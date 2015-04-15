from tkinter import *
 
root = Tk()
im = PhotoImage(file='lol.gif')
l = Text(root,height=7,width=7,font='Arial 14',wrap=WORD)
l = Label(root, image=im)
l.pack()
 
root.mainloop()