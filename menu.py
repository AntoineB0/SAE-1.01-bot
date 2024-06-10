from razerSynapse import razerSynapse
from colormode import colormode

def menu() -> int:

    choix : int


    print(razerSynapse(50))
    print("\n")
    print(colormode.ROUGE)
    print("   _____                        __________        .__              .__             .__   ")
    print("  /     \\   ____   ____  __ __  \\______   \\_______|__| ____   ____ |__|__________  |  |  ")
    print(" /  \\ /  \\_/ __ \\ /    \\|  |  \\  |     ___/\\_  __ \\  |/    \\_/ ___\\|  \\____ \\__  \\ |  |  ")
    print("/    Y    \\  ___/|   |  \\  |  /  |    |     |  | \\/  |   |  \\  \\___|  |  |_> > __ \\|  |__")
    print("\\____|__  /\\___  >___|  /____/   |____|     |__|  |__|___|  /\\___  >__|   __(____  /____/")
    print("        \\/     \\/     \\/                                  \\/     \\/   |__|       \\/      ")
    print("\n")
    print(colormode.RESET)
    print(razerSynapse(50))
    print("\n" * 2)
    print("Choisissez une action à effectuer :", "\n")
    print("1 : Jeu des Allumettes")
    print("2 : Jeu du Morpion")
    print("3 : Jeu des Devinettes")
    print("4 : Jeu du puissance 4")
    print("5 : Afficher les scores")
    print("6 : Afficher le menu des regles")
    print("7 : Quitter le programme \n")

    choix = int(input("Quel est votre choix : "))

    print("\n" * 2)

    return choix