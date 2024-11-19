import parking.voiture


class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.est_abonne = False
        self.est_super_abonne = False
        self.nb_frequentation = 0

    def augmenter_nb_frequentation(self):
        self.nb_frequentation+=1

    def get_nb_frequentation(self):
        return self.nb_frequentation

    def s_abonne(self, abonnement):
        pass


    def se_desabonner(self):
        pass

    def nouvelle_voiture(self, hauteur, longueur, immatri):
        new_car = parking.voiture.Voiture(hauteur, longueur, immatri)
        pass


    def demander_maintenance(self):
        pass


    def demander_livraison(self, date, heure, adresse_livraison):
        pass


    def demander_entretien(self):
        pass

    def entrer_parking(self, acces):
        return ""
