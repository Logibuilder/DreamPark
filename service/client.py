import pydoc
import parking.voiture


class Client:

    """
        Classe représentant un client du parking.
        Un client peut être abonné ou non, avoir un historique de fréquentation,
        et ectuer diverses actions comme demander des services ou ajouter une voiture.
    """
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.est_abonne = False
        self.est_super_abonne = False
        self.nb_frequentation = 0

    def augmenter_nb_frequentation(self):
        """
        Incrémente le compteur de fréquentations du client.
        """
        self.nb_frequentation+=1

    def get_nb_frequentation(self):
        """
        Retourne le nombre de fréquentations du client.

        :return: Nombre de visites du client (type: int).
        """
        return self.nb_frequentation

    def s_abonner(self, abonnement):
        """
        Permet au client de souscrire un abonnement.
        Cette méthode devra être implémentée pour gérer les détails de l'abonnement.

        :param abonnement: Détails de l'abonnement (type attendu: Abonnement ou similaire).
        """
        pass


    def se_desabonner(self):
        """
        Permet au client de se désabonner.
        Cette méthode devra être implémentée pour gérer la désinscription.
        """
        pass

    def nouvelle_voiture(self, hauteur, longueur, immatri):
        """
        Permet au client d'ajouter une nouvelle voiture à son compte.

        :param hauteur: Hauteur de la voiture (type: float).
        :param longueur: Longueur de la voiture (type: float).
        :param immatri: Immatriculation de la voiture (type: str).
        """
        new_car = parking.voiture.Voiture(hauteur, longueur, immatri)
        pass


    def demander_maintenance(self):
        """
        Permet au client de demander une maintenance pour son véhicule.
        Cette méthode devra être implémentée.
        """
        pass


    def demander_livraison(self, date, heure, adresse_livraison):
        """
        Permet au client de demander une livraison de son véhicule.

        :param date: Date de la livraison (type: datetime.date ou similaire).
        :param heure: Heure de la livraison (type: datetime.time ou similaire).
        :param adresse_livraison: Adresse de livraison (type: str).
        """
        pass


    def demander_entretien(self):
        """
        Permet au client de demander un entretien pour son véhicule.
        Cette méthode devra être implémentée.
        """
        pass

    def entrer_parking(self, acces):
        """
        Permet au client d'entrer dans le parking via un accès spécifique.

        :param acces: Point d'accès utilisé par le client (type: Acces ou similaire).
        :return: Confirmation ou statut de l'entrée (type: str ou similaire).
        """
        return ""


    def estAbonne (self):
        return self.est_abonne

    def est_super_abonne(self):
        return self.est_super_abonne


#pydoc.writedoc("client")