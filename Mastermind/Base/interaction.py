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


# Tests
if __name__ == "__main__":
        
    #-- QUESTION 1 --#
    print('\nQuestion 1')
    print('Expected:\nBJVN\t0 bons pions\t0 bonnes couleurs\nGet:')
    affiche_indications(0, 0, [1, 2, 3, 4])
    print('Expected:\nRJNF\t3 bons pions\t1 bonnes couleurs\nGet:')
    affiche_indications(3, 1, [0, 2, 4, 6])
    print('Expected:\nORGJ\t4 bons pions\t2 bonnes couleurs\nGet:')
    affiche_indications(4, 2, [7, 0, 1, 2])

    #-- QUESTION 2 --#
    print('\nQuestion 2')
    print('Expected:\n      BJV       \nGet:')
    affiche_jolies_indications(0, 0, [1, 2, 3])
    print('Expected:\n    * BJV * *  \nGet:')
    affiche_jolies_indications(2, 1, [1, 2, 3])
    print('Expected:\n      * RJNF * *    \nGet:')
    affiche_jolies_indications(3, 1, [0, 2, 4, 6])
    print('Expected:\n    * * ORGJ * * * *\nGet:')
    affiche_jolies_indications(4, 2, [7, 0, 1, 2])

    #-- QUESTION 3 --#
    print('\nQuestion 3')
    print('Expected:\nEntrez votre combinaison : RJNF\nCode de la combinaison :\n[0, 2, 4, 6]\nGet:')
    comb = saisie_joueur()
    print('Code de de la combinaison :')
    print(comb)

    #-- QUESTION 4 --#
    print('\nQuestion 4')
    print('Expected:\nEntrez votre combinaison a 4 pions : rjnf\nCode de la combinaison :\n[0, 2, 4, 6]\nGet:')
    comb = saisie_verif_joueur(4)
    print('Code de de la combinaison :')
    print(comb)
    print('Expected:\nEntrez votre combinaison a 5 pions : RJNFQ\nCouleur inconnue\nGet:')
    comb = saisie_verif_joueur(5)
    print('Expected:\nEntrez votre combinaison 4 pions : RJN\nNombre de pions incorrect\nGet:')
    comb = saisie_verif_joueur(4)
    

