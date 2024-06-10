from random import shuffle
from colormode import colormode
from razerSynapse import razerSynapse


def morpion(joueur: list[str]) -> list[str] :
    grille : list[list[str]]
    tour : int
    choix : int
    gagnant : list[str]


    shuffle(joueur)

    print(f"{joueur[0]} commence !")

    grille = [[colormode.GRIS + "1"+ colormode.RESET, colormode.GRIS +"2"+ colormode.RESET, colormode.GRIS +"3"+ colormode.RESET],
               [colormode.GRIS +"4"+ colormode.RESET, colormode.GRIS +"5"+ colormode.RESET, colormode.GRIS +"6"+ colormode.RESET],
               [colormode.GRIS +"7"+ colormode.RESET, colormode.GRIS +"8"+ colormode.RESET, colormode.GRIS +"9"+ colormode.RESET] ]
    tour = 0
    choix = 0
    gagnant = []

    print(razerSynapse(50))
    print(colormode.ROUGE)
    print("\n")
    print("   _____                      .__               ")
    print("  /     \\   _________________ |__| ____   ____  ")
    print(" /  \\ /  \\ /  _ \\_  __ \\____ \\|  |/  _ \\ /    \\ ")
    print("/    Y    (  <_> )  | \\/  |_> >  (  <_> )   |  \\")
    print("\\____|__  /\\____/|__|  |   __/|__|\\____/|___|  /")
    print("        \\/             |__|                  \\/ ")
    print("\n")
    print(colormode.RESET)
    print(razerSynapse(50))
    print("\n")





    while tour < 9:

        if tour % 2 == 0:
            print(f"\n{joueur[0]}", " à vous de jouer ! (vous êtes les O)")
            print("Voici la grille : \n")
            print("┌───┬───┬───┐")
            print(f"│ {grille[2][0]} │ {grille[2][1]} │ {grille[2][2]} │")
            print("├───┼───┼───┤")
            print(f"│ {grille[1][0]} │ {grille[1][1]} │ {grille[1][2]} │")
            print("├───┼───┼───┤")
            print(f"│ {grille[0][0]} │ {grille[0][1]} │ {grille[0][2]} │")
            print("└───┴───┴───┘")

            while not (0 < choix < 10) :
                try:
                    choix = int(input("Quelle case voulez-vous jouer ? : "))
                    if not (0 < choix < 10):
                        print("\n Veuillez entrer un nombre entre 1 et 9 !")
                    else : 
                        if grille[(choix-1)//3][(choix-1)%3] == colormode.BLEU+"X"+colormode.RESET or grille[(choix-1)//3][(choix-1)%3] == colormode.ROUGE+"O"+colormode.RESET:
                            print("\n Veuillez entrer une case vide !")
                            choix = 0
                        else :
                            grille[(choix-1)//3][(choix-1)%3] = (colormode.ROUGE+"O"+colormode.RESET)

                except ValueError:
                    print("Veuillez entrer un nombre entier !")
            
            choix = 0

        else:
            print(f"\n{joueur[1]}", " à vous de jouer ! (vous êtes les X)")
            print("Voici la grille : \n")
            print("┌───┬───┬───┐")
            print(f"│ {grille[2][0]} │ {grille[2][1]} │ {grille[2][2]} │")
            print("├───┼───┼───┤")
            print(f"│ {grille[1][0]} │ {grille[1][1]} │ {grille[1][2]} │")
            print("├───┼───┼───┤")
            print(f"│ {grille[0][0]} │ {grille[0][1]} │ {grille[0][2]} │")
            print("└───┴───┴───┘")

            while not (0 < choix < 10) :
                try:
                    choix = int(input("Quelle case voulez-vous jouer ? : "))
                    if not (0 < choix < 10):
                        print("\n Veuillez entrer un nombre entre 1 et 9 !")
                    else : 
                        if grille[(choix-1)//3][(choix-1)%3] == colormode.BLEU+"X"+colormode.RESET or grille[(choix-1)//3][(choix-1)%3] == colormode.ROUGE+"O"+colormode.RESET:
                            print("\n Veuillez entrer une case vide !")
                            choix = 0
                        else :
                            grille[(choix-1)//3][(choix-1)%3] = (colormode.BLEU + "X" + colormode.RESET)

                except ValueError:
                    print("Veuillez entrer un nombre entier !")

            choix = 0

        for j in range (3) :
            if ((grille[j][0] == grille[j][1] == grille[j][2] == (colormode.BLEU + "X" + colormode.RESET))
                or (grille[0][j] == grille[1][j] == grille[2][j] == (colormode.BLEU + "X" + colormode.RESET))):

                print(f"\n{joueur[1]} a gagné !")
                gagnant = [joueur[1], str(9-tour)]
                tour = 9

            elif ((grille[j][0] == grille[j][1] == grille[j][2] == (colormode.ROUGE+"O"+colormode.RESET))
                or (grille[0][j] == grille[1][j] == grille[2][j] == (colormode.ROUGE+"O"+colormode.RESET))) :

                print(f"\n{joueur[0]} a gagné !")
                gagnant = [joueur[0], str(9-tour)]
                tour = 9

        if ((grille[0][0] == grille[1][1] == grille[2][2] == (colormode.BLEU + "X" + colormode.RESET))
                or (grille[0][2] == grille[1][1] == grille[2][0] == (colormode.BLEU + "X" + colormode.RESET))):

                print(f"\n{joueur[1]} a gagné !")
                gagnant = [joueur[1], str(9-tour)]
                tour = 9

        elif ((grille[0][0] == grille[1][1] == grille[2][2] == (colormode.ROUGE+"O"+colormode.RESET))
                or (grille[0][2] == grille[1][1] == grille[2][0] == (colormode.ROUGE+"O"+colormode.RESET))) :

                print(f"\n{joueur[0]} a gagné !")
                gagnant = [joueur[0], str(9-tour)]
                tour = 9
        
        elif tour == 9 :
            gagnant = ["DRAW",str(-1)]
        
        
        tour = tour + 1
    
    print("Voici la grille finale : \n")
    print("┌───┬───┬───┐")
    print(f"│ {grille[2][0]} │ {grille[2][1]} │ {grille[2][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {grille[1][0]} │ {grille[1][1]} │ {grille[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {grille[0][0]} │ {grille[0][1]} │ {grille[0][2]} │")
    print("└───┴───┴───┘")

    return gagnant