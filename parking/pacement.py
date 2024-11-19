class Placement:
    """"""

    def __init__(self, date_debut, date_fin):
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.est_en_cours = True


    def set_est_en_cours(self, bool):
        self.est_en_cours = bool


    def partir_place(self):
        pass
