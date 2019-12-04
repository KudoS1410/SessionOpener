import tkinter as tk
from tkinter import filedialog, Text
import os # for running the apps
import subprocess, sys

opener ="open" if sys.platform == "darwin" else "xdg-open"
apps = []

if os.path.isfile("data.txt"):
	with open("data.txt", 'r') as f:
		for line in f:
			if line[0] == "/":
				line = line.strip()
				apps.append(line)

def add_app():

	for widget in frame.winfo_children() :
		widget.destroy()

	filename = filedialog.askopenfilename(initialdir = "/home/divyansh", title = "Select File",
	 filetypes = (("executables", "*.exe"), ("allfiles", "*.*")))

	apps.append(filename)

	for app in apps:
		label = tk.Label(frame, text = app, fg = "white", bg = "red")
		label.pack()
	pass

def run_apps():
	for app in apps:
		subprocess.call([opener, app])
		print(opener)

root = tk.Tk() # this is holds the whole gui

# our faviourite canvas
canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42") # this is the canvas with a background and initial size
canvas.pack() # this attaches it to the root

frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1) # now the frame changes with the canvas / gui resize
# the relx and rely are the paddings from the left
for app in apps:
	label = tk.Label(frame, text = app, fg = "white", bg = "red")
	label.pack()
	pass
# the open file button
openfile = tk.Button(root, text = "Open File", fg = "white", bg = "#263D42", padx = 5, pady = 10, command = add_app)
openfile.pack() # this attaches it to the root and neither to the canvas or the frame

runapps = tk.Button(root, text = "Run Apps", fg = "white", bg = "#263D42", padx = 5, pady = 10, command = run_apps)
runapps.pack() 

root.mainloop() # this runs the gui

with open("data.txt" , 'w') as f:
	for app in apps:
		f.write(app + "\n")