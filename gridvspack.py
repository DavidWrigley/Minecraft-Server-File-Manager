# minecraft server config

# imports
import time
import threading
import Tkinter 

# begin
from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename

# TK stuff
root=Tk()
root.title('Minecraft Config')

# globals
Rightsidewidth = 12
data = []

# callbacks
def Savefile():

	file_opts = options = {}
	options['filetypes'] = [('all files', '.*'), ('properties files', '.properties')]
	options['initialfile'] = 'server.properties'

	filename = asksaveasfilename(**file_opts)

	print filename

	if("server.properties" in filename):
		fsave = open(filename)
	else:
		print "incorrect file, try again"

		top = Toplevel()
		top.title("Incorrect File Name")

		msg = Message(top, text = "You can only save this file as a server.properties file, please try again", width = 400)
		msg.pack()

		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()

		return

	# save the data

	# sync the file

	# close the file
	fsave.close()

def Openfile():
	# open the file

	file_opts = options = {}
	options['filetypes'] = [('all files', '.*'), ('properties files', '.properties')]
	options['initialfile'] = 'server.properties'

	filename = askopenfilename(**file_opts)

	if("server.properties" in filename):
		fload = open(filename)
	elif(filename != ''):
		print "incorrect file, try again"

		top = Toplevel()
		top.title("Incorrect File Name")

		msg = Message(top, text = "Somehow you got around my file name restrictions, well done, have a cookie (please dont do it again, you may break your server, just choose the right file)", width = 400)
		msg.pack()

		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()
		return
	else:
		return

	# read the file
	AllData = fload.readlines()

	# close the file
	fload.close()
	
	for a in AllData:
		print a.split('=')
		data.append(a.split('='))

	# creat the grid
	for x in range(2):
		Grid.columnconfigure(Paramframe,x,weight=1)
	for y in range(10):
		Grid.rowconfigure(Paramframe,y,weight=1)

	# change the label and button to saving.
	Openbutton.config(text = 'Save', command = Savefile)
	Welcomelabel.config(text = 'Click to Save the Minecraft Server File') 

	# fill widgets
	generator_settings = Label(Paramframe, text = 'Generator Type')
	generator_settings.grid(row = 1, sticky = W)

	generator_settings_entry = Entry(Paramframe, width = Rightsidewidth)
	generator_settings_entry.grid(row = 1, column = 1, sticky = E)
	generator_settings_entry.insert(0,data[2][1])

	op_permission_level = Label(Paramframe, text = 'Admin Permission')
	op_permission_level.grid(row = 2, sticky = W)

	op_permission_level_varable = StringVar(root)
	op_permission_level_varable.set(data[3][1])
	op_permission_level_drop = OptionMenu(Paramframe, op_permission_level_varable, "1", "2", "3", "4")
	op_permission_level_drop.config(width = Rightsidewidth)
	op_permission_level_drop.grid(row = 2, column = 1, sticky = E)

	allow_nether = Label(Paramframe, text = 'Enable Nether')
	allow_nether.grid(row = 3, sticky = W)

	allow_nether_varable = StringVar(root)
	allow_nether_varable.set(data[4][1])
	allow_nether_drop = OptionMenu(Paramframe, allow_nether_varable, "true", "false")
	allow_nether_drop.config(width = Rightsidewidth)
	allow_nether_drop.grid(row = 3, column = 1, sticky = E)

	level_name = Label(Paramframe, text = 'World Name')
	level_name.grid(row = 4, sticky = W)

	level_name_entry = Entry(Paramframe, width = Rightsidewidth)
	level_name_entry.grid(row = 4, column = 1, sticky = E)
	level_name_entry.insert(0,data[5][1])

	enable_query = Label(Paramframe, text = 'Server Query')
	enable_query.grid(row = 5, sticky = W)

	enable_query_varable = StringVar(root)
	enable_query_varable.set(data[6][1])
	enable_query_drop = OptionMenu(Paramframe, enable_query_varable, "true", "false")
	enable_query_drop.config(width = Rightsidewidth)
	enable_query_drop.grid(row = 5, column = 1, sticky = E)

	allow_flight = Label(Paramframe, text = 'Allow Flight')
	allow_flight.grid(row = 6, sticky = W)

	allow_flight_varable = StringVar(root)
	allow_flight_varable.set(data[7][1])
	allow_flight_drop = OptionMenu(Paramframe, allow_flight_varable, "true", "false")
	allow_flight_drop.config(width = Rightsidewidth)
	allow_flight_drop.grid(row = 6, column = 1, sticky = E)

	announce_achievements = Label(Paramframe, text = 'Broadcast Achievements')
	announce_achievements.grid(row = 7, sticky = W)

	announce_achievements_varable = StringVar(root)
	announce_achievements_varable.set(data[8][1])
	announce_achievements_drop = OptionMenu(Paramframe, announce_achievements_varable, "true", "false")
	announce_achievements_drop.config(width = Rightsidewidth)
	announce_achievements_drop.grid(row = 7, column = 1, sticky = E)

	server_port = Label(Paramframe, text = 'Server Port')
	server_port.grid(row = 8, sticky = W)

	server_port_entry = Entry(Paramframe, width = Rightsidewidth)
	server_port_entry.grid(row = 8, column = 1, sticky = E)
	server_port_entry.insert(0,data[9][1])

	level_type = Label(Paramframe, text = 'World Type')
	level_type.grid(row = 9, sticky = W)

	level_type_varable = StringVar(root)
	level_type_varable.set(data[10][1])
	level_type_drop = OptionMenu(Paramframe, level_type_varable, "DEFAULT", "FLAT", "LARGEBIOMES", "AMPLIFIED")
	level_type_drop.config(width = Rightsidewidth)
	level_type_drop.grid(row = 9, column = 1, sticky = E)

	enable_rcon = Label(Paramframe, text = 'Enable Remote Console')
	enable_rcon.grid(row = 10, sticky = W)

	enable_rcon_varable = StringVar(root)
	enable_rcon_varable.set(data[11][1])
	enable_rcon_drop = OptionMenu(Paramframe, enable_rcon_varable, "true", "false")
	enable_rcon_drop.config(width = Rightsidewidth)
	enable_rcon_drop.grid(row = 10, column = 1, sticky = E)

	level_seed = Label(Paramframe, text = 'Seed')
	level_seed.grid(row = 11, sticky = W)

	level_seed_entry = Entry(Paramframe, width = Rightsidewidth)
	level_seed_entry.grid(row = 11, column = 1, sticky = E)
	level_seed_entry.insert(0,data[12][1])

	force_gamemode = Label(Paramframe, text = 'Force Gamemode')
	force_gamemode.grid(row = 12, sticky = W)

	force_gamemode_varable = StringVar(root)
	force_gamemode_varable.set(data[13][1])
	force_gamemode_drop = OptionMenu(Paramframe, force_gamemode_varable, "true", "false")
	force_gamemode_drop.config(width = Rightsidewidth)
	force_gamemode_drop.grid(row = 12, column = 1, sticky = E)

	server_ip = Label(Paramframe, text = 'Server IP')
	server_ip.grid(row = 13, sticky = W)

	server_ip_entry = Entry(Paramframe, width = Rightsidewidth)
	server_ip_entry.grid(row = 13, column = 1, sticky = E)
	server_ip_entry.insert(0,data[14][1])

	max_build_height = Label(Paramframe, text = 'Max Build Height')
	max_build_height.grid(row = 14, sticky = W)

	max_build_height_entry = Entry(Paramframe, width = Rightsidewidth)
	max_build_height_entry.grid(row = 14, column = 1, sticky = E)
	max_build_height_entry.insert(0,data[15][1])

	spawn_npcs = Label(Paramframe, text = 'Spawn NPCS')
	spawn_npcs.grid(row = 15, sticky = W)

	spawn_npcs_varable = StringVar(root)
	spawn_npcs_varable.set(data[16][1])
	spawn_npcs_drop = OptionMenu(Paramframe, spawn_npcs_varable, "true", "false")
	spawn_npcs_drop.config(width = Rightsidewidth)
	spawn_npcs_drop.grid(row = 15, column = 1, sticky = E)

	white_list = Label(Paramframe, text = 'Player White List')
	white_list.grid(row = 16, sticky = W)

	white_list_varable = StringVar(root)
	white_list_varable.set(data[17][1])
	white_list_drop = OptionMenu(Paramframe, white_list_varable, "true", "false")
	white_list_drop.config(width = Rightsidewidth)
	white_list_drop.grid(row = 16, column = 1, sticky = E)

	spawn_animals = Label(Paramframe, text = 'Spawn Animals')
	spawn_animals.grid(row = 17, sticky = W)

	spawn_animals_varable = StringVar(root)
	spawn_animals_varable.set(data[18][1])
	spawn_animals_drop = OptionMenu(Paramframe, spawn_animals_varable, "true", "false")
	spawn_animals_drop.config(width = Rightsidewidth)
	spawn_animals_drop.grid(row = 17, column = 1, sticky = E)

	hardcore = Label(Paramframe, text = 'Enable Hardcore Mode')
	hardcore.grid(row = 18, sticky = W)

	hardcore_varable = StringVar(root)
	hardcore_varable.set(data[19][1])
	hardcore_drop = OptionMenu(Paramframe, hardcore_varable, "true", "false")
	hardcore_drop.config(width = Rightsidewidth)
	hardcore_drop.grid(row = 18, column = 1, sticky = E)

	snooper_enabled = Label(Paramframe, text = 'Enable Snooper')
	snooper_enabled.grid(row = 19, sticky = W)

	snooper_enabled_varable = StringVar(root)
	snooper_enabled_varable.set(data[20][1])
	snooper_enabled_drop = OptionMenu(Paramframe, snooper_enabled_varable, "true", "false")
	snooper_enabled_drop.config(width = Rightsidewidth)
	snooper_enabled_drop.grid(row = 19, column = 1, sticky = E)

	online_mode = Label(Paramframe, text = 'Enable Online Mode')
	online_mode.grid(row = 20, sticky = W)

	online_mode_varable = StringVar(root)
	online_mode_varable.set(data[21][1])
	online_mode_drop = OptionMenu(Paramframe, online_mode_varable, "true", "false")
	online_mode_drop.config(width = Rightsidewidth)
	online_mode_drop.grid(row = 20, column = 1, sticky = E)

	resource_pack = Label(Paramframe, text = 'Resource Pack URL')
	resource_pack.grid(row = 21, sticky = W)

	resource_pack_entry = Entry(Paramframe, width = Rightsidewidth)
	resource_pack_entry.grid(row = 21, column = 1, sticky = E)
	resource_pack_entry.insert(0,data[22][1])

	pvp = Label(Paramframe, text = 'Enable PVP')
	pvp.grid(row = 22, sticky = W)

	pvp_varable = StringVar(root)
	pvp_varable.set(data[23][1])
	pvp_drop = OptionMenu(Paramframe, pvp_varable, "true", "false")
	pvp_drop.config(width = Rightsidewidth)
	pvp_drop.grid(row = 22, column = 1, sticky = E)

	difficulty = Label(Paramframe, text = 'Difficulty Setting')
	difficulty.grid(row = 23, sticky = W)

	difficulty_varable = StringVar(root)

	# check and set
	if(data[24][1] == "0\n"):
		difficulty_varable.set("0 - Peaceful")
	elif(data[24][1] == "1\n"):
		difficulty_varable.set("1 - Easy")
	elif(data[24][1] == "2\n"):
		difficulty_varable.set("2 - Normal")
	elif(data[24][1] == "3\n"):
		difficulty_varable.set("3 - Hard")

	difficulty_drop = OptionMenu(Paramframe, difficulty_varable, "0 - Peaceful", "1 - Easy", "2 - Normal", "3 - Hard")
	difficulty_drop.config(width = Rightsidewidth)
	difficulty_drop.grid(row = 23, column = 1, sticky = E)

	enable_command_block = Label(Paramframe, text = 'Enable Command Block\'s')
	enable_command_block.grid(row = 24, sticky = W)

	enable_command_block_varable = StringVar(root)
	enable_command_block_varable.set(data[25][1])
	enable_command_block_drop = OptionMenu(Paramframe, enable_command_block_varable, "true", "false")
	enable_command_block_drop.config(width = Rightsidewidth)
	enable_command_block_drop.grid(row = 24, column = 1, sticky = E)

	gamemode = Label(Paramframe, text = 'Gamemode')
	gamemode.grid(row = 25, sticky = W)

	gamemode_varable = StringVar(root)

	# check and set
	if(data[26][1] == "0\n"):
		gamemode_varable.set("0 - Survival")
	elif(data[26][1] == "1\n"):
		gamemode_varable.set("1 - Creative")
	elif(data[26][1] == "2\n"):
		gamemode_varable.set("2 - Adventure")

	gamemode_drop = OptionMenu(Paramframe, gamemode_varable, "0 - Survival", "1 - Creative", "2 - Adventure")
	gamemode_drop.config(width = Rightsidewidth)
	gamemode_drop.grid(row = 25, column = 1, sticky = E)

	player_idle_timeout = Label(Paramframe, text = 'Player Timeout')
	player_idle_timeout.grid(row = 26, sticky = W)

	player_idle_timeout_entry = Entry(Paramframe, width = Rightsidewidth)
	player_idle_timeout_entry.grid(row = 26, column = 1, sticky = E)
	player_idle_timeout_entry.insert(0,data[27][1])

	max_players = Label(Paramframe, text = 'Maximum Players')
	max_players.grid(row = 27, sticky = W)

	max_players_entry = Entry(Paramframe, width = Rightsidewidth)
	max_players_entry.grid(row = 27, column = 1, sticky = E)
	max_players_entry.insert(0,data[28][1])

	spawn_monsters = Label(Paramframe, text = 'Spawn Monsters')
	spawn_monsters.grid(row = 28, sticky = W)

	spawn_monsters_varable = StringVar(root)
	spawn_monsters_varable.set(data[29][1])
	spawn_monsters_drop = OptionMenu(Paramframe, spawn_monsters_varable, "true", "false")
	spawn_monsters_drop.config(width = Rightsidewidth)
	spawn_monsters_drop.grid(row = 28, column = 1, sticky = E)

	generate_structures = Label(Paramframe, text = 'Generate Structures')
	generate_structures.grid(row = 29, sticky = W)

	generate_structures_varable = StringVar(root)
	generate_structures_varable.set(data[30][1])
	generate_structures_drop = OptionMenu(Paramframe, generate_structures_varable, "true", "false")
	generate_structures_drop.config(width = Rightsidewidth)
	generate_structures_drop.grid(row = 29, column = 1, sticky = E)

	view_distance = Label(Paramframe, text = 'View Distance')
	view_distance.grid(row = 30, sticky = W)

	view_distance_entry = Entry(Paramframe, width = Rightsidewidth)
	view_distance_entry.grid(row = 30, column = 1, sticky = E)
	view_distance_entry.insert(0,data[31][1])

	motd = Label(Paramframe, text = 'Server Name')
	motd.grid(row = 31, sticky = W)

	motd_entry = Entry(Paramframe, width = Rightsidewidth)
	motd_entry.grid(row = 31, column = 1, sticky = E)
	motd_entry.insert(0,data[32][1])

def Removeframe():
	# remove the parameter frame
	Paramframe.grid_forget()

# frames
Mainframe = Frame(root, width = 400)
Mainframe.pack(side = TOP, padx = 10, pady = 10, fill = None, expand = False)

Fileframe = Frame(Mainframe, width = 380)
Fileframe.grid(row = 0, column = 0)

Paramframe = Frame(Mainframe, width = 380)
Paramframe.grid(row = 1, column = 0)

# label
Welcomelabel = Label(Fileframe, text='Click to Open the Minecraft Server File')
Welcomelabel.grid(row = 0, column = 0)

# buttons
Openbutton = Button(Fileframe, text = 'Open',command = Openfile, width = (Rightsidewidth-2))
Openbutton.grid(row = 0, column = 1)

# required
root.mainloop()