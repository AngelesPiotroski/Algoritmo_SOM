# need >pip install matplotlib
# encoding: utf-8
import functions

def main():
  #read the knowledge and save it in to a list of vectors:
  data_file_txt = open("data_r2.txt", "r")
  list_points_Knowledge=functions.load_from_txt(data_file_txt)
  
  #testing if the function list_points_Knowledge is returning a list from txt:
  #print(list_points_Knowledge)
  
  #testing the function closest_weight with a  Point[0,1] and list_points_Knowledge:
  #print("el nodo mas cercano a [0,1] es: ", functions.closest_weight([0,1],list_points_Knowledge))

  number_of_clusters = 2
  clustersList = []
  MaxStep=1000
  t=1
  #start algorithm
  #genering random values for the centroides at first time
  clustersList = functions.generate_random_list(number_of_clusters)
  
  
  while( t < MaxStep):
    
     t+=1
     LearnRestrictor=1/t
  #end algorithm
  
if __name__=="__main__":
  main()
  