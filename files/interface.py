from tkinter import *
def printing():
    print(text)

root = Tk()

im = PhotoImage(file = 'lol.gif')
back = Label(root, image = im)
textW = Text(root, height = 10, width = 23, font = 'Arial 14', wrap=WORD)

back.place(x=0, y=0)
textW.place(x=14, y=150)

but1 = Button(root, text = "print")
text = textW.get('1.0', END)
but1.bind("B1", printing)
but1.pack()
 
root.mainloop()
