from time import sleep
import os
from colormode import colormode

def CCleaner(TimeBeforeClear : int, type : int):
    """
    Procédure qui nettoie la console et affiche un message de redirection vers le menu
    Args:
        TimeBeforeClear (int): Temps avant le nettoyage de la console
        type (int): Type de redirection (1 : Menu principal, 2 : Jeu sélectionné, 3 : Scores, else : Backrooms)

    préconditions : TimeBeforeClear est un entier positif
    postconditions : La console est nettoyée et un message de redirection est affiché
    """
    texte : str

    if type == 1:
        texte = "au menu principal"
    elif type == 2: 
        texte = "vers le jeu sélectionné"
    elif type == 3:
        texte = "vers les scores"
    else : 
        texte = "vers le menu"
        
    print(colormode.ROUGE)
    print(f"Vous serez redirigés {texte} dans {TimeBeforeClear} secondes")
    print(colormode.RESET)
    if TimeBeforeClear != 0:
        sleep(TimeBeforeClear)
    os.system('cls' if os.name=='nt' else 'clear')

