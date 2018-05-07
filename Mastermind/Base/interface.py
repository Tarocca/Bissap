# -*- coding: utf-8 -*-
codes_couleurs = { "R" :0 , "B" :1 , "J" :2 , "V" :3 , "N" :4 , "M" :5 , "F" :6 , "O" :7}
couleurs_codes = {0: "R" , 1: "B" , 2: "J" , 3: "V" , 4: "N" , 5: "M" , 6: "F" , 7: "O" }
noms_couleurs = { "R" : "Rouge" , "B" : "Bleu" , "J" : "Jaune" , "V" : "Vert" , "N" : \
                  "Noir" , "M" : "Marron" , "F" : "Fushia" , "O" : "Orange" }


#-- QUESTION 1 --#
def affiche_indications(nb_places, nb_couleurs, proposition):
    prop=""
    for i in range (4):
        prop+=couleurs_codes[proposition[i]]
    print("Il y a",nb_places,"pions bien placés\nIl y a",nb_couleurs,"bonnes couleurs\nLa proposition du joueur était",prop)
    """
        Affiche un rappel de la proposition du joueur, suivi du nombre
        de pions bien placé et du nombre de bonnes couleurs
    
        :param nb_places: nombre de pion bien placé
        :type nb_places: int
        :param nb_couleurs: nombre de bonnes couleurs
        :type nb_couleurs: int
        :param proposition: la proposition du joueur
        :type proposition: list(int, ...)
    """
    
    pass

#-- QUESTION 2 --#
def affiche_jolies_indications(nb_places, nb_couleurs, proposition):
    a,b,prop="","",""
    for i in range (nb_places):
        b+=" *"
    for i in range(nb_couleurs):
        a+=" *"
    for i in range (len(proposition)):
        prop+=couleurs_codes[proposition[i]]
    print(a,prop,b)
    """
        Affiche un rappel esthetique de la proposition du joueur.
    
        :param nb_places: nombre de pion bien placé
        :type nb_places: int
        :param nb_couleurs: nombre de bonnes couleurs
        :type nb_couleurs: int
        :param proposition: la proposition du joueur
        :type proposition: list(int, ...)
    """
    
    pass


#-- QUESTION 3 --#
def saisie_joueur():
    cd=[]
    prop=""
    print("Veuillez entrer votre combinaison")
    prop=input()
    for i in range (len(prop)):
        cd+=[codes_couleurs[prop[i].upper()]]
    return (cd)
        
    """
        Permet de recuperer la combinaison de pions proposee par un
        joueur

        :return: le code correspondant a la combinaison
        :rtype: list(int ...)
    """


#-- QUESTION 4 --#
def saisie_verif_joueur(nb_pions):
    cd=[]
    prop=""
    print("Veuillez entrer votre combinaison")
    prop=input()
    if len(prop) != nb_pions:
        return print("Le nombre de pion est incorrect!")
    for i in range (len(prop)):
        if prop[i].upper() in list(codes_couleurs.keys()) :
            pass
        else:
            return print("Cette couleur n'est pas disponible")
    for i in range (len(prop)):
        cd+=[codes_couleurs[prop[i].upper()]]
    return (cd)
    """
        Permet de recuperer la combinaison de pions proposee par un
        joueur. Verifie que la combinaison est composé de nb_pions
        et que les couleurs sont bien dans la liste de couleurs
        disponible.
        
        :param nb_pions: nombre de pions de la combinaison
        :type nb_pions: int
        :return: le code correspondant a la combinaison
        :rtype: list(int ...)
    """
#-- QUESTION 5 --#
def verification_position(solution, proposition):
    c=0
    for i in range (len(proposition)):
        if solution[i]==proposition[i]:
            c+=1
    return print(c)
        
    """
        Renvoie le nombre de pions de la proposition bien placés
        par rapport à la solution.
    
        :param solution: combinaison a deviner
        :type solution: list(int, ...)
        :param proposition: proposition a comparer a la solution
        :type proposition: list(int, ...)
        :return: nombre de pions de la proposition bien placés
        :rtype: int
    """
    
    pass

#-- QUESTION 6 --#
def verification_couleur(solution, proposition):
    c=0
    
    for i in range (len(proposition)):
        for j in range (len(solution)):
                if solution[j]==proposition[i]:
                    if i !=j:
                        c+=1
    return print(c)
            
    """
        Renvoie le nombre de pions de la proposition présents dans
        la solution, mais mals placés.
    
        :param solution: combinaison a deviner
        :type solution: list(int, ...)
        :param proposition: proposition a comparer a la solution
        :type proposition: list(int, ...)
        :return: nombre de pions de la proposition présents dans
        la solution, mais mals placés
        :rtype: int
    """
    
    pass


#-- QUESTION 7 --#
def verification(solution, proposition):
    a,b=0,0
    for i in range (len(proposition)):
        if solution[i]==proposition[i]:
            a+=1
    
    for i in range (len(proposition)):
        for j in range (len(solution)):
                if solution[j]==proposition[i]:
                    if i!=j:
                        b+=1
    return print("Num_pos=",a,"Num_couleur=",b)
    """
        Renvoie le nombre de pions de la proposition bien placés
        par rapport à la solution ainsi que le nombre de pions de
        a proposition présents dans la solution, mais mals placés.
    
        :param solution: combinaison a deviner
        :type solution: list(int, ...)
        :param proposition: proposition a comparer a la solution
        :type proposition: list(int, ...)
        :return: nombre de pions de la proposition bien placés
        et nombre de pions présents dans la solution, mais mals placés
        :rtype: tuple(int, int)
    """
    
    pass


#-- QUESTION 8 --#
def jouer(solution, nb_coup):
    for loop in range (nb_coup):
        x=saisie_verif_joueur(4)
        g=verification(solution,x)
        if a == 4 and b == 0:
            return print("Brava...")
        else:
            print(" Try Again")
        
            
        
        
    """    
        Fonction comprenant la boucle de jeu du mastermind.
    
        :param solution: combinaison a deviner
        :type solution: list(int, ...)
        :param nb_coup: nombre de coup pour deviner la combinaison
        :type nb_coup: int
        :return: resultat de la partie
        :rtype: bool
    """
    
    pass

def sol_aleatoire(taille_combinaison):
    f=[0]
    for i in range (taille_combinaison):
        if f[i]:
            f+=abs(6*RAND())
    return print(f)        
    
        
    """
        Fonction permettant de générer une combinaison
        aléatoire
    
        :param taille_combinaison: taille de la combinaison a générer
        :type taille_combinaison: int
        :return: combinaison
        :rtype: list(int, int, ... )
    """
    
    pass




# Tests
if __name__ == "__main__":
        
    #-- QUESTION 8 --#
    print('\nQuestion 8')
    solution = [2,0,3,1]
    nb_coup = 5
    resultat = jouer(solution, nb_coup)
    if resultat:
        print('Gagné !')
    else:
        print('Perdu !')
    #-- QUESTION 9 --#
    '''
    print('\nQuestion 9')
    taille_combinaison = 5
    solution = sol_aleatoire(taille_combinaison)
    nb_coup = 5
    resultat = jouer(solution, nb_coup)
    if resultat:
        print('Gagné !')
    else:
        couleurs_codes = {0: "R" , 1: "B" , 2: "J" , 3: "V" , 4: "N" , 5: "M" , 6: "F" , 7: "O" }
        print('Perdu ! La solution etait {}'.format([couleurs_codes[c] for c in solution]))
    '''
    
