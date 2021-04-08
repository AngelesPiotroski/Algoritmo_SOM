import math
import random
#encoding: utf-8

#return a list of vectors from the .txt
def load_from_txt(data_file_txt):
    #create a list
    list_points_Knowledge = []
    print("\n##############################################")
    print("# Loading data from txt:\t\t     #")
    #read a line from the .txt
    for data in data_file_txt.readlines():
        data_x=float(data[0:3])
        data_y=float(data[4:7])
        print ("# Vector added to knowledge list:",[data_x,data_y],"#")
        list_points_Knowledge.append([data_x,data_y])
    print("##############################################\n")
    #close the .txt file
    data_file_txt.close()
    return list_points_Knowledge 

#give random values like: a,bc
def give_random_values():
    return round(random.random(),2)

def generate_random_list(number_of_clusters):
    clustersList = []
    for i in range(number_of_clusters):
      clustersList.append([give_random_values(),give_random_values()])
    return clustersList

#return a euclidian distance from two points
def euc_distance(point, weightToCalcule): 
    result=math.sqrt((point[0]-weightToCalcule[0])**2+(point[1]-weightToCalcule[1])**2)
    return round(result,2)

#return the closest centroide according to a point
def closest_weight(point, centroides):
    #define a empty list witch save the results of euclidean results evaluating the point and the centroides(list)
    allResultsEuclidean = []
    #for any centroide calculate the euclidean distance
    for w in centroides:
        print("calculating eucliden distance of", w , " = ", euc_distance(point,w)," and added to list of results")
        allResultsEuclidean.append(euc_distance(point,w))
    print("\nthe min in the list of results is: ", min(allResultsEuclidean))
    #catching the index of the min result in allResultsEuclidean list (this tells us which element of the list of centroids is the minimum)
    indexOfClosest = allResultsEuclidean.index(min(allResultsEuclidean))
    print("the position of the min is: ", indexOfClosest, " (positions in vectors starts in cero)")
    #returning the centroide in the index of min result in allResultsEuclidean
    return (centroides[indexOfClosest]) 

#return the difference between two points in R2
def diff_r2(point1,point2):
    #this is like 'x1-x1', 'y1-y2' and return a vector with this result
    diff_result=[point1[0]-poin2[0],point1[1]-poin2[1]]
    return diff_result

#return the value from evaluate the function
def vicinityImpactFunction(centroideWeightWinner,centroideToUpdate):
    #1 con la ganadora >1 <0 si no es la ganadora.  vecindad entre conjunto de pesos distancia entre conuntos de pesos y la ganadora
    return (1/(1+diff_r2(centroideToUpdate,centroideWeightWinner)))
    
def update_weight(centroide, pointKnow, vicinityFunc,LearnRestrictor):
    #apply the formula for update weights
    weight_x=centroideWeightWinner[0]+vicinityImpactFunction*LearnRestrictor*(pointKnow[0]-centroideWeightWinner[0])
    weight_y=centroideWeightWinner[1]+vicinityImpactFunction*LearnRestrictor*(pointKnow[1]-centroideWeightWinner[1])
    centroide_weight_Updated=(weight_x,weight_y)
    return centroide_weight_Updated