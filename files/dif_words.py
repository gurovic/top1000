from Tkinter import *

Language = str("Language")
Quit = str("Quit")

#��������� ����

#

#�������� ����
root = Tk()
root.title("������� ������")

#����
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label=Language, menu=file_menu)
file_menu.add_command(label="English")
file_menu.add_separator()
file_menu.add_command(label="�������")

edit_menu = Menu(menu)
menu.add_cascade(label=Quit, command=root.destroy)
frame = Frame(root)
frame.grid()

lbl = Label(frame, text="������� �����")
lbl.grid(row=0, column=0)

lbl = Label(frame, text="������� �����")
lbl.grid(row=0, column=1)

btn = Button(frame, text="�������� ������� �����")
btn.grid(row=2, column=0)

#���� ������
txt_inp = Text(frame, width=100, height=50, )
txt_inp.grid(row=1, column=0)

#����� ����
txt_out = Text(frame, width=50, height=50)
txt_out.grid(row=1, column=1)

root.mainloop()