import pydoc
class Place:
    """
    Auteur de cette classe : ASSANE KANE

    Classe représentant une place de parking.

    Attributs :
    ----------
    - numero : int
        Numéro unique de la place dans son niveau.
    - niveau : str
        Identifiant du niveau auquel appartient la place (ex. : "A", "B").
    - longueur : float
        Longueur de la place (en mètres).
    - hauteur : float
        Hauteur de la place (en mètres).
    - est_libre : bool
        Indique si la place est libre ou non.
    - id : str
        Identifiant unique de la place (composé du niveau et du numéro).
    """
    def __init__(self, numero, niveau, longeur, hauteur):
        """
        Initialise une place de parking.

        :param numero: Numéro unique de la place.
        :param niveau: Identifiant du niveau de la place.
        :param longueur: Longueur de la place.
        :param hauteur: Hauteur de la place.
        """
        self.numero = numero
        self.niveau = niveau
        self.longeur = longeur
        self.hauteur = hauteur
        self.est_libre = True
        self.id = niveau+str(self.numero)


    def set_valeur_libre(self, bool):
        """
        Modifie l'état d'occupation de la place.

        :param est_libre: Booléen indiquant si la place est libre (True) ou occupée (False).
        """
        est_libre = bool


    def __add_placement__(self, placement):
        """
        Associe un placement (occupation) à cette place.

        :param placement: L'objet représentant le placement à associer.
        """
        pass


pydoc.writedoc("place")

