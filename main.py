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

currentConfigJSON = jc.configurationJSON()
currentSettingJSON = jc.settingsJSON()
currentEventJSON = jc.eventJSON()


def defineDirectory():
    dir = filedialog.askdirectory()
    lbl.config(text=dir)
    dirInput = lbl.cget("text")
    print(dirInput)
    #make config object
    currentConfigJSON.print()
    
    currentConfigJSON.importJSON(dirInput)
    #except:
    #    print("Whoopsie-daisy there buckaroo, input a valid directory.")
    #make settings event
    currentSettingJSON.print()

    try:
        currentSettingJSON.importJSON(dirInput)
    except:
        print("Whoopsie-daisy there buckaroo, input a valid directory.")

    #make event object
    currentEventJSON.print()
    try:
        currentEventJSON.importJSON(dirInput)
    except:
        print("Whoopsie-daisy there buckaroo, input a valid directory.")


    #dir = dir+"/server/cfg/settings.json"
    #with open(dir) as f:
    #    data = json.load(f)
    #print(json.dumps(data))
    #f = open(dir)
    #print(f)
    # I moved this to be a function within each JSON object, I'm thinking
    # that we'll try to get it to ask for a directory, if if finds the files within
    # that directory then it will import all of the settings from that directory. 
    # I think we should make the directory to look for the cfg folder though.
    # So that way you can save just that folder with the JSONs and load it from anywhere
defineDirectory = tk.Button(window, text = "Find Directory", bg = "white", fg = "black", command = defineDirectory, font = ("Comic Sans",11))
defineDirectory.grid(column = 0, row = 0)

#import from folder, previous configuration
#instantiate new versions of JSONs, import over
notebook = ttk.Notebook(window)

#pack options for configJSON into frame
configFrame = tk.Frame(notebook)
#3 columns, varname, currentvalue, new value (box or selector)

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
mcValue = tk.Label(configFrame, text = currentConfigJSON.getmaxConnections())
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

menu = tk.Menu(window) 
new_item = tk.Menu(menu) 
#new_item.add_command(label='New', command = clicked) 
#menu.add_cascade(label='File', menu=new_item) 
window.config(menu=menu)
window.mainloop()