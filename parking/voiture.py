import pydoc

class Voiture:

    """
    Auteur de cette classe : ASSANE KANE

    Classe représentant une voiture dans le système de gestion de parking.
    Chaque voiture possède des caractéristiques physiques et une immatriculation unique.

    Attributs :
    ----------
    - hauteur : float
        La hauteur de la voiture (en mètres).
    - longueur : float
        La longueur de la voiture (en mètres).
    - immatriculation : str
        L'immatriculation unique de la voiture.
    - est_dans_parking : bool
        Indique si la voiture est actuellement garée dans le parking.
    """
    def __init__(self, hauteur, longueur, immatri):
        """
        Initialise une voiture avec ses dimensions et son immatriculation.

        :param hauteur: Hauteur de la voiture (type: float).
        :param longueur: Longueur de la voiture (type: float).
        :param immatri: Immatriculation unique de la voiture (type: str).
        """
        self.hauteur = hauteur
        self.longueur = longueur
        self.immatriculation = immatri
        self.est_dans_parking = False

    def add_placement(self, placement):
        """
        Associe un placement à cette voiture.
        Cette méthode sera utilisée pour gérer le stationnement de la voiture
        dans une place de parking.

        :param placement: L'objet Placement correspondant à la place attribuée (type: Placement).
        """
        self.est_dans_parking = True
        # Logique de gestion du placement à définir ici
        return True

#pydoc.writedoc("voiture")