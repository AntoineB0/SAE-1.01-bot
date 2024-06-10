from random import randint
from colormode import colormode

def razerSynapse (taille : int) -> str :
    
    ligne : str
    _ : int

    ligne = ""

    for _ in range (0, taille):
        ligne = ligne + "—" + colormode.tab[randint(0, len(colormode.tab)-1)]
    
    return ligne + colormode.RESET