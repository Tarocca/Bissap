# -*- coding: utf-8 -*-
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

# Tests
if __name__ == "__main__":
        
    #-- QUESTION 5 --#
    print('\nQuestion 5')
    print('Expected:\n1\nGet:')
    num_pos = verification_position([1, 5, 7, 0], [1, 2, 3, 4])
    print(num_pos)
    print('Expected:\n4\nGet:')
    num_pos = verification_position([1, 5, 7, 0, 2], [1, 5, 7, 0, 4])
    print(num_pos)
    print('Expected:\n2\nGet:')
    num_pos = verification_position([1, 0, 2, 4], [0, 1, 2, 4])
    print(num_pos)

    #-- QUESTION 6 --#
    print('\nQuestion 6')
    print('Expected:\n2\nGet:')
    num_couleur = verification_couleur([1, 5, 7, 0], [1, 2, 5, 4])
    print(num_couleur)
    print('Expected:\n4\nGet:')
    num_couleur = verification_couleur([1, 5, 7, 0, 2], [1, 5, 7, 0, 4])
    print(num_couleur)
    print('Expected:\n4\nGet:')
    num_couleur = verification_couleur([1, 0, 2, 4], [0, 1, 2, 4])
    print(num_couleur)

    #-- QUESTION 7 --#
    print('\nQuestion 7')
    print('Expected:\nNum_pos = 0, Num_couleur = 0\nGet:')
    num_pos, num_couleur = verification([1, 5, 3], [2, 6, 4])
    print('Num_pos = {}, Num_couleur = {}'.format(num_pos, num_couleur))
    print('Expected:\nNum_pos = 1, Num_couleur = 3\nGet:')
    num_pos, num_couleur = verification([1, 2, 0, 3], [1, 0, 3, 2])
    print('Num_pos = {}, Num_couleur = {}'.format(num_pos, num_couleur))
    print('Expected:\nNum_pos = 4, Num_couleur = 0\nGet:')
    num_pos, num_couleur = verification([1, 2, 0, 3], [1, 2, 0, 3])
    print('Num_pos = {}, Num_couleur = {}'.format(num_pos, num_couleur))
