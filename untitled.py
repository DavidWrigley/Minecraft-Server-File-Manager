# minecraft server config

# imports
import time
import threading
import Tkinter 

# begin
from Tkinter import *
from tkFileDialog import askopenfilename

# TK stuff
root=Tk()
root.title('Minecraft Config')

# callbacks
def Openfile():
	# open the file
	filename = askopenfilename()
	f = open(filename)

	# read the file
	AllData = f.readlines()
	f.close()
	
	for a in AllData:
		print a.split('=')

	# fill widgets
	generator_settings = Label(Paramframe, text = 'World Type')
	generator_settings.grid(row = 0, column = 0)

	op_permission_level = Label(Paramframe, text = 'Admin Permission')
	op_permission_level.grid(row = 1, column = 0)

	# initilise the frame
	# Addframe()

def Removeframe():
	# remove the parameter frame
	Paramframe.pack_forget()

# frames
Mainframe = Frame(root)
Mainframe.pack(side = TOP, padx = 10, pady = 10, fill = X)

Fileframe = Frame(Mainframe)
Fileframe.pack(side = TOP, fill = X)

Paramframe = Frame(Mainframe)
Paramframe.pack(side = TOP, fill = X)

# label
Welcomelabel = Label(Fileframe, text='Click to open the Minecraft Server File')
Welcomelabel.pack(side = LEFT)

Testlabel = Label(Paramframe, text = 'This is a Test')
Testlabel.pack(side = LEFT)

# buttons
Openbutton = Button(Fileframe, text = 'open',command = Openfile)
Openbutton.pack(side = LEFT)

# required
root.mainloop()