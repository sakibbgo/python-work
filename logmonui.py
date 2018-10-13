import time, os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import threading





root = Tk() 
root.title("Log Monitor")
root.geometry("500x500")

labelText=StringVar()
labelText.set("Input String: ")
labelDir=Label(root, textvariable=labelText)
labelDir.pack()

directory=StringVar(None)

text = tk.Entry(root,textvariable=directory,width=30)
text.focus_set()
show = tk.Text(root,)

var =  ()    
def startLogMonitor():
    root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/sin/Desktop",title = "Select file",filetypes = (("All Files",".*"),("all files",".")))
    print (root.filename)
    filename = root.filename
    file = open(filename,'r')
    file.seek(0,2) # Go to the end of the file
    while 1:
        line = file.readline()
        if not line: # Sleep briefly
            continue
        else:
            if text.get() in line.lower(): 
                show = tk.Text(root,)
                show.insert(INSERT,line)
                show.pack() 
                messagebox.showinfo("Error", "We found a matching string in the log! Click Monitor Log again to continue logging.")
                time.sleep(15)
                show.destroy()
                break
                #tk.messagebox.showinfo("Error!", "See Log!")


def background(var):
    th = threading.Thread(target=startLogMonitor, args=var)
    th.start()


    
monitorButton = tk.Button(root, text = "Monitor Log", command=lambda: background(var))


text.pack()

monitorButton.pack()

root.mainloop()







