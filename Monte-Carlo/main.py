# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:00:49 2017

@author: Stephane Guinard
"""

from tirage_points import get_points_final
from distance_cercle import nb_points_sub_domain

# Main pour tester l'intégralité des codes

if __name__ == "__main__":
    # Choix du nombre de points
    n = 1000
    # Tirage des points
    points = tirage_points.get_points_final(n)
    # Calcul d'appartenance au cercle trigonométrique
    nb_points = distance_cercle.nb_points_sub_domain(points)
    # Calcul de pi
    
