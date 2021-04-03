# note: if this fails, try >pip uninstall matplotlib
# and then >pip install matplotlib
import functions

def main():
  #read the knowledge and save it in to a list of float vectors
  print("Loading data from txt:\n")
  data_file_txt = open("data_r2.txt", "r")
  list_Points_Knowledge = []
  for data in data_file_txt.readlines():
    data_x=float(data[0:3])
    data_y=float(data[4:7])
    print ("Vector added to knowledge list:",[data_x,data_y])
    list_Points_Knowledge.append([data_x,data_y])
  #close the data_file_txt
  data_file_txt.close() 
  print(functions.give_random_values())
  
if __name__=="__main__":
  main()
  