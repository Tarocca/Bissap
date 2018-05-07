import copy
from random import choice
from mecanique import verif_solution
from interface import affichage

def possibilites(plateau):
    '''
    Retourne tous les coups possibles jouables sur le plateau

    :param plateau: le plateau de jeu ou l'on veut connaitre
    les differents coups jouables
    :type plateau: list(list(string, ...), ...)
    :return : la liste des coups possible sous forme (ligne, colonne)
    :rtype: tuple(tuple(int, int), ...)
    '''

    pos = tuple()
    for x in range(len(plateau)):
        for y in range(len(plateau)):
            if plateau[x][y] == ' ':
                pos += ((x,y),)

    return pos

def random_pick(plateau,marque):
    '''
    Renvoie un coup jouable calculé de facon aleatoire sur le plateau

    :param plateau: le plateau de jeu sur lequel calculer le coup a jouer
    :type plateau: list(list(string, ...), ...)
    :return: le coup a jouer sous forme (ligne, colonne)
    :rtype: (int, int)
    '''
    coups = possibilites(plateau)
    return choice(coups)

def eval_plateau(plateau,marque,n):
    '''
    Fonction d'evaluation du plateau utilisée dans l'agorithme minimax

    :param plateau: le plateau de jeu a evaluer
    :type plateau: list(list(string, ...), ...)
    :param marque: la marque du joueur
    :type marque: string
    :param n: nombre de marque a aligné pour gagner la partie
    :type n: int
    :return: le score du plateau calculé
    :rtype: int
    '''

    res = verif_solution(plateau,n)
    if marque == 'x':
        marque_adversaire = 'o'
    else:
        marque_adversaire = 'x'
    score = 0
    if marque_adversaire in res:
        score = -1
    elif marque in res:
        score = 1


    return score

def coup_minmax(plateau, marque, profondeur=6):
    '''
    Applique la première itération de l'agorithme minmax sur la
    grille pour déterminer le coup optimal a jouer

    :param plateau: le plateau de jeu ou calculer le meilleur coup
    :type plateau: list(list(string, ...), ...)
    :param marque: marque du joueur
    :type marque: string
    :param profondeur: nombre de coups a simuler afin de determiner
    le meilleur
    :type profondeur: int
    '''
    pos = possibilites(plateau)
    new_plateaux = jouer_coups(plateau, pos, marque)

    eval_pos = [minmax(plat, marque, True, profondeur - 1) for plat in new_plateaux]

    eval_pos_dict = dict()
    for i, score in enumerate(eval_pos):
        eval_pos_dict[i] = score

    #On prend la clef max en comparant les valeurs du dictionnaire
    indx = max(eval_pos_dict, key=eval_pos_dict.get)
    return pos[indx]

def jouer_coups(grille, coups, marque):
    '''
    Simule les coups passé en argument sur la grille

    :param grille: plateau de jeu sur lequelle placer les coups
    :type grille: list(list(string, ...), ...)
    :param coups: la liste des coups a simuler
    :type coups: tuple(tuple(int, int), ...)
    :param marque: marque du joueur a simuler sur la grille
    :type marque: string
    :return: les grilles simulées composées de la grille originale
    et des coups joués
    :rtype: list( list(list(string, ...),...), ... )
    '''
    new_grilles = [copy.deepcopy(grille) for po in coups]
    for i, plat in enumerate(new_grilles):
        plat[coups[i][0]][coups[i][1]] = marque

    return new_grilles

def minmax(plateau, marque, tour_oppossant, profondeur=2):
    '''
    Algorithme minmax qui permet de renvoyer le score associé
    au plateau de façon itérative

    :param plateau: le plateau de jeu a evaluer
    :type plateau: list(list(string, ...), ...)
    :param marque: marque du joueur
    :type marque: string
    :param tour_oppossant: spécifie s'il s'agit du tour de l'opposant
    (True) ou du tour du joueur (False)
    :type tour_oppossant: Bool
    :param profondeur: nombre de coups a simuler afin de determiner
    le score du plateau
    :type profondeur: int
    :return: le score du plateau
    :rtype: float
    '''

    if tour_oppossant:
        if marque == 'x':
            marque_adversaire = 'o'
        else:
            marque_adversaire = 'x'

    current_eval = eval_plateau(plateau, marque, len(plateau))
    pos = possibilites(plateau)

    # Condition d'arret
    if abs(current_eval) == 1 or len(pos) == 0 or profondeur == 0:
        return current_eval
    else:
        if tour_oppossant:
            new_plateaux = jouer_coups(plateau, pos, marque_adversaire)
        else:
            new_plateaux = jouer_coups(plateau, pos, marque)

        eval_pos = [minmax(plat, marque, not tour_oppossant, profondeur-1) for plat in new_plateaux]

        if not tour_oppossant:
            return max(eval_pos)
        else:
            return min(eval_pos)


if __name__=="__main__":
    plateau = [[' ', ' ', ' '],[' ', ' ', ' '],[' ',' ',' ']]
    print(possibilites(plateau))
    plateau = [['o', 'x', ' ', 'x'],[' ','x', 'x', ' '],[' ',' ','o','o'],[' ',' ','o','o']]
    print(possibilites(plateau))
