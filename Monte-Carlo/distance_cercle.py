
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:18:17 2017

@author: Stephane Guinard
"""

import tirage_points
from math import sqrt

#-- QUESTION 2.5 --#
def compute_distance(x_point,y_point,x_circle,y_circle):
        X=x_point-x_circle
        Y=y_point-y_circle
        Z=sqrt(X**2+Y**2)
        return Z
        
        """
            Calcul la distance euclidienne entre les points (x_point, y_point)
            et (x_circle, y_circle)

            :param x_point: abscisse du premier point
            :type x_point: float
            :param y_point: ordonne du premier point
            :type y_point: float
            :param x_circle: abscisse du second point
            :type x_circle: float
            :param y_circle: ordonne du second point
            :type y_circle: float
            :return: la distance entre les deux points
            :rtype: float
        """
        
        pass

#-- QUESTION 2.6 --#
def is_inside_circle(x_point,y_point,x_circle=0,y_circle=0,r=1):
        y=compute_distance(x_point,y_point,x_circle,y_circle)
        if y<=r:
                return True
        return False
        """
            Determine si le point (x_point, y_point) a l'interieur du cercle
            de centre (x_circle, y_circle) et de rayon r

            :param x_point: abscisse du point
            :type x_point: float
            :param y_point: ordonne du point
            :type y_point: float
            :param x_circle: abscisse du centre du cercle
            :type x_circle: float
            :param y_circle: ordonne du centre du cercle
            :type y_circle: float
            :param r: rayon du cercle
            :type r: float
            :return: appartenance du point (x_point, y_point) au cercle
            :rtype: bool
        """
#-- QUESTION 3.8 --#    
def nb_points_sub_domain(points):
        c=0
        for i in range (len(points)):
                y=is_inside_circle(points[i][0],points[i][1])
                if y==True:
                        c+=1
        return c
"""
            Renvoie le nombre de point present dans le sous domain defini comme
            le cercle de centre (0,0) et de rayon 1

            :param points: les points dont l'on veut determiner l'appartenance
            au sous-domaine
            :type points: list(tuple(float, float), ... )
            :return: nombre de points dans le cercle
            :rtype: int
"""
# Tests unitaires
if __name__ == "__main__":

        #-- QUESTION 2.5 --#
    print('\nQuestion 2-5')
    print('Expected:\n0.0\n1.0\n0.64\nGet:')
    print(compute_distance(0.2, 0.2, 0.2, 0.2))
    print(compute_distance(1.0, 0.0, 0.0, 0.0))
    print(compute_distance(0.4, 0.5, 0.0, 0.0))

        #-- QUESTION 2.6 --#
    print('\nQuestion 2-6')
    print('Expected:\nTrue\nFalse\nGet:')
    print(is_inside_circle(0.5, 0.5, 0.0, 0.0, 1.0))
    print(is_inside_circle(0.9, 0.9, 0.0, 0.0, 1.0))
    
        #-- QUESTION 2.7 --#
    print('\nQuestion 2-7')
    print('Expected:\nTrue\nFalse\nGet:')
    print(is_inside_circle(0.5, 0.5))
    print(is_inside_circle(0.9, 0.9))
    
        #-- QUESTION 3.8 --#
    nb_points = 100
    print('\nQuestion 3-8')
    print('Expected:\nNombre de points dans le sous domaine = x\
 sur {} points au total\nGet:'.format(nb_points))
    points = tirage_points.get_points_final(nb_points)
    n = nb_points_sub_domain(points)
    print('Nombre de points dans le sous domaine = {}\
 sur {} points au total'.format(n, nb_points))
