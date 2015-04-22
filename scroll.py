from Tkinter import *

editorWindow = Tk()

scroll = Scrollbar(editorWindow)
scroll.grid(sticky = E+W+S+N, row = 4, column = 3)
editCanvas = Canvas(editorWindow, bd = 0, yscrollcommand = scroll.set,
height = 300)
editCanvas.grid(sticky = E+W+S+N, row = 4, column = 0, columnspan = 3)

i = 0
for i in range(100):
       Button(editCanvas, <...>).grid(row = i, column = 0)
       Entry(editCanvas, <...>).grid(row = i, column = 1)
       Entry(editCanvas, <...>).grid(row = i, column = 2)
       Entry(editCanvas, <...>).grid(row = i, column = 3)

scroll.config(command = editCanvas.yview)
editCanvas.config(scrollregion=editCanvas.bbox(ALL))
editCanvas.config(height = 30)

editorWindow.mainloop()
