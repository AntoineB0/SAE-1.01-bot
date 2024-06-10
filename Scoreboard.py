from razerSynapse import razerSynapse
from colormode import colormode
from Tri import Tri
import StructureDonnee 

def scoreboard(Score : StructureDonnee.Jeux):
    """
    Quand on veut afficher le scoreboard d'un jeu:
        -Selectionner le jeu
          -> Le programme tri les scores
        -Le programme affiche les scores
    """
    choix : int
    
    choix = 0
    
    print(razerSynapse(50))
    print("\n")
    print (colormode.VIOLET)
    print ("  _________                                  ")
    print (" /   _____/ ____  ___________   ____   ______")
    print (" \\_____  \\_/ ___\\/  _ \\_  __ \\_/ __ \\ /  ___/")
    print (" /        \\  \\__(  <_> )  | \\/\\  ___/ \\___ \\ ")
    print ("/_______  /\\___  >____/|__|    \\___  >____  >")
    print ("        \\/     \\/                  \\/     \\/ ")
    print("\n")
    print (colormode.RESET)
    print(razerSynapse(50))
    
    
    while choix != 5:
        print("1 : Jeu des Allumettes")
        print("2 : Jeu du Morpion")
        print("3 : Jeu des Devinettes")
        print("4 : Jeu du puissance 4")
        print("5 : Revenir au menu principal \n")
        
        choix= int(input("Vous voulez afficher le score de quels jeux ?"))
        
        if choix == 1:
            #Allumettes
            razerSynapse(50)
            Score.Alumettes = Tri(Score.Alumettes)
            #Afficher les scores
            affichage(Score.Alumettes)
            
        
        elif choix == 2:
            #Morpion
            razerSynapse(50)
            Score.Morpion = Tri(Score.Morpion)
            #Afficher les scores
            affichage(Score.Morpion)
            
            
        elif choix == 3:
            #Devinettes
            razerSynapse(50)
            Score.Devinette = Tri(Score.Devinette)
            #Afficher les scores
            affichage(Score.Devinette)
            
            
        elif choix == 4:
            #Puissance4
            razerSynapse(50)
            Score.Puissance4 = Tri(Score.Puissance4)
            #Afficher les scores
            affichage(Score.Puissance4)
            
            
    
    
def affichage(tableau:list[StructureDonnee.Joueur]) -> None:
    """affiche les scores de tout les joueurs 

    Args:
        tableau (list[StructureDonnee.Joueur]): tableau contenant tout les scores en fonction des jeux 
    """
    #Affichage Graphique
    print(razerSynapse(50))
    print("\n")
    print (colormode.JAUNE)
    print("""
.__    .__       .__                                       
|  |__ |__| ____ |  |__   ______ ____  ___________   ____  
|  |  \|  |/ ___\|  |  \ /  ___// ___\/  _ \_  __ \_/ __ \ 
|   Y  \  / /_/  >   Y  \\\\___ \\\\  \__(  <_> )  | \/\  ___/ 
|___|  /__\___  /|___|  /____  >\___  >____/|__|    \___  >
     \/  /_____/      \/     \/     \/                  \/ 
          """)
    print("\n")
    print (colormode.RESET)
    print(razerSynapse(50))
    
    #Affichage des scores
    for i in range(len(tableau)):
        print(f"| {str(i+1)}e position : {str(tableau[i].Nom)} avec {str(tableau[i].Score)} points ")
        
    print("\n")
    print(razerSynapse(50))
    
    