def affichage (grille):
    """
       Fonction retournant un affichage esthétique de la grille de jeu du morpion supposément en 3x3
       :grille: grille de jeu
       :type grille: list
       :rtype: srting or list
    """
    c=0
    d=[]
    r=['*',' ','-',' ','-',' ','-',' ','-',' ','-',' ','-',' ','-','*',]
    for j in range (5):
        if j==0 or j==5:
            d.append(r)
        else:
            for i in range (len(grille)+1):
                if i ==0:
                    d[i]+='|'
                elif i==(len(grille)+1):
                    d[i]+='|\n'
                else:
                    d[i][j]+=grille[0]
    return d


#Test
print(affichage([('x ',' o',' x'),(' x',' o',' x'),(' x',' o',' x')]))
       
