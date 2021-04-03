# need >pip install matplotlib

import functions

def main():
  #read the knowledge and save it in to a list of float vectors:
  data_file_txt = open("data_r2.txt", "r")
  list_points_Knowledge = []
  print("Loading data from txt:\n")
  for data in data_file_txt.readlines():
    data_x=float(data[0:3])
    data_y=float(data[4:7])
    print ("Vector added to knowledge list:",[data_x,data_y])
    list_points_Knowledge.append([data_x,data_y])
  data_file_txt.close() 

  #start the algorithm
  MaxStep=1000
  t=0
  while( t < 1000):
    
    t+=1
  
if __name__=="__main__":
  main()
  