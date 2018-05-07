# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:14:04 2018

@author: Rei
"""


#Importation
import scipy.special as sp
import numpy as np
import matplotlib.pyplot as plt
import math as m
import os
from itertools import chain

# Définition des classes
class deformation():
    def __init__(self,nomfic):
        self.donnees_travail=np.genfromtxt(nomfic,skip_header=3)#Fichier de données
        self.taille_donnees=len(self.donnees_travail)#Nombre de ligne du fichier de données
        self.cnm=self.donnees_travail[:,3]#Coefficient devant le cosinus
        self.snm=self.donnees_travail[:,4]#Coefficient devant le sinus
        self.ordre=self.donnees_travail[:,2]#Ordre 
        self.degre=self.donnees_travail[:,1]#Degré   

   
   
    def donnees(self,degre_max):
        """
        Renvoie des données jusqu'a un degré donné, permet de réduire le champs d'utilisation
    :degre_max: integer
    :degre type: integer
    :rtype: array
        """
        self.donnees_travail=self.donnees_travail[np.where(self.degre<=degre_max),:]

#Définition de fonction

def fichiers():
    """
    Fonction qui permet de récupérer les fichiers sous leurs noms normalisés nécéssaires au calcul des deformatiosn de la terre liées au réchauffement climatique)
    :dir: emplacement des fichiers par défaut répertoire ou se trouve le script python
    :type dir: string
    :rtype: list of string
    """
    c=[]
    for i in os.listdir():
        if 'GSM-2' in i:
            c+=[i]
    return c

def aplatissement_dynamique(ordre,degre,fichiers):
    """
    Calcul l'aplatissment dynamique d'un point donné
    :ordre: ordre du coefficient demandé
    :degre: degré du coefficient demandé
    :fichiers: ensemble des fichiers à traiter
    :ordre type: integer
    :degre type: integer
    :fichiers type: string list 
    :rtype: tableau
    """
    dates=[]
    annees_decimales=[]
    coefficient_cnm=[]
    C=[]
    a=''
    
    for i in range (len(fichiers)):
        dates+=[int(fichiers[i][6:10])]
        
        
    for i in range (len(fichiers)):
        a=deformation(fichiers[i],40)
        liste=np.where((a.ordre==ordre)&(a.degre==degre))
        C=a.cnm[liste]
        coefficient_cnm.append(C)
        annees_decimales.append(float(dates[i])+(float(fichiers[i][10:13])-1)/365)

    coefficient_cnm=np.array(coefficient_cnm)    
    coeff=np.polyfit(annees_decimales,coefficient_cnm,1) #Régression linéaire
    reglin=[annees_decimales[i]*coeff[0]+coeff[1] for i in range(len(fichiers))]
    reglin=np.array(reglin)
    plt.plot(dates,coefficient_cnm)
    plt.plot(dates,reglin)
    plt.show()    




#Definition de la fonction champ_moyen
def champ_moyen(degre,ordre,annee):
    '''
    Cette fonction calcule la constante et la dérive du champ moyen pour une année à
    partir des données fournies par le satellite GRACE
    :degre: degré
    :ordre: ordre
    :annee: année décimale
    :annee type: float
    :return: pente et dérive pour l'année renseignée
    :rtype: list
    '''
    dates=np.array([2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])
    coefficient_cnm=[]
    annees_decimales=[]
    a=''
    C=[]
    indice=0
    for i in range(14):
        a=annees[i]
        liste=np.where((a.degre==degre)&(a.ordre==ordre))
        C=a.cnm[liste]
        coefficient_cnm.append(C)
        annees_decimales.append(float(dates[i])+0.365-annee)    
    coefficient_cnm=np.array(coefficient_cnm)
    return np.polyfit(annees_decimales,coefficient_cnm,1)      
    
    
    
def pnmbarre(degre,ordre,x):
    pnm=sp.lpmv(ordre,degre,x)*(-1)**ordre#Fonction de Legendre ramené sous convention géodésique via le (-1)^ordre.
    return np.sqrt(2*(2*degre+1))*np.sqrt(sp.poch(1,degre-ordre)/sp.poch(1,degre+ordre))*pnm#Utilisation de pochhammer pour les factorielle pour limiter les erreurs






def variation_masse_apparente(love,table,p_ave,p_w,R,degre,champs_moyen):
    """
    :love: Table des nombres de love
    :table: table comprenant les valeurs des nombres de love en fonction du degré
    :p_ave: densité moyenne de la terre en kg/m^3
    :p_w: densité de l'eau en kg/m^3
    :R: rayon moyen de la Terre
    :degre: degre maximal auquel doit être effectué le calcul
    :champs_moyen: fichier comprenant les champs_moeyn sur une période donnée 
    :love type: array
    :table type: array list
    :p_ave type: float
    :p_w type: float
    :R type: float
    :degre type: integer
    :champs_moyen type: array
    """
    A=R*p_ave/(3*p_w)#Constante par laquelle sont multippliées les somme calculé ensuite
    total=[]#Liste qui abritera l'ensemble des résultats
    compteur=3#Les coefficients concernant les valeurs de degré strictement inférieur à deux ne sont pas traitée car elles entrainent une erreur de division par zero d'où le fait que l'on saute les nombre de love leur correspondant
    print(compteur)
    for angle in table:# dans la mesure ou dans cette boucle on en sortira les angle lamda et phi on nomme l'iterable "angle"
        somme1=0
        somme2=0
        compteur=3#Les coefficients sont nuls pour les deux premiers degrés entrainant une erreur division par zero ou des resulatts infinis
        for deg in range(2,degre-1):#Correspond au degré
            somme1+=(2*deg+1)/(1+love[deg,3])
            for ordre in range (deg+1):#Correspond a l'ordre, sinon il s'arreterais à deg-1
                somme2+=pnmbarre(deg,ordre,np.cos(np.pi/2-angle[0][1]*np.pi/180))*(champs_moyen[compteur,3]*np.cos(ordre*angle[0][0]*np.pi/180)+champs_moyen[compteur,5]*np.sin(ordre*angle[0][0]*np.pi/180))
                compteur+=1
        total+=[somme1*somme2*A]
    return total
                
def variation_deplacement_vertical(love,table,R,degre,champs_moyen,rebond_post_glaciaire=False):
    """
    Fonction calculant la variation en hauteur 
    :love: Table des nombres de love
    :table: table comprenant les valeurs des nombres de love en fonction du degré
    :R: rayon moyen de la Terre
    :degre: degre maximal auquel doit être effectué le calcul
    :champs_moyen: fichier comprenant les champs_moeyn sur une période donnée 
    :rebond_post_glaciare: défini si l'utilisateur veut prendre en compte le rebond glaciare, même si vrai le rebond glaciare n'est pris en compte que si il excéde 0.3 mm
    :love type: array
    :table type: array list
    :R type: float
    :degre type: integer
    :champ_moyen type: array
    :rebond_post_glaciaire: boolean
    
    """
    total=[]#Mêmes remarques ou presque que pour la variations de masse apparente 
    compteur=4
    somme1=[]
    somme2=[]
    for angle in table:
        somme1=0
        somme2=0
        compteur=3
        for deg in (2,degre):
            somme1+=love[deg,1]/(1+love[deg,3])
            for ordre in range (deg):
                somme2+=pnmbarre(deg,ordre,np.cos(np.pi/2-angle[0][1]*np.pi/180))*(champs_moyen[compteur,3]*np.cos(ordre*angle[0][0]*np.pi/180)+champs_moyen[compteur,5]*np.sin(ordre*angle[0][0]*np.pi/180))
        if rebond_post_glaciaire==True:
            if angle[3]>(0.3):
                total+=[R*somme1*somme2-angle[3]]
            else:
                total+=[R*somme1*somme2]
        else:
            total+=[R*somme1*somme2]
        
    return total
                
def carte_variation_masse_afrique(love,table,p_ave,p_w,R,degre,champs_moyen):
    """
    Affiche les variations de champs terrestre au niveau de l'afrique sous forme de graphique coloré représentant ladites variation en hauteur d'eau mm/a
    :love: Table des nombres de love
    :table: table comprenant les valeurs des nombres de love en fonction du degré
    :R: rayon moyen de la Terre
    :degre: degre maximal auquel doit être effectué le calcul
    :champs_moyen: fichier comprenant les champs_moeyn sur une période donnée 
    :p_ave: densité moyenne de la terre en kg/m^3
    :p_w: densité de l'eau en kg/m^3
    :love type: array
    :table type: array list
    :R type: float
    :degre type: integer
    :p_ave type: float
    :p_w type: float
    :rtype:None
    """
    lat=np.arange(-34.84,38.345,2)#crée un array avec un pas de deux degré qui couvre la lattitude de l'afrique
    long=np.arange(-17.52,51.28555,2)#crée un array avec un pas de deux qui couvre la longitude de l'afrique
    coast=np.genfromtxt('coast.txt')
    x,y=np.meshgrid(lat,long) #Crée une grille à partir latitudes et longitudes de l'afrique la symbolisant par la même occasion
    color=variation_masse_apparente(love,[[(x,y)]],p_ave,p_w,R,degre,champs_moyen)
    color = list(chain.from_iterable(color))
    plt.pcolormesh(y,x,color)
    plt.plot(coast[:,1],coast[:,0])
    plt.show()

  



#Test
a=deformation('GSM-2_2007001-2007031_0031_GRGS_0080_03v3.txt')
p_ave=5517
p_w=1000
R=6400
love=np.genfromtxt('Load_Love2_CM_boy.dat',skip_header=13)

champs_moyen=np.genfromtxt('champ_moyenhugo.txt',skip_header=1)
table=np.array([[(2.5,48.5),-0.247,-0.050,-0.129],[(-0.5,7.5),-0.951,-0.090,-0.144],[(-56.5,-3.5),-0.064,-0.042,0.049],[(-40.5,65.5),-5.691,-0.063,-1.346],[(42.5,-69.5),2.526,0.152,0.487]])
carte_variation_masse_afrique(love,table,p_ave,p_w,R,40,champs_moyen)
print(variation_masse_apparente(love,table,p_ave,p_w,R,40,champs_moyen))

