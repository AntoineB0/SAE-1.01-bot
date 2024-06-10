from random import shuffle
from razerSynapse import razerSynapse
from colormode import colormode
import Bot_Allumette

"""
Allumettes :
    - 20 allumettes au départ
    - 2 joueurs
    - Chaque joueur peut prendre 1, 2 ou 3 allumettes
    - Le joueur qui prend la dernière allumette a perdu

préconditions : On prend en entrée un tableau de strings pour les joueurs et un tableau de int pour les points

postconditions : On affiche le gagnant et on retourne les points
"""

def Alumettes(joueur : list[str]) -> list[str] :

    alumettes : int
    choix : int
    tour : int
    difficulté : int

    shuffle(joueur)
    alumettes = 20
    choix = 0
    tour = 0

    print(razerSynapse(50))
    print("\n")
    print(colormode.ROUGE)
    print("   _____  .__                        __    __                 ")
    print("  /  _  \\ |  |  __ __  _____   _____/  |__/  |_  ____   ______")
    print(" /  /_\\  \\|  | |  |  \\/     \\_/ __ \\   __\\   __\\/ __ \\ /  ___/")
    print("/    |    \\  |_|  |  /  Y Y  \\  ___/|  |  |  | \\  ___/ \\___ \\ ")
    print("\\____|__  /____/____/|__|_|  /\\___  >__|  |__|  \\___  >____  >")
    print("        \\/                 \\/     \\/                \\/     \\/ ")
    print(colormode.RESET)
    print("\n")
    print(razerSynapse(50))
    print("\n" * 2)


    if joueur[0] == "robot1" or joueur[1] == "robot1" or joueur[0] == "robot2" or joueur[1] == "robot2":
        difficulté = int(input("Entrée le niveau de difficulté de l'ordinateur (1, 2 ou 3) : "))


        print(f"{joueur[0]} commence !")
        print("Voici les allumettes : \n")

        print("| " * alumettes)
        print("| " * alumettes)

        print("\n" * 2)
        print(razerSynapse(20))
        print("\n" * 2)

        while alumettes > 0:
            while choix < 1 or choix > 3:
                try:
                    if joueur[tour%2] == "robot1" or joueur[tour%2] == "robot2":
                        if difficulté == 1:
                            choix = Bot_Allumette.Allumette_Facile()
                        elif difficulté == 2:
                            choix = Bot_Allumette.Allumette_Moyen(alumettes)
                        elif difficulté == 3:
                            choix = Bot_Allumette.Allumette_Difficile(alumettes)
                        else :
                            choix = int(input(f"{joueur[tour%2]} Combien d'allumettes voulez-vous prendre ? (1, 2 ou 3) : "))
                            if choix < 1 or choix > 3:
                                print("\n Veuillez entrer un nombre entre 1 et 3 !")
                except ValueError:
                    print("Veuillez entrer un nombre entier !")

                alumettes = alumettes - choix
                choix = 0
                tour += 1

                if alumettes < 0:
                    alumettes = 0
                    
                print("")
                print("| " * alumettes)
                print("| " * alumettes)
                print("Il reste ", alumettes, " allumettes !")
                
                print("\n" * 2)
                print(razerSynapse(20))
                print("\n" * 2)

        print(f"{joueur[(tour-1)%2]} a perdu !")
        print("\n" * 2)
        return [joueur[(tour)%2], str(5)]


    else :    
        print(f"{joueur[0]} commence !")
        print("Voici les allumettes : \n")

        print("| " * alumettes)
        print("| " * alumettes)

        print("\n" * 2)
        print(razerSynapse(20))
        print("\n" * 2)

        while alumettes > 0:
            while choix < 1 or choix > 3:
                try:
                    choix = int(input(f"{joueur[tour%2]} Combien d'allumettes voulez-vous prendre ? (1, 2 ou 3) : "))
                    if choix < 1 or choix > 3:
                        print("\n Veuillez entrer un nombre entre 1 et 3 !")

                except ValueError:
                    print("Veuillez entrer un nombre entier !")

            alumettes = alumettes - choix
            choix = 0
            tour += 1

            if alumettes < 0:
                alumettes = 0
                
            print("")
            print("| " * alumettes)
            print("| " * alumettes)
            print("Il reste ", alumettes, " allumettes !")
            
            print("\n" * 2)
            print(razerSynapse(20))
            print("\n" * 2)

        print(f"{joueur[(tour-1)%2]} a perdu !")
        print("\n" * 2)
        return [joueur[(tour)%2], str(5)]
    
Alumettes(["titi","robot2"])