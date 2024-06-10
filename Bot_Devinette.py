#           Bot pour le jeu devinette 
#--------------------------------------------------
# Bot Facile qui va donner un nombre alléatoire
# Bot Moyen qui utilise la methode de dychotomie mais le milieu va etre defini alleatoirement 
# Bot Difficile qui va utiliser la methode de dychotomie 
#--------------------------------------------------
from random import *


def Devinette_Facile(valeurMax:int) -> int:
    """Bot facile renvoie une valeur aléatoire

    Args:
        valeurMax (int): Taille l'interval

    Returns:
        int: une valeur aléatoire
    """
    valeur:int
    
    if valeurMax < 0:
        valeur = -1
    else:
        valeur = randint(0,valeurMax)
    return valeur


def Devinette_Moyen(ValeurMin:int , ValeurMax:int) -> int:
    """Bot Moyen qui utilise la methode de la dichotomie mais avec un milieux aléatoire 

    Args:
        ValeurMin (int): Valeur minimum pour la dichotomie
        ValeurMax (int): Valeur maximum pour la dichotomie

    Returns:
        int: une valeur aléatoire dans l'interval donné
    """
    valeur:int
    
    if ValeurMin > ValeurMax :
        valeur = -1
    elif ValeurMin < 0:
        valeur = -1
    else:
        valeur = randint(ValeurMin,ValeurMax)
    return valeur

def Devinette_Difficile(ValeurMin:int , ValeurMax:int, AncienneValeur:int, Position:int) -> int:
    """Bot Moyen qui utilise la methode de la dichotomie 

    Args:
        ValeurMin (int): Valeur minimum pour la dichotomie
        ValeurMax (int): Valeur maximum pour la dichotomie
        AncienneValeur (int): Ancienne Valeur retourner par le bot 

    Returns:
        int: le milieu de l'interval
    """
    NouvelleValeur:int
    #Position = 1 la valeur à trouver est plus haute , = 2 la valeur à trouver est plus basse
    if Position == 1:
        NouvelleValeur = AncienneValeur + (ValeurMax-AncienneValeur)
        return NouvelleValeur
    elif Position ==2:
        NouvelleValeur = ValeurMin + (AncienneValeur-ValeurMin)
    else:
        NouvelleValeur = -1
    
    return NouvelleValeur