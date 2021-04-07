import random
import math
# encoding: utf-8

def give_random_values():
    return round(random.random(),2)

def euc_distance(point, weightToCalcule): 
    return math.sqrt((point[0]-weightToCalcule[0])**2+(point[1]-weightToCalcule[1])**2)

def closest_weight(point, centroides):
    #define a empty list witch save the results of euclidean results
    allResultsEuclidean = []
    for w in centroides:
        print("calculating eucliden distance of", w , " = ", euc_distance(point,w)," and added to list of results")
        allResultsEuclidean.append(euc_distance(point,w))
    print("\n the min in the list of results is: ", min(allResultsEuclidean))
    #catching the index of the min result
    indexOfClosest = allResultsEuclidean.index(min(allResultsEuclidean))
    print("the posiition of the min is: ", indexOfClosest)
    #returning the centroide in the index of min result in allResultsEuclidean
    return (centroides[indexOfClosest])

def vicinityImpact(x,y):
    #based on the 'mexican hat function' https://lemnismath.org/2020/08/la-funcion-sombrero-mexicano/
    return (3*(math.sin((x**2)+(y**2))))/((x**2)+(y**2))
    #1 con la ganadora >1 <0 si no es la ganadora.  vecindad entre conjunto de pesos distancia entre conuntos de pesos y la ganadora
    
def update_weight(centroideWeightWinner, pointKnow, vicinityFunc,LearnRestrictor):
    #apply the formula for update winner weights
    weight_x=centroideWeightWinner[0]+vicinityFunc*LearnRestrictor*(pointKnow[0]-centroideWeightWinner[0])
    weight_y=centroideWeightWinner[1]+vicinityFunc*LearnRestrictor*(pointKnow[1]-centroideWeightWinner[1])
    centroide_weight_Updated=(weight_x,weight_y)
    return centroide_weight_Updated