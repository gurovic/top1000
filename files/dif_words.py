from Tkinter import *

Language = str("Language")
Quit = str("Quit")

#выделение слов

#

#Название окна
root = Tk()
root.title("Сложные тексты")

#Меню
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label=Language, menu=file_menu)
file_menu.add_command(label="English")
file_menu.add_separator()
file_menu.add_command(label="Русский")

edit_menu = Menu(menu)
menu.add_cascade(label=Quit, command=root.destroy)
frame = Frame(root)
frame.grid()

lbl = Label(frame, text="Введите текст")
lbl.grid(row=0, column=0)

lbl = Label(frame, text="Сложные слова")
lbl.grid(row=0, column=1)

btn = Button(frame, text="Выделить сложные слова")
btn.grid(row=2, column=0)

#ввод текста
txt_inp = Text(frame, width=100, height=50, )
txt_inp.grid(row=1, column=0)

#вывод слов
txt_out = Text(frame, width=50, height=50)
txt_out.grid(row=1, column=1)

root.mainloop()