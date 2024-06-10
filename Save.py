import pickle 
import StructureDonnee
from typing import BinaryIO

def loaddata(NomFichier: str) -> StructureDonnee.Jeux :
    """Fonction qui ouvre le fichier binaire et qui renvoie une instance de jeux qui possède les données des parties precedente
    

    Args:
        Fichier (BinaryIO): Le fichier binaire

    Returns:
        StructureDonnee.Jeux: une instance de jeux qui possède les données des parties precedente
    """
    fichier: BinaryIO
    sauvegarde: StructureDonnee.Jeux
    fichier = open(NomFichier,"rb")
    fin : bool = False
    while not fin:
        try:
            sauvegarde = pickle.load(fichier)
        except EOFError :
            fin = True
    fichier.close()
    return sauvegarde


def savedata(NomFichier :str , donneeJeux:StructureDonnee.Jeux) -> None:
    """Fonction de sauvegarde

    Args:
        NomFichier (BinaryIO): Le fichier avec les données 
        donneeJeux (StructureDonnee.Jeux): Donnée des joueurs 
    """
    FichierBinaire : BinaryIO
    FichierBinaire = open(NomFichier,'wb')
    pickle.dump(donneeJeux,FichierBinaire)
    FichierBinaire.close()


def checkFileExistance(FilePath) -> bool:
    #fonction qui texte la presence du fichier 
    try : 
        with open(FilePath, 'r') as f:   
            return True
    except FileNotFoundError as e:
        return False
    
    
def DejaJouer(Tableau:list[StructureDonnee.Joueur] , Resultat:list[str] ) -> list[StructureDonnee.Joueur]:
    """Si le joueur à deja jouer on va juste modifier son score sinon on crée un nouveau profil

    Args:
        Tableau (list[StructureDonnee.Joueur]): Tableau qui contient des instance de joueur , c'est dedans que l'on va chercher le pseudo du joueur qui à gagner
        Resultat (list[str]): Un tableau qui contient le nom du joueur qui a gagné  dans la case [0] 
            Et le score dans la case [1] (en chaine de caractère)
            
    Returns: 
        list[StructureDonnee.Joueur]: Tableau après modification des scores 
    """
    compteur:int
    Nom:str
    Score:str
    position:int
    Joueur : StructureDonnee.Joueur
    
    position = -1
    Nom = Resultat[0]
    Score = Resultat[1]
    compteur = 0
    
    while compteur < len(Tableau) and position == -1:
        if Tableau[compteur].Nom == Nom :
            position = compteur
        compteur = compteur + 1
    
    if position == -1:
        Joueur = StructureDonnee.Joueur()
        Joueur.Nom = Nom
        Joueur.Score = Score
        Tableau.append(Joueur)
    else:
        Tableau[compteur-1].Score = str(int(Tableau[compteur-1].Score) + int(Score))
        
    return Tableau

    