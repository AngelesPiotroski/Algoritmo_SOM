# encoding: utf-8
# importar todas las funciones de pylab
from pylab import *
from time import *
# importar el módulo pyplot
import matplotlib.pyplot as plt

def plot_r2(points_to_plot,centroides_to_plot):
    plt.ion()
    #plot atributes
    title('Valores')
    xlabel('Eje X')
    ylabel('Eje Y')
    #x list from points
    xArrayPoints = [point[0] for point in points_to_plot]
    #y list from points
    yArrayPoints= [point[1] for point in points_to_plot]
    #make a plot
    scatter(xArrayPoints,yArrayPoints, label='Puntos Conocimiento')
    #x list from centroides
    xArrayCentroide = [weight[0] for weight in centroides_to_plot]
    #x list from centroides
    yArrayCentroide= [weight[1] for weight in centroides_to_plot]
    #make a plot
    scatter(xArrayCentroide,yArrayCentroide, label='Pesos', marker = 'd')
    #make legend
    plt.legend(loc='upper left')
    plt.draw()
    plt.pause(0.5)
    plt.cla()

    

