from colormode import colormode
from razerSynapse import razerSynapse
import time
from time import sleep
from random import shuffle

def Puissance4 (joueur : list[str]) -> list[str] :
    print(razerSynapse(50))
    print("\n")
    print (colormode.ROUGE)
    print ("__________      .__                                               _____  ")
    print ("\\______   \\__ __|__| ______ ___________    ____   ____  ____     /  |  | ")
    print (" |     ___/  |  \\  |/  ___//  ___/\\__  \\  /    \\_/ ___\\/ __ \\   /   |  |_")
    print (" |    |   |  |  /  |\\___ \\ \\___ \\  / __ \\|   |  \\  \\__\\  ___/  /    ^   /")
    print (" |____|   |____/|__/____  >____  >(____  /___|  /\\___  >___  > \\____   | ")
    print ("                        \\/     \\/      \\/     \\/     \\/    \\/       |__| ")
    print (colormode.RESET)
    print(razerSynapse(50))

    """
    Le tableau ressemblera à ça :
    .———————————————————————————.
    │ A0│ A1│ A2│ A3│ A4│ A5│ A6│
    │———————————————————————————│
    │ B0│ B1│ B2│ B3│ B4│ B5│ B6│
    │———————————————————————————│
    │ C0│ C1│ C2│ C3│ C4│ C5│ C6│
    │———————————————————————————│
    │ D0│ D1│ D2│ D3│ D4│ D5│ D6│
    │———————————————————————————│
    │ E0│ E1│ E2│ E3│ E4│ E5│ E6│
    │———————————————————————————│
    │ F0│ F1│ F2│ F3│ F4│ F5│ F6│
    .———————————————————————————.
    """

    grille : list[list[str]]
    tour : int
    choix : int
    gagnant : list[str]
    colonne : int
    compteur : int
    terminer : bool

    tour = 0
    terminer = False
    gagnant = ["",""]
    shuffle(joueur)
    grille = [[" "," "," "," "," "," "," "], 
              [" "," "," "," "," "," "," "], 
              [" "," "," "," "," "," "," "], 
              [" "," "," "," "," "," "," "], 
              [" "," "," "," "," "," "," "], 
              [" "," "," "," "," "," "," "]]

    while tour < 42 :
        if tour % 2 == 0 :
            print (f"\n{joueur[0]} à vous de jouer ! (vous êtes les Jaunes)")
            print("Voici la grille :")
            print("")
            print("  1   2   3   4   5   6   7  ")
            print (f"╭───┬───┬───┬───┬───┬───┬───╮")
            print (f"│ {grille[0][0]} │ {grille[0][1]} │ {grille[0][2]} │ {grille[0][3]} │ {grille[0][4]} │ {grille[0][5]} │ {grille[0][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[1][0]} │ {grille[1][1]} │ {grille[1][2]} │ {grille[1][3]} │ {grille[1][4]} │ {grille[1][5]} │ {grille[1][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[2][0]} │ {grille[2][1]} │ {grille[2][2]} │ {grille[2][3]} │ {grille[2][4]} │ {grille[2][5]} │ {grille[2][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[3][0]} │ {grille[3][1]} │ {grille[3][2]} │ {grille[3][3]} │ {grille[3][4]} │ {grille[3][5]} │ {grille[3][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[4][0]} │ {grille[4][1]} │ {grille[4][2]} │ {grille[4][3]} │ {grille[4][4]} │ {grille[4][5]} │ {grille[4][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[5][0]} │ {grille[5][1]} │ {grille[5][2]} │ {grille[5][3]} │ {grille[5][4]} │ {grille[5][5]} │ {grille[5][6]} │")
            print (f"╰───┴───┴───┴───┴───┴───┴───╯  ")
            choix = int(input("Quelle colonne voulez-vous jouer ? : "))

            while not (0 < choix < 8) :
                choix = int(input("Quelle colonne voulez-vous jouer ? : "))
                print("\n Veuillez entrer un nombre entre 1 et 7 !")
            

            colonne = choix - 1

            while grille[0][colonne] != " " :
                print("\n Veuillez entrer une colonne vide !")
                choix = int(input("Quelle colonne voulez-vous jouer ? : "))
                colonne = choix - 1

            compteur = 0
            while compteur < 5 and not terminer:
                compteur = compteur +1
                if grille[compteur][colonne] != " " :
                    grille[compteur-1][colonne] = colormode.JAUNE+"●"+colormode.RESET
                    terminer = True
                elif compteur == 5 :
                    grille[compteur][colonne] = colormode.JAUNE+"●"+colormode.RESET
                    terminer = True


        else :
            print (f"\n{joueur[1]} à vous de jouer ! (vous êtes les Rouges)")
            print("Voici la grille :")
            print("  1   2   3   4   5   6   7  ")
            print (f"╭───┬───┬───┬───┬───┬───┬───╮")
            print (f"│ {grille[0][0]} │ {grille[0][1]} │ {grille[0][2]} │ {grille[0][3]} │ {grille[0][4]} │ {grille[0][5]} │ {grille[0][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[1][0]} │ {grille[1][1]} │ {grille[1][2]} │ {grille[1][3]} │ {grille[1][4]} │ {grille[1][5]} │ {grille[1][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[2][0]} │ {grille[2][1]} │ {grille[2][2]} │ {grille[2][3]} │ {grille[2][4]} │ {grille[2][5]} │ {grille[2][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[3][0]} │ {grille[3][1]} │ {grille[3][2]} │ {grille[3][3]} │ {grille[3][4]} │ {grille[3][5]} │ {grille[3][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[4][0]} │ {grille[4][1]} │ {grille[4][2]} │ {grille[4][3]} │ {grille[4][4]} │ {grille[4][5]} │ {grille[4][6]} │")
            print (f"├───┼───┼───┼───┼───┼───┼───┤")
            print (f"│ {grille[5][0]} │ {grille[5][1]} │ {grille[5][2]} │ {grille[5][3]} │ {grille[5][4]} │ {grille[5][5]} │ {grille[5][6]} │")
            print (f"╰───┴───┴───┴───┴───┴───┴───╯  ")

            choix = -1
            choix = int(input("Quelle colonne voulez-vous jouer ? : "))

            while not (0 < choix < 8) :
                print("\n Veuillez entrer un nombre entre 1 et 7 !")
                choix = int(input("Quelle colonne voulez-vous jouer ? : "))
            

            colonne = choix - 1

            while grille[0][colonne] != " " :
                print("\n Veuillez entrer une colonne vide !")
                choix = int(input("Quelle colonne voulez-vous jouer ? : "))
                colonne = choix - 1

            compteur = 0
            while compteur < 5 and not terminer:
                compteur = compteur +1
                if grille[compteur][colonne] != " " :
                    grille[compteur-1][colonne] = colormode.ROUGE+"●"+colormode.RESET
                    terminer = True
                elif compteur == 5 :
                    grille[compteur][colonne] = colormode.ROUGE+"●"+colormode.RESET
                    terminer = True
                
        tour = tour + 1
        terminer = False

        #Code des conditions de victoire. 
        #Rappel : Pour gagner il faut que 4 pions de la même couleur soient alignés horizontalement, verticalement ou en diagonale.

        #Conditions de victoire horizontales
        for i in range(6) :
            for j in range (4) :
                if grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3] != " " :
                    if grille[i][j] == colormode.JAUNE+"●"+colormode.RESET :
                        print(razerSynapse(50))
                        print(f"{joueur[0]} à gagné !")
                        print(razerSynapse(50))
                        gagnant = [joueur[0], str(5)]
                    else :
                        print(razerSynapse(50))
                        print(f"{joueur[1]} à gagné !")
                        print(razerSynapse(50))
                        gagnant = [joueur[1], str(5)]
                    tour = 42

        #Conditions de victoire verticales
        for i in range(3) :
            for j in range (7) :
                if grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] != " " :
                    if grille[i][j] == colormode.JAUNE+"●"+colormode.RESET :
                        print(razerSynapse(50))
                        print(f"{joueur[0]} à gagné !")
                        print(razerSynapse(50))
                        gagnant = [joueur[0], str(5)]
                    else :
                        print(f"{joueur[1]} à gagné !")
                        gagnant = [joueur[1], str(5)]
                    tour = 42

        #conditions de victoire diagonales descendantes :
        for i in range(3) :
            for j in range (4) :
                if grille[0+i][0+j] == grille[i+1][1+j] == grille[i+2][2+j] == grille[i+3][3+j] != " " :
                    if grille[0+i][0+j] == colormode.JAUNE+"●"+colormode.RESET :
                        print(razerSynapse(50))
                        print(f"{joueur[0]} à gagné !")
                        print(razerSynapse(50))
                        gagnant = [joueur[0], str(5)]
                    else :
                        print(razerSynapse(50))
                        print(f"{joueur[1]} à gagné !")
                        print(razerSynapse(50))
                        gagnant = [joueur[1], str(5)]
                    tour = 42
        
        #Conditions de victoire diagonales montantes :
        for i in range(3) :
            for j in range(4) :
                if grille[5-i][0+j] == grille[4-i][1+j] == grille[3-i][2+j] == grille[2-i][3+j] != " " :
                    if grille[5-i][0+j] == colormode.JAUNE+"●"+colormode.RESET :
                        print(razerSynapse(50))
                        print(f"{joueur[0]} à gagné !")
                        print(razerSynapse(50))
                        gagnant = [joueur[0], str(5)]
                    else :
                        print(razerSynapse(50))
                        print(f"{joueur[1]} à gagné !")
                        print(razerSynapse(50))
                        gagnant = [joueur[1], str(5)]
                    tour = 42
    

    print("Voici la grille finale :")
    print("")
    print("  1   2   3   4   5   6   7  ")
    print (f"╭───┬───┬───┬───┬───┬───┬───╮")
    print (f"│ {grille[0][0]} │ {grille[0][1]} │ {grille[0][2]} │ {grille[0][3]} │ {grille[0][4]} │ {grille[0][5]} │ {grille[0][6]} │")
    print (f"├───┼───┼───┼───┼───┼───┼───┤")
    print (f"│ {grille[1][0]} │ {grille[1][1]} │ {grille[1][2]} │ {grille[1][3]} │ {grille[1][4]} │ {grille[1][5]} │ {grille[1][6]} │")
    print (f"├───┼───┼───┼───┼───┼───┼───┤")
    print (f"│ {grille[2][0]} │ {grille[2][1]} │ {grille[2][2]} │ {grille[2][3]} │ {grille[2][4]} │ {grille[2][5]} │ {grille[2][6]} │")
    print (f"├───┼───┼───┼───┼───┼───┼───┤")
    print (f"│ {grille[3][0]} │ {grille[3][1]} │ {grille[3][2]} │ {grille[3][3]} │ {grille[3][4]} │ {grille[3][5]} │ {grille[3][6]} │")
    print (f"├───┼───┼───┼───┼───┼───┼───┤")
    print (f"│ {grille[4][0]} │ {grille[4][1]} │ {grille[4][2]} │ {grille[4][3]} │ {grille[4][4]} │ {grille[4][5]} │ {grille[4][6]} │")
    print (f"├───┼───┼───┼───┼───┼───┼───┤")
    print (f"│ {grille[5][0]} │ {grille[5][1]} │ {grille[5][2]} │ {grille[5][3]} │ {grille[5][4]} │ {grille[5][5]} │ {grille[5][6]} │")
    print (f"╰───┴───┴───┴───┴───┴───┴───╯  ")
    return gagnant
