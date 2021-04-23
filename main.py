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
  MaxStep=5
  t=1
  LearnRestrictor=1
  #take the number of clusters
  number_of_clusters= 10
  #generate the clusters
  clustersList = functions.generate_random_list(number_of_clusters)
  listaClusterInicial= clustersList
  listModifCluster= []
  while( t < MaxStep):
    #just for test
    #plot_functions.plot_r2(list_points_Knowledge,clustersList)
    print("####################iteracion nro ", t)
    #for each known point in the data list
    for point in list_points_Knowledge:
      #get the winning centroid
      winning_centroid = functions.closest_weight(point,clustersList)
      #for each cluster in the cluster list
      for centroide in clustersList:
        #calculate the vicinity function
        vecinity_value= functions.vicinityImpactFunction(winning_centroid,centroide )
        print("*********************vecindad ",vecinity_value)
        #update the weights of each cluster
        centroide= functions.update_weight(winning_centroid ,point, vecinity_value , LearnRestrictor)
        print("ceeentroidee------------------------",centroide)
        #add the modified clusters to the auxiliary list
        listModifCluster.append(centroide)
        plot_functions.plot_r2(list_points_Knowledge,clustersList)
    #load the updated list to the cluster list
    #clustersList.clear()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    clustersList = listModifCluster
    #show iteration
    #plot_functions.plot_r2(list_points_Knowledge,clustersList)
    t+=1
    LearnRestrictor=1/t
    print("####################----------------------------------------iteracion nro ", t)
  #end algorithm
  #plot_functions.plot_r2(list_points_Knowledge,clustersList)
  print("los valores iniciales de los clusters son ",listaClusterInicial)
  print("los valores finales de los clusters son ",clustersList)
  
if __name__=="__main__":
  main()
  