import pydoc
class Placement:
    """
    Auteur de cette classe : ASSANE KANE

    Classe représentant un placement dans le parking.
    Un placement correspond à l'occupation d'une place de parking par un véhicule
    pendant une période définie.
    Attributs :
    ----------
    - date_debut : datetime.date
        La date à laquelle le placement a commencé.
    - date_fin : datetime.date
        La date prévue de fin du placement.
    - est_en_cours : bool
        Statut indiquant si le placement est toujours actif.
    """

    def __init__(self, date_debut, date_fin):
        """
        Initialise un placement avec une date de début et une date de fin.

        :param date_debut: La date de début du placement (type: datetime.date).
        :param date_fin: La date de fin prévue du placement (type: datetime.date).
        """
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.est_en_cours = True


    def set_est_en_cours(self, bool):
        """
        Définit le statut du placement (actif ou non).

        :param statut: Nouveau statut du placement (type: bool).
        """
        self.est_en_cours = bool


    def partir_place(self):
        """
        Méthode à implémenter pour gérer le départ du véhicule de la place de parking.
        Elle devra inclure les actions nécessaires pour libérer la place et mettre à jour
        le statut du placement.
        """
        pass


pydoc.writedoc("placement")