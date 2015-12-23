from tkinter import *
from deleter_and_sorter import * 

#text_input = text_inp.get(1.0, END)
level = 1000 # max is 5990 sorry:c, min is 10
lang_nomb = 1
Quit = str("Quit")
Language = str("Language")
Label1 = str("Enter the Text")
Label2 = str("Difficult Words")
Button1 = str("Distinguish difficult words")

def distinguish_text():
    dif_words = sorter.distinguish(text_input)
    
def dist():
    w = txt_inp.get('1.0' , "end")
    l = distinguish(w, "frequency", level)
    txt_out.insert('end', l)
        
#Íàçâàíèå îêíà
root = Tk()
root.title("Ñëîæíûå òåêñòû")

#Ìåíþ
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label=Language, menu=file_menu)
file_menu.add_command(label="English")
file_menu.add_separator()
file_menu.add_command(label="Ðóññêèé")

edit_menu = Menu(menu)
menu.add_cascade(label=Quit, command=root.destroy)
frame = Frame(root)
frame.grid()

#Ëåéáëû
lbl = Label(frame, text=Label1)
lbl.grid(row=0, column=0)

lbl = Label(frame, text=Label2)
lbl.grid(row=0, column=1)

#Êíîïêà
btn = Button(frame, text=Button1, command = dist)
btn.grid(row=2, column=0)

#ââîä òåêñòà
txt_inp = Text(frame, width=50, height=30)
txt_inp.grid(row=1, column=0)

#âûâîä ñëîâ
txt_out = Text(frame, width=20, height=30)
txt_out.grid(row=1, column=1)


root.mainloop()
