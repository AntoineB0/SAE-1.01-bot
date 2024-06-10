from Alumettes import Alumettes

if __name__ == "__main__":
    
    choix: int
    Joueur : list[str]
    Temp : str

    Joueur = []
    choix = 0

    print("\n","-"*30, "\n")
    print("Bienvenue dans ce programme de Mini-Jeux ! \n")
    Temp = input("Veuillez entrer le nom du joueur 1 : ")
    Joueur.append(Temp)
    Temp = input("\nVeuillez entrer le nom du joueur 2 : ")
    Joueur.append(Temp)



    while choix != 6:

        print("\n","-"*30, "\n")
        print("Veuillez choisir quelque chose à faire :", "\n")
        print("1 : Jeu des Allumettes")
        print("2 : Jeu du Morpion")
        print("3 : Jeu des devinettes")
        print("4 : Jeu du puissance 4")
        print("5 : Afficher les scores")
        print("6 : quitter le programme \n")


        choix = int(input("Quel est votre choix : "))

        while choix < 1 or choix > 6:
            print("erreur de saisie")
            choix = int(input("quel est votre choix d'opération : "))

        if choix == 1:
            print(Alumettes(Joueur, [0, 0]))
            choix = 0

        if choix == 2:
            choix = 0

        if choix == 3:
            choix = 0

        if choix == 4:
            choix = 0

        if choix == 5:
            choix = 0