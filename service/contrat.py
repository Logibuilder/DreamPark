import pydoc
from datetime import datetime

class Contrat:
    """
    Classe représentant un contrat avec une date de début, une date de fin
    et un état indiquant s'il est encore en cours.
    """
    def __init__(self, date_debut, date_fin):
        """
        Initialiser un contrat avec une date de début, une date de fin,
        et définir son état comme "en cours" par défaut.

        :param date_debut: La date de début du contrat (type: date).
        :param date_fin: La date de fin du contrat (type: date).
        """
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.est_en_cours = True

    def rompre_contrat(self):
        """
        Permet de rompre le contrat si la date actuelle correspond à la date de fin.
        Met à jour l'état `est_en_cours` à False.
        """
        if self.date_fin == datetime.now().date():
            self.est_en_cours = False


pydoc.writedoc("contrat")