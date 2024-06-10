from razerSynapse import razerSynapse
from CCleaner import CCleaner

def Regles():
    """Affiche un menu et les règles du jeu sélectionné
    """
    choix = 0
    
    while choix != 5:
        print("Afficher les règles de quel jeu:")
        print("1 : Jeu des Allumettes")
        print("2 : Jeu du Morpion")
        print("3 : Jeu des Devinettes")
        print("4 : Jeu du Puissance 4")
        print("5 : Quitter")
        
        choix = int(input("Vous voulez afficher les règles de quel jeu (1-5): "))
    
        if choix == 1:
            # Allumettes
            razerSynapse(30)
            print("""
                  Deux joueurs s'affrontent en alternant, et à chaque tour, ils peuvent choisir de prendre 1, 2 ou 3 allumettes d'un seul tas. 
                  L'objectif reste de forcer l'adversaire à prendre la dernière allumette. 
                  La stratégie consiste à manipuler les tas de manière astucieuse pour garantir la victoire. 
                  Le joueur qui prend la dernière allumette est déclaré vainqueur. 
                  """)
            razerSynapse(30)
            input("Appuyer sur entrée pour quitter: ")
            CCleaner(0,0)
            
        elif choix == 2:
            # Morpion
            razerSynapse(30)
            print("""
                  Le Morpion est un jeu classique à deux joueurs se déroulant sur une grille de 3x3 cases. 
                  Chaque joueur utilise soit des "X" soit des "O" et tente d'aligner trois de ses symboles horizontalement, 
                  verticalement ou en diagonale. Les joueurs placent tour à tour leur symbole dans une case inoccupée, 
                  et le premier à aligner trois symboles remporte la partie. Si la grille est remplie sans alignement de trois symboles, 
                  la partie est déclarée nulle. C'est un jeu simple mais stratégique, favorisant la réflexion tactique. 
                  """)
            razerSynapse(30)
            input("Appuyer sur entrée pour quitter: ")
            CCleaner(0,0)
            
        elif choix == 3:
            # Devinette
            razerSynapse(30)
            print("""
                Dans le jeu de "Devinette", le joueur 1 énonce un intervalle numérique et choisit une valeur secrète à l'intérieur de cet intervalle. 
                Le joueur 2 doit deviner cette valeur en proposant des nombres. Le joueur 1 donne des indications telles que "plus grand" ou "plus petit" 
                après chaque tentative du joueur 2. 
                """)
            razerSynapse(30)
            input("Appuyer sur entrée pour quitter: ")
            CCleaner(0,0)
            
        elif choix == 4:
            # Puissance 4
            razerSynapse(30)
            print("""
                Le Puissance 4 est un jeu de société pour deux joueurs. Sur une grille verticale de 6 lignes et horizontale de 7 colonnes,
                les joueurs déposent tour à tour un pion de leur couleur dans une colonne de leur choix. L'objectif est de former 
                une rangée de quatre pions de sa propre couleur, que ce soit horizontalement, verticalement ou en diagonale.
                  """)
            razerSynapse(30)
            input("Appuyer sur entrée pour quitter: ")
            CCleaner(0,0)
            
        elif choix == 5:
            # Byebye
            razerSynapse(30)
            
        else:
            print("ERREUR d'interval")


