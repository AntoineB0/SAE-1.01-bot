#Le programme du jeu Devinette pour la SAE 1.01
from random import shuffle
from colormode import colormode
from razerSynapse import razerSynapse


def Devinette(joueur : list[str]) -> list[str]:

    """Le joueur 1 choisi la taille de l'ensemble , il choisi un nombre entre 1 et n , puis le joueur2 doit deviner le nombre saisi par le joueur1 , pour chaque tout le joueur1 doit dire si le nombre est plus grand ou plus petit ou gagné (besoin d'anti cheat)

    Args:
        joueur (list): Une liste contenant le nom des deux joueurs

    Returns:
        str: Le programme renvoie le nom du joueur qui a gagné  dans la case [0] 
            Et le score dans la case [1] (en chaine de caractère)
    """
    #Mode de fonctionnement du programme:
    #
    #Le joueur 2 a perdu quand il a un nombre d'essai superieur à 2/3 des valeurs de l'interval
    #
        
    #Declaration de variable
    joueur1 : str
    joueur2:str
    ValeurMax : int
    ValeurTrouver : int #Valeur à trouver
    ValeurJoueur2 : int #Valeur saisie par le joueur 2
    NombreEssaie : int #Le nombre d'essai va determiner le score 
    gagner : int # 1 = gagner , 0 = continue , -1 = triche
    position : int 
    
    #Variable pour le bot
    NiveauBot : int
    ValeurBot : int
    
    #Programme
    shuffle(joueur)
    joueur1 = joueur[0]
    joueur2 = joueur[1]
    ValeurJoueur2 = -1
    ValeurTrouver = -1
    ValeurMax= -1
    NombreEssaie = 0
    gagner = 0
    position = -1
    

    print(razerSynapse(50))
    print("\n")
    print(colormode.ROUGE)
    print("________              .__               __    __          ")
    print("\\______ \\   _______  _|__| ____   _____/  |__/  |_  ____  ")
    print(" |    |  \\_/ __ \\  \\/ /  |/    \\_/ __ \\   __\\   __\\/ __ \\ ")
    print(" |    `   \\  ___/\\   /|  |   |  \\  ___/|  |  |  | \\  ___/ ")
    print("/_______  /\\___  >\\_/ |__|___|  /\\___  >__|  |__|  \\___  >")
    print("        \\/     \\/             \\/     \\/                \\/ ")
    print(colormode.RESET)
    print("\n")
    print(razerSynapse(50))
    print("\n" * 2)

    print(colormode.ROUGE+"""
ATTENTION : 
          
        Dans ce jeu, la triche est interdite, si vous trichez, vous perdez automatiquement
        et votre adversaire remportera le maximum de points possibles.

        VERIFIEZ BIEN VOS REPONSES AVANT DE LES VALIDER AFIN D EVITER TOUTE MAUVAISE SURPRISE.
"""+colormode.RESET)

    if joueur2 != "Robot" or joueur1 != "Robot":
        print(razerSynapse(10) + joueur1 + razerSynapse(10)+ "\n")
        ValeurMax = int(input("Saisir la valeur de l'intervalle: "))

        
        while ValeurMax < 0 :
            print(razerSynapse(10) + joueur1 + razerSynapse(10)+ "\n")
            ValeurMax = int(input("Saisir la valeur de l'intervalle: "))

        while ValeurTrouver < 0 or ValeurTrouver > ValeurMax :
            print("\n")
            print(razerSynapse(10) + joueur1 + razerSynapse(10))
            print("\n")
            print("Saisir la valeur à trouver: ", end='')
            ValeurTrouver = int(input(colormode.HIDE))
            print(colormode.RESET+"")

        while (gagner == 0) and (NombreEssaie < int(ValeurMax *2/3 )):
            print("\n")
            print("tour : " + str(NombreEssaie)+ razerSynapse(10) + joueur2 + razerSynapse(10))
            print("\n")
            ValeurJoueur2 = int(input("Deviner la valeur: "))
            while ValeurJoueur2 > ValeurMax or ValeurMax < 0:
                print("La valeur saisie n'est pas comprise dans l'intervalle "+"[0,"+str(ValeurMax)+"]")
                ValeurJoueur2 = int(input("Deviner la valeur: "))
            position = -1 #la valeur à changer donc je retablie la position à -1
            NombreEssaie = NombreEssaie + 1

            while position < 0 or position > 2 :
                print("\n")
                print(razerSynapse(10) + joueur1 + razerSynapse(10))
                print("\n")
                position = int(input("La valeur à trouver est juste(0) , plus haute(1) ou plus basse(2): "))

            if ((position != 0) and (ValeurJoueur2 == ValeurTrouver) ): # Valeur exact
                gagner = - 1
            elif ((position != 1) and (ValeurJoueur2 < ValeurTrouver)) : #la valeur du j2 est plus petite 
                gagner = - 1
            elif ((position != 2) and (ValeurJoueur2 > ValeurTrouver)): #La valeur du j2 est plus grande 
                gagner = - 1
            elif position == 0 and ValeurJoueur2 == ValeurTrouver :
                gagner = 1 
            else:
                gagner = 0


        if NombreEssaie < int(ValeurMax *2/3 ) :
            if gagner == 1 :
                print(colormode.VERT+"Bravo "+str(joueur2)+" vous avez gagné !!!")
                return([joueur2,str(ValeurMax-NombreEssaie)])
            elif gagner == -1 :
                print(colormode.ROUGE+"VAC:"+str(joueur1)+" triche")
                return([joueur2,str(ValeurMax)])
        else:
            if gagner == 1 or gagner == 0:
                print(colormode.VERT+"Bravo "+str(joueur1)+" vous avez gagné !!!")
                return([joueur1,str(ValeurMax)])
            elif gagner == -1 :
                print(colormode.ROUGE+"VAC:"+str(joueur1)+" triche")
                return([joueur2,str(ValeurMax)])
    else:
        #Selection du niveau du Bot
        print("Vous voulez jouer contre un bot de quel niveau:")
        print(colormode.VERT+"1-Facile"+colormode.RESET)
        print(colormode.JAUNE+"2-Normal"+colormode.RESET)
        print(colormode.ROUGE+"3-Difficile"+colormode.RESET)
        
        NiveauBot = input("Quel niveau voulez vous ? :")
        while NiveauBot < 0 and NiveauBot > 4:
            NiveauBot = input("Quel niveau voulez vous ?(Une valeur dans l'interval[1-3]):")
        
        
        if joueur1 == "Robot":
            print("Work in progress  ")
            
        elif joueur2 == "Robot":
            print(razerSynapse(10) + joueur1 + razerSynapse(10)+ "\n")
            ValeurMax = int(input("Saisir la valeur de l'intervalle: "))

            
            while ValeurMax < 0 :
                print(razerSynapse(10) + joueur1 + razerSynapse(10)+ "\n")
                ValeurMax = int(input("Saisir la valeur de l'intervalle: "))

            while ValeurTrouver < 0 or ValeurTrouver > ValeurMax :
                print("\n")
                print(razerSynapse(10) + joueur1 + razerSynapse(10))
                print("\n")
                print("Saisir la valeur à trouver: ", end='')
                ValeurTrouver = int(input(colormode.HIDE))
                print(colormode.RESET+"")
        
    
    return(["Erreur"]) #Si le programme arrive ici c'est qu'il y a une erreur