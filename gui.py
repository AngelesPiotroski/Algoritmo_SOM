from tkinter import *
import tkinter
from tkinter import filedialog
path = "No se ha selecionado data set"


def readFilePath():
    path=tkinter.filedialog.askopenfilename(title="Select a data set",filetypes = (("text files","*.txt"),("all files","*.*")))
    labelPathFile = tkinter.Label(wd, text=path)
    labelPathFile.grid(row=2, column=1)

#window
wd = tkinter.Tk()
wd.geometry("800x600")
#label file search
labelFilePath = tkinter.Label(wd, text="Seleccione la dirección del data set de formato .txt:")
labelFilePath.grid(row=0, column=0)
#Button file search
ButtonOpenDataSetFile = tkinter.Button(wd,text="Cargar Data Set", command=readFilePath)
ButtonOpenDataSetFile.grid(row=0, column=1)
#label clusters
labelClusterAsk = tkinter.Label(wd, text="Seleccione la cantidad de Clusters:")
labelClusterAsk.grid(row=1, column=0)
#spin for clusters number
sp = tkinter.Spinbox(wd, from_= 1, to = 100)
sp.grid(row=1, column=1)

wd.mainloop()