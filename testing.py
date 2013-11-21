import Tkinter
from Tkinter import *

root = Tk()
frame=Frame(root)
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)
frame.grid(row=0,column=0,sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame,7,weight=1)
Grid.columnconfigure(frame,0,weight=1)

#example values
for x in range(60):
    for y in range(30):
        btn = Button(frame)
        btn.grid(column=x, row=y)
for x in range(60):
  Grid.columnconfigure(frame,x,weight=1)
for y in range(30):
  Grid.rowconfigure(frame,y,weight=1)

root.mainloop()