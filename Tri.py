import StructureDonnee

def Tri (tableau:list[StructureDonnee.Joueur]) -> list[StructureDonnee.Joueur] :
    """Fonction de tri (tri à bulles) pour trier un tableau de joueurs par score de façon décroissante.

    Args:
        tableau (list[StructureDonnee.Joueur]): Le tableau de joueurs à trier.

    Returns:
        list[StructureDonnee.Joueur]: Le tableau trié par score.
    """
    n:int
    compteur1 : int
    compteur2 : int
    temporaire : StructureDonnee.Joueur
    
    
    n = len(tableau)

    for compteur1 in range(n - 1):
        for compteur2 in range(0, n-compteur1-1):
            if int(tableau[compteur2].Score) < int(tableau[compteur2+1].Score):
                temporaire = tableau[compteur2]
                tableau[compteur2] = tableau[compteur2+1]
                tableau[compteur2 + 1] =  temporaire

    return tableau