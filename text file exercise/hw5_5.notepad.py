from tkinter import*
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *



root=Tk()
root.title("Untitled - Notepad")
m=Menu(root)
TextArea = Text(root)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Add controls (widget)
TextArea.grid(sticky = N + E + S + W)
#################
def display():

    label=Label(text="you selected an option")
    label.pack()
##################
def openFile():
    global filePath

    filePath = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
    if filePath == "":
        # no file to open
        filePath = None
    else:
        # Try to open the file
        # set the window title
        root.title(os.path.basename(filePath) + " - Notepad")
        TextArea.delete(1.0, END)

        file = open(filePath, "r")

        TextArea.insert(1.0, file.read())

        file.close()

#############################


filemenu=Menu(m)
filemenu.add_command(label="New",command=display)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As",command=display)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
m.add_cascade(label="File",menu=filemenu)
################################
editmenu=Menu(m)
editmenu.add_command(label="Cut",command=lambda:TextArea.event_generate("<<Cut>>"))
editmenu.add_command(label="Copy",command=lambda:TextArea.event_generate("<<Copy>>"))
editmenu.add_command(label="Paste",command=lambda:TextArea.event_generate("<<Paste>>"))
m.add_cascade(label="Edit",menu=editmenu)
################################
helpmenu=Menu(m)
helpmenu.add_command(label="About",command=display)
m.add_cascade(label="Help",menu=helpmenu)


#####################
root.config(menu=m)
mainloop()


