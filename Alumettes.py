from random import shuffle

"""
Allumettes :
    - 20 allumettes au départ
    - 2 joueurs
    - Chaque joueur peut prendre 1, 2 ou 3 allumettes
    - Le joueur qui prend la dernière allumette a perdu

préconditions : On prend en entrée un tableau de strings pour les joueurs et un tableau de int pour les points

postconditions : On affiche le gagnant et on retourne les points
"""
def Alumettes(joueur : list[str], points : list[int]):

    alumettes : int
    choix : int
    tour : int

    shuffle(joueur)
    alumettes = 20
    choix = 0
    tour = 0

    print(f"{joueur[0]} commence !")
    print("Voici les allumettes : \n")

    print("| " * alumettes)
    print("| " * alumettes)

    while alumettes > 0:
        while choix < 1 or choix > 3:
            try:
                choix = int(input(f"\n{joueur[tour%2]} Combien d'allumettes voulez-vous prendre ? (1, 2 ou 3) : "))
                if choix < 1 or choix > 3:
                    print("\n Veuillez entrer un nombre entre 1 et 3 !")

            except ValueError:
                print("Veuillez entrer un nombre entier !")

        alumettes = alumettes - choix
        choix = 0
        tour += 1

        print("")
        print("| " * alumettes)
        print("| " * alumettes)
        print("Il reste ", alumettes, " allumettes !")

    print(f"{joueur[(tour-1)%2]} a perdu !")