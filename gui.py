from tkinter import *

class Main_window:
    root = Tk()
    root.title("Main Menú - SOM (Self-Organizing Map) - Stetson & Piotroski")
    pathDataSetFile = "Not selected."
    clustersNumber = 0
    
    def __init__(self):
        #inputs frame
        frame_inputs = LabelFrame(self.root, text="INITIAL VALUES", padx=50,pady=50)
        frame_inputs.grid(row=1, column=0)

        button_select_data_set = Button(frame_inputs, text = "Select DATA SET .txt file", width=25, command = lambda: self.setPathFile(label_data_set_path))
        button_select_data_set.pack()

        #clusters scale
        clusters_scale = Scale(frame_inputs, label="Select the number of clusters:", 
                            from_=1, to=10, orient=HORIZONTAL, length=200, command = lambda a: self.setClusterNumber(a,label_clusters))
        clusters_scale.pack()

        #values setted frame
        frame_values_selected = LabelFrame(self.root, text="SELECTED VALUES", padx=65,pady=71.5)
        frame_values_selected.grid(row=1, column=1)
        #data set path label
        label_data_set_path = Label(frame_values_selected, text="DATA SET path file: "+self.pathDataSetFile)
        label_data_set_path.pack()
        #number clusters label
        label_clusters = Label(frame_values_selected, text="Number of clusters selected: "+str(self.clustersNumber))
        label_clusters.pack()

    def setPathFile(self,label_data_set_path):
            from tkinter import filedialog
            self.pathDataSetFile = filedialog.askopenfilename(title="Select a data set",
                                                    filetypes = (("text files","*.txt"),("all files","*.*")))
            label_data_set_path.config(text="DATA SET path file: "+self.pathDataSetFile)
            

    def setClusterNumber(self,val,label_clusters):
        self.clustersNumber=val
        print(self.clustersNumber)
        label_clusters.config(text="Number of clusters selected: "+str(self.clustersNumber))
        
        
wn = Main_window()
wn.root.mainloop()