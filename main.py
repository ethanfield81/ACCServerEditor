import json
import tkinter as tk
import tkinter.ttk as ttk
import jsonClasses as jc
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu


window = tk.Tk()
window.title("ACC Server Editor")
window.geometry('800x600')

# first thing is indentify server folder
lbl = tk.Label(window, text = "beans", font = ("Comic Sans",11))
lbl.grid(column = 1, row = 0)



def defineDirectory():
    dir = filedialog.askdirectory()
    lbl.config(text=dir)
    dir = dir+"/server/cfg/settings.json"
    with open(dir) as f:
        data = json.load(f)
    print(data)
    #f = open(dir)
    #print(f)
defineDirectory = tk.Button(window, text = "Find Directory", bg = "white", fg = "black", command = defineDirectory, font = ("Comic Sans",11))
defineDirectory.grid(column = 0, row = 0)

<<<<<<< HEAD
#notebook = tkinter.ttk.Notebook(window, )

=======
#import from folder, previous configuration
#instantiate new versions of JSONs, import over
notebook = ttk.Notebook(window)

#pack options for configJSON into frame
configFrame = tk.Frame(notebook)
#3 columns, varname, currentvalue, new value (box or selector)
currentConfigJSON = jc.configurationJSON()
currentConfigJSON.print()
#some sort of import step
udpLabel = tk.Label(configFrame, text = "UDP Port")
udpValue = tk.Label(configFrame, text = currentConfigJSON.getudpPort())
udpNew = tk.Entry(configFrame)
udpLabel.grid(column = 0, row = 0)
udpValue.grid(column = 1, row = 0)
udpNew.grid(column = 2, row = 0)

tcpLabel = tk.Label(configFrame, text = "TCP Port")
tcpValue = tk.Label(configFrame, text = currentConfigJSON.gettcpPort())
tcpNew = tk.Entry(configFrame)
tcpLabel.grid(column = 0, row = 1)
tcpValue.grid(column = 1, row = 1)
tcpNew.grid(column = 2, row = 1)

mcLabel = tk.Label(configFrame, text = "Maximum Connections")
mcValue = tk.Label(configFrame, currentConfigJSON.getmaxConnections())
mcNew = tk.Entry(configFrame)
mcLabel.grid(column = 0, row = 2)
mcValue.grid(column = 1, row = 2)
mcNew.grid(column = 2, row = 2)

lanLabel = tk.Label(configFrame, text = "Lan Discoverability")
lanValue = tk.Label(configFrame, text = jc.boolToText(currentConfigJSON.getlanDiscovery()))
lanNew = tk.Checkbutton(configFrame, variable = currentConfigJSON.getlanDiscovery())

configFrame.pack()


settingsFrame = tk.Frame(notebook)
settingsFrame.pack()
eventFrame = tk.Frame(notebook)
eventFrame.pack()

notebook.add(configFrame, text = "Configuration")
notebook.add(settingsFrame, text = "Settings")
notebook.add(eventFrame, text = "Event")

notebook.grid(column = 0, row = 2)
>>>>>>> b5b1edaaaf9bbd85eff619ed6ccae39ae22d5ea9

menu = tk.Menu(window) 
new_item = tk.Menu(menu) 
#new_item.add_command(label='New', command = clicked) 
#menu.add_cascade(label='File', menu=new_item) 
window.config(menu=menu)
window.mainloop()