# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:02:05 2017

@author: Stephane Guinard
"""
from random import random as rand
#-- QUESTION 1.1 --#
def get_random_point():
    X,Y = rand(),rand()
    return X,Y
    """
        Renvoie un point qui a pour coordonnees deux chiffres aleatoires compris entre
        0 et 1.
    
        :return: un tuple composé de l'abscisse et de l'ordonné du point
        :rtype: tuple(float, float)
    """
    
    pass

#-- QUESTION 1.2 --#
def get_10_points():
    point=[]
    for i in range (10):
        point+=[get_random_point()]
    return point
        
    """
        Renvoie 10 points generes de facon aleatoire.

        :return: une liste de points
        :rtype: list( tuple(float, float), ... )
    """
    
    pass

#-- QUESTION 1.3 --#
def get_points(nb_points):
    point=[]
    for i in range (nb_points):
        point+=[get_random_point()]
    return point
    """
        Renvoie nb_point points generes de facon aleatoire.

        :param nb_points: nombre de point à tirer
        :type nb_point: int
        :return: list_points : une liste de points
        :rtype: list( tuple(float, float), ... )
    """

    pass

#-- QUESTION 1.4 --#
def get_points_final(nb_points=10, display=True):
    point=[]
    for i in range (nb_points):
        point+=[get_random_point()]
    if display==True:
        return point
    return
    """
        Renvoie nb_point points generes de facon aleatoire. L'argument display permet,
        ou non, d'afficher les points generes

        :param nb_points: nombre de point à tirer
        :type nb_point: int
        :param display: affiche ou non les points tires
        :type: bool
        :return: list_points : une liste de points
        :rtype: list( tuple(float, float), ... )
    """

    pass


# Tests
if __name__ == "__main__":
    
    #-- QUESTION 1.1 --#
    print('\nQuestion 1-1')
    print('Expected:\n(0.x, 0.x)\nGet:')
    p = get_random_point()
    print(p)

    #-- QUESTION 1.2 --#
    print('\nQuestion 1-2')
    print('Expected:\n[(0.x, 0.x), (0.x, 0.x), ... , (0.x, 0.x)] 10 times\nGet:')
    list_p = get_10_points()
    print(list_p)

    #-- QUESTION 1.3 --#
    num_points = 8
    print('\nQuestion 1-3')
    print('Expected:\[(0.x, 0.x), (0.x, 0.x), ... , (0.x, 0.x)] {} times\nGet:'.format(num_points))
    list_p = get_points(num_points)
    print(list_p)
    
    #-- QUESTION 1.4 --#
    print('\nQuestion 1-4')
    print('Expected:\nPoint 1 = (0.x, 0.x); Point 2 = (0.x, 0.x); ... {}\
          \n[(0.x, 0.x), (0.x, 0.x), ... , (0.x, 0.x)] {} times\nGet:'.format(num_points,num_points))
    list_p = get_points_final(num_points, True)
    print(list_p)
    print('\nExpected:\n[(0.x, 0.x), (0.x, 0.x), ... , (0.x, 0.x)] 10 times\nGet:')
    list_p = get_points_final() #Default params
    print(list_p)

