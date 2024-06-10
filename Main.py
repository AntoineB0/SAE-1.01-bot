from Alumettes import Alumettes
from Devinette import Devinette
from Morpion import morpion
from Puissance4 import Puissance4
from colormode import colormode
from menu import menu
from razerSynapse import razerSynapse
from CCleaner import CCleaner
from Scoreboard import scoreboard
from Regle import Regles
import StructureDonnee
import Save

if __name__ == "__main__":
    
    choix: int
    Joueur : list[str]
    Temp : str
    résultat : list[str]
    
    NomFichier: str
    Sauvegarde: StructureDonnee.Jeux
    
    

    NomFichier = "SaveFile"
    if Save.checkFileExistance(NomFichier):
        Sauvegarde = Save.loaddata(NomFichier)
    else:
        Sauvegarde = StructureDonnee.Jeux()
        Sauvegarde.Alumettes = []
        Sauvegarde.Devinette = []
        Sauvegarde.Morpion = []
        Sauvegarde.Puissance4 = []
    
    Joueur = []
    choix = 0

    print(razerSynapse(50))
    print("\n")
    print(colormode.ROUGE)
    print("   _____  .__       .__       __                     ")
    print("  /     \\ |__| ____ |__|     |__| ____  __ _____  ___")
    print(" /  \\ /  \\|  |/    \\|  |     |  |/ __ \\|  |  \\  \\/  /")
    print("/    Y    \\  |   |  \\  |     |  \\  ___/|  |  />    < ")
    print("\\____|__  /__|___|  /__| /\\__|  |\\___  >____//__/\\_ \\")
    print("        \\/        \\/     \\______|    \\/            \\/")
    print(colormode.RESET)
    print("\n")
    print(razerSynapse(50))

    print("Bienvenue dans ce programme de Mini-Jeux ! \n")
    print("Vous allez choisir vos noms de joueurs. Ces noms devront faire obligatoirement 4 caractères et être différents. \n")
    Temp = input("Veuillez entrer le nom du joueur 1 : ")
    while len(Temp) != 4 or Temp == "    " and (Temp != "robot1" or Temp != "robot2"):
        print("Le nom doit faire 4 caractères et être non vide")
        Temp = input("Veuillez entrer le nom du joueur 1 : ")

    Joueur.append(Temp)

    Temp = input("\nVeuillez entrer le nom du joueur 2 : ")

    while Temp == Joueur[0] or len(Temp) != 4 or Temp == "    " and (Temp != "robot1" or Temp != "robot2"):
        print("Le nom doit faire 4 caractères et être différent de celui du joueur 1")
        Temp = input("Nom invalide, veuillez en choisir un autre :")

    Joueur.append(Temp)

    
    while choix != 7:


        if choix == 0 :
            choix = menu()

        elif choix == 1:
            CCleaner(0, 2)
            résultat = Alumettes(Joueur)
            Save.DejaJouer(Sauvegarde.Alumettes,résultat)
            print("\n")
            print(razerSynapse(30))
            print("\n")
            CCleaner(2, 1)
            choix = 0

        elif choix == 2:
            CCleaner(0, 2)
            résultat = morpion(Joueur)
            if résultat != [] :
                Save.DejaJouer(Sauvegarde.Morpion,résultat)
            print("\n")
            print(razerSynapse(30))
            print("\n")
            CCleaner(2, 1)
            choix = 0
            
        elif choix == 3:
            CCleaner(0, 2)
            résultat = Devinette(Joueur)
            Save.DejaJouer(Sauvegarde.Devinette,résultat)
            print("\n")
            print(razerSynapse(30))
            print("\n")
            CCleaner(2, 1)
            choix = 0


        elif choix == 4:
            CCleaner(0, 2)
            résultat = Puissance4(Joueur)
            if résultat != ["",""] :
                Save.DejaJouer(Sauvegarde.Puissance4,résultat)
            CCleaner(2, 1)
            choix = 0

        elif choix == 5:
            CCleaner(0, 3)
            scoreboard(Sauvegarde)
            CCleaner(2, 1)
            choix = 0

        elif choix == 6:
            CCleaner(0, 2)
            Regles()
            CCleaner(0, 2)
            choix = 0
        else : 
            print("Erreur de saisie")
            choix = 0
    
    #Sauvegarde des données
    Save.savedata(NomFichier,Sauvegarde)
    #Affichage
    
    print(colormode.VERT)
    print("""
  ───────────────
( A la revoyure ! )
  ───────────────
         \\   ^__^ 
          \\  (oo)\\_______
             (__)\\       )\\/\\
                 │├────w │
                 ││     ││
          """)
    print("\n")
    print(razerSynapse(30))
    print(colormode.RESET)