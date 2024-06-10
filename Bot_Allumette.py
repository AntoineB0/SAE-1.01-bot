#           Bot pour le jeu des allumette
#--------------------------------------------------
# Bot Facile qui va donner un nombre alléatoire
# Bot Moyen qui utilise à 50% la facile et à 50% la difficile 
# Bot Difficile qui va renvoyer une valeur 1[4]
#--------------------------------------------------
from random import *

def Allumette_Facile()-> int:
    """Renvoie un nombre aléatoire entre 1 et 3

    Returns:
        int: une valeur entre 1 et 3
    """
    valeur:int
    valeur = randint(1,3)

    return valeur

def Allumette_Difficile(nbAllumette:int) -> int:
    """Renvoie une valeur qui va faire que le nombre d'allumettre sera 1[4]
    
    nbAllumette (int): Le nombre d'allumette dans le jeu 
    
    Returns:
        int: une valeur entre 1 et 3
    """
    valeur:int

    if nbAllumette-1 % 4 ==1:
        valeur = 1
    
    if nbAllumette-2 % 4 ==1:
        valeur = 2

    if nbAllumette-3 % 4 ==1:
        valeur = 3

    else:
        valeur = 3

    return valeur

def Allumette_Moyen(nbAllumette:int) -> int:
    """Renvoie à 50% une valeur du bot facile et à 50% une valeur du bot difficile 
    
    nbAllumette (int): Le nombre d'allumette dans le jeu 
    
    Returns:
        int: une valeur entre 1 et 3
    """
    aléatoire:int
    valeur:int

    aléatoire = randint(0,1)
    if aléatoire == 0:
        valeur = Allumette_Facile()
    else:
        valeur = Allumette_Difficile(nbAllumette)
    
    return valeur