from mecanique import verif_solution
from interface import getinput, affichage
from ia import random_pick, coup_minmax, possibilites

def coup_joueur(coups_possibles):
    '''
    Renvoie le coup du joueur, en s'assurant qu'il s'agit
    bien d'un coup valable

    :param coups_possibles: liste des coups jouable
    :type coups_possibles: tuple(tuple(int, int), ...)
    :return: le coup du joueur
    :rtype: tuple(int, int)
    '''
    coord = getinput()
    while not coord or coord not in coups_possibles:
        coord = getinput()

    return coord
	

def jouer(size_tab, func_ia=None):
    '''
    Fonction principale de jeu.

    Cette fonction contient la boucle de jeu qui permet de jouer au morpion.
    La boucle s'arrete lorsqu'un joueur a gagné ou lorsque la grille est
    pleine.

    :param size_tab: taille de la grille de jeu
    :type size_tab: int
    :param func_ia: fonction permettant à l'ordinateur de jouer en choisisant un coup.
    Par défaut à None, c'est à dire que l'on joue contre un autre joueur humain
    :type func_ia: fonction
    '''

    # Initialisation de la grille de jeu
    tab = [[' ']*size_tab for x in range(size_tab)]

    #I nitialisation des joueurs humains ou ordinateurs
    if func_ia == None:
        joueur = {'x' :'joueur', 'o' : 'joueur'}
    else:
        joueur = {'x': 'joueur', 'o': 'ia'}

    
    num_joueur = len(joueur)
    cpt_joueur = 0
    end = False
    
    while not end:
        
        print(affichage(tab))
        print('Joueur {}'.format(list(joueur.keys())[cpt_joueur]))

        coups_possibles = possibilites(tab)

        if  list(joueur.values())[cpt_joueur] == 'joueur':
            # Coup joueur humain
            coup = coup_joueur(coups_possibles)
        else:
            # Coup joueur ordinateur
            coup = func_ia(tab,list(joueur.keys())[cpt_joueur])

        tab[coup[0]][coup[1]] = list(joueur.keys())[cpt_joueur]

        sol = verif_solution(tab,size_tab)
        # On regarde si un joueur a gagné
        if len(sol) != 0:
            end = True
            print("Gagnant : ", *sol)

        # On regarde si la grille est pleine
        if len(coups_possibles) == 1:
            end = True

        # On passe au joueur suivant
        cpt_joueur = (cpt_joueur + 1) % num_joueur

    print(affichage(tab))


if __name__=='__main__':
    jouer(3)
    jouer(3, random_pick)
    jouer(3, coup_minmax)

