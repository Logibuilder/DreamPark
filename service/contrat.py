class Contrat:
    def __init__(self, date_debut, date_fin):
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.est_en_cours = True

    def rompre_contrat(self):
        pass