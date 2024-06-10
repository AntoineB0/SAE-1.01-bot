#Le programme du jeu Devinette pour la SAE 1.01
from random import shuffle
from colormode import colormode


def Devinette(joueur : list[str]) -> list:

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
    
    
    print(colormode.RESET+"-"*10,joueur1,"-"*10)
    ValeurMax = int(input("Saisi la valeur de l'interval: "))

    
    
    while ValeurTrouver < 0 and ValeurTrouver > ValeurMax :
        print("-"*10,joueur1,"-"*10)
        print("Saisir la valeur a trouver: ", end='')
        ValeurTrouver = int(input(colormode.HIDE))

    print(colormode.RESET+"") 

    #Rajouter une condition pour que le joueur 1 puisse gagner
    while gagner == 0:
        print(str(NombreEssaie)+"-"*10 , joueur2 , "-"*10)
        ValeurJoueur2 = int(input("Deviner la valeur: "))
        position = -1 #la valeur à changer donc je retablie la position à -1
        NombreEssaie = NombreEssaie + 1

        while position < 0 or position > 2 :
            print("-"*10,joueur1,"-"*10)
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


    if NombreEssaie < int(ValeurMax *2 /3 ) :
        if gagner == 1 :
            print(colormode.VERT+"Bravo "+str(joueur1)+" vous avez gagné !!!")
            print(colormode.RESET+"-"*20)
            return([joueur2,str(ValeurMax-NombreEssaie)])
        elif gagner == -1 :
            print(colormode.ROUGE+"VAC:"+str(joueur1)+" triche")
            print(colormode.RESET+"-"*20)
            return([joueur2,str(ValeurMax)])
    else:
        if gagner == 1 :
            print(colormode.VERT+"Bravo "+str(joueur1)+" vous avez gagné !!!")
            print(colormode.RESET+"-"*20)
            return([joueur1,str(ValeurMax)])
        elif gagner == -1 :
            print(colormode.ROUGE+"VAC:"+str(joueur1)+" triche")
            print(colormode.RESET+"-"*20)
            return([joueur2,str(ValeurMax)])



        
    print(Devinette(["titi","toto"]))
        
    
        
    

    
    
    
    
    
    
    
    

    
    
    