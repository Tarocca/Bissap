"""
Crée le Mardi d'un mois
@author: Chocolatine
"""

"""
Fonctions d'initialisation
"""
import tirage_points as tp
import distance_cercle as dc
import matplotlib.pyplot as plt
import numpy as np
"""
Script Du calcul de PI
"""
#Question 3.9
def calcul_pi(nb_points):
    Y=[]
    Y=tp.get_points_final(nb_points)
    X=dc.nb_points_sub_domain(Y)
    pi=4*(X/(nb_points))
    return pi
#Quetsion 3.10
"""
On remarque que pour avoir une valeur précise de pi on a besoin d'un trés grand nombre de points toutefois elle à le mérite d'^etre trés simple à réaliser avec nos ordinateurs actuels
"""
#Question 4.11
def show_points(X):
    x=[]
    y=[]
    for i in range (len(X)):
        x+=[X[i][0]]
        y+=[X[i][1]]
    plt.plot(x,y)
    plt.show()
    return

def aff_pi(nb_points):
    a=[]
    zx=[]
    zy=[]
    ya=[]
    xa=[]
    Y=tp.get_points_final(nb_points)
    for i in range (len(Y)):
        if dc.is_inside_circle(Y[i][0],Y[i][1]):
            zx+=[Y[i][0]]
            zy+=[Y[i][1]]
        else:
            xa+=[Y[i][0]]
            ya+=[Y[i][1]]
    g=[]
    t=np.linspace(0,1,0.1)
    for k in t:
        g+=[sqrt(1-k*k)]
    plt.plot(zx,zy,'r+',xa,ya,'b*',g,t,'b')
    plt.show()    
###TEST###
X=tp.get_points_final(10)
print(aff_pi(10000000))
