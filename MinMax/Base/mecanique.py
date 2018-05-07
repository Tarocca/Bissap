
def saisie_utilisateur(saisie):
    try:
        x=saisie.split(',')
    except ValueError:
        print("La saisie est invalide")
    except IndexError:
        print("Les valeurs sont invalides")

def coups_possible(grille):
    c=[]
    for i in range (len(grille)):
        for j in range (len(grille[0])):
            if grille[j][i]==' ':
                c+=[(i,j)]
    return c


            
            
    
    
        
    
























def verif_solution(grille,n):
    """
    Cherche dans la grille une combinaison de marques gagnantes.

    La fonction parcour la grille passée en argument et recherche un
    alignement vertical/horizontal ou digonal de n marques identiques.
    Il peut y avoir plusieurs marques gagnantes dans la grille

    :param grille: la grille a analyser
    :param n: le nombre de marques qui doivent etre alignees pour considerer
    la combinaison gagnante (souvent n = taille de la grille)
    :type grille: list(list(string, string, ...), ... )
    :type n: entier
    :return: renvoie la ou les marques gagnantes. Renvoie une list vide
    dans le cas ou il n'y a pas de gagnant
    :rtype: list(string, ...) ou list()
    """
    
    size_plat = len(plateau)
    winner = list()
    for x in range(size_plat):
        for y in range(size_plat):
            if plateau[x][y] == ' ':
                continue
            if size_plat - x >= n:
                comp = [plateau[x][y]==plateau[x+z][y] for z in range(n)]
                if False not in comp:
                    winner.append(plateau[x][y])
            if size_plat - y >= n:
                comp = [plateau[x][y]==plateau[x][y+z] for z in range(n)]
                if False not in comp:
                    winner.append(plateau[x][y])
            if size_plat - x >= n and size_plat - y >= n:
                comp = [plateau[x][y]==plateau[x+z][y+z] for z in range(n)]
                if False not in comp:
                    winner.append(plateau[x][y])
            if size_plat - x >= n and y+1 >= n:
                comp = [plateau[x][y]==plateau[x+z][y-z] for z in range(n)]
                if False not in comp:
                    winner.append(plateau[x][y])
    return winner


if __name__=='__main__':
    plateau = [['o', 'x', ' ', 'x'],['x','x', 'x', 'x'],[' ',' ','o','o'],[' ',' ','o','o']]
    print(verif_solution(plateau,4))
    plateau = [['x', 'x', ' ', 'x'],['x','x', 'x', 'o'],[' ',' ','x','o'],[' ',' ','o','o']]
    print(verif_solution(plateau,3))
    plateau = [['x', 'x', ' '],['x','o', 'x'],[' ',' ','x']]
    print(verif_solution(plateau,3))
    plateau = [['x', 'x', 'o'],['x','o', 'x'],['o',' ',' ']]
    print(verif_solution(plateau,3))

#Test

print(coups_possible([('x ',' ',' x'),(' ',' o',' x'),(' x',' o',' x')]))
