# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:04:35 2017

@author: sguinard
"""
import tirage_points as tp
import distance_cercle as dc
from math import sqrt

def create_distrib(points):
    distrib=[]
    for i in range (len(points)):
        if dc.is_inside_circle(points[i][0],points[i][1]):
            distrib+=[1]
        else:
            distrib+=[0]
    return distrib
            
    """
        Fonction qui permet de créer une distribution 
        à partir d'un tirage aléatoire de points
        en fonction de leur appartenance ou non 
        au quart de cercle trigonométrique
    
        :param points: ensemble de points tirés aléatoirement
        :type points: liste(tuple(float,float),...)
        :return: distribution des points
        :rtype: liste(int)
    """
    pass
    
def moyenne(distrib):
    a=0
    for i in range (len(distrib)):
        a+=distrib[i]
    m=a/(len(distrib))
    return m
        
    """
        Fonction qui calcule la moyenne d'une distribution
    
        :param distrib: distribution de points
        :type distrib: liste(i
        nt)
        :return: moyenne de la distribution
        :rtype: float
    """
    pass

def variance(distrib):
    a=moyenne(distrib)
    y=0
    for i in range (len(distrib)):
        y+=(distrib[i]-(a**2))
    return y/(len(distrib))
print(moyenne(create_distrib(tp.get_points_final(5000))))
print(variance(create_distrib(tp.get_points_final(5000))))
m=1.96*sqrt(variance(create_distrib(tp.get_points_final(5000)))/5000)
d=2.58*sqrt(variance(create_distrib(tp.get_points_final(5000)))/5000)
print(m,d)
print(4*moyenne(create_distrib(tp.get_points_final(5000)))-m,4*moyenne(create_distrib(tp.get_points_final(5000)))+m)
print(4*moyenne(create_distrib(tp.get_points_final(5000)))-d,4*moyenne(create_distrib(tp.get_points_final(5000)))+d)
"""
        Fonction qui calcule la variance d'une distribution
        
        :param distrib: distribution de points
        :type distrib: liste(float)
        :return: variance de la distribution
        :rtype: float
"""
pass
    
"""if __name__ == "__main__":"""
