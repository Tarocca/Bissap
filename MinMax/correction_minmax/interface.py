def affichage(plateau):
    '''
    Renvoie une chaine de caracteres comportant
    la grille de jeu dans un affichage normalisé

    :param plateau: la grille de jeu a afficher
    :type plateau: list(list(string, ...), ...)
    :return: la chaine a afficher
    :rtype: string
    '''
    size_plat = len(plateau)
    first_last = '*'+'-'*(2*size_plat+1)+'*'
    body = ''
    for ligne in plateau:
        body += '\n|'
        for case in ligne:
            body += ' ' + case
        body += ' |'

    return first_last + body +'\n' + first_last

def getinput():
    '''
    Récupère le coup d'un joueur

    :return: le coup du joueur
    :rtype: tuple(int, int)
    '''
    pos = input('Ou mettre la marque ? ')
    try:
        x, y = pos.split(',')
        x, y = int(x), int(y)
    except ValueError:
        print('Erreur lors de la saisie')
        return False
    else:
        return (x, y)


if __name__=="__main__":
    plateau = [[' ', ' ', ' '],[' ', ' ', ' '],[' ',' ',' ']]
    to_affiche = affichage(plateau)
    print(to_affiche)
    plateau = [['o', 'x', ' ', 'x'],[' ','x', 'x', ' '],[' ',' ','o','o'],[' ',' ','o','o']]
    to_affiche = affichage(plateau)
    print(to_affiche)
    x, y = getinput()
    plateau[x][y] = 'o'
    to_affiche = affichage(plateau)
    print(to_affiche)
