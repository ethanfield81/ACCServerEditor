import json
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu


window = tk.Tk()
window.title("ACC Server Editor")
window.geometry('800x600')

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

#notebook = tkinter.ttk.Notebook(window, )


menu = tk.Menu(window) 
new_item = tk.Menu(menu) 
#new_item.add_command(label='New', command = clicked) 
#menu.add_cascade(label='File', menu=new_item) 
window.config(menu=menu)
window.mainloop()