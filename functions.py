import random

def give_random_values():
    return round(random.random(),2)

def euc_distance(p1, p2): 
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def closest_weight(point,centroides):
    #compare the distances between the centroides
    distanceCen1=euc_distance(point, centroides[0])
    distanceCen2=euc_distance(point, centroides[1])
    
    #return the centroide near to that point
    if distanceCen1 < distanceCen2:
        result=centroides[0]
    else:
        result=centroides[1]
    return result

def vicinityImpact(x,y):
    #based on the 'mexican hat function' https://lemnismath.org/2020/08/la-funcion-sombrero-mexicano/
    return (3*(math.sin((x**2)+(y**2))))/((x**2)+(y**2))

def update_weight(centroideWeightWinner, pointKnow, vicinityFunc,LearnRestrictor):
    #apply the formula for update winner weights
    weight_x=centroideWeightWinner[0]+vicinityFunc*LearnRestrictor*(pointKnow[0]-centroideWeightWinner[0])
    weight_y=centroideWeightWinner[1]+vicinityFunc*LearnRestrictor*(pointKnow[1]-centroideWeightWinner[1])