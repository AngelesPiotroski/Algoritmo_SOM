# need >pip install matplotlib
# encoding: utf-8
import functions
import plot_functions

def main():
  #read the knowledge and save it in to a list of vectors:
  data_file_txt = open("data_r2.txt", "r")
  list_points_Knowledge=functions.load_from_txt(data_file_txt)

  #testing if the function list_points_Knowledge is returning a list from txt:
  #print(list_points_Knowledge)
  
  #testing the function closest_weight with a  Point[0,1] and list_points_Knowledge:
  #print("el nodo mas cercano a [0,1] es: ", functions.closest_weight([0,1],list_points_Knowledge))

  #start algorithm

  clustersList = []
  MaxStep=3000
  t=1
  LearnRestrictor=1
  #take the number of clusters
  number_of_clusters= 10
  #generate the clusters
  clustersList = functions.generate_random_list(number_of_clusters)
  listaClusterInicial= clustersList
  while( t < MaxStep):
    #just for test
    #plot_functions.plot_r2(list_points_Knowledge,clustersList)
    #for each known point in the data list
    for point in list_points_Knowledge:
      #get the winning centroid
      winning_centroid = functions.closest_weight(point,clustersList)
      #for each cluster in the cluster list
      for centroide in clustersList:
        #calculate the vicinity function
        vecinity_value_X= functions.vicinityImpactFunctionInX(winning_centroid,centroide )
        vecinity_value_Y= functions.vicinityImpactFunctionInY(winning_centroid,centroide )
        round(vecinity_value_X,2)
        round(vecinity_value_Y,2)
        #update the weights of each cluster
        #print("el viejo valor del centroide es ",centroide)
        centroide= functions.update_weight(winning_centroid , point, vecinity_value_X,vecinity_value_Y , LearnRestrictor)
        #print("el nuevo valor del centroide es ",centroide)
        
    #show iteration
    t+=1
    LearnRestrictor=1/t
    print("####################----------------------------------------iteracion nro ", t)
    print("####################----------------------------------------el lear es  ", LearnRestrictor)

  #end algorithm
  plot_functions.plot_r2(list_points_Knowledge,clustersList)
  print("los valores iniciales de los clusters son ",listaClusterInicial)
  print("los valores finales de los clusters son ",clustersList)
  
if __name__=="__main__":
  main()
  