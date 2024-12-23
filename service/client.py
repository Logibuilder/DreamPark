import pydoc

import parking
from parking.voiture import Voiture


class Client:
    listeClients = []
    """
        Classe représentant un client du parking.
        Un client peut être abonné ou non, avoir un historique de fréquentation,
        et ectuer diverses actions comme demander des services ou ajouter une voiture.
    """
    def __init__(self, nom, adresse):
        self.nom = nom
        self.myCar = None
        self.adresse = adresse
        self.est_abonne = False
        self.est_super_abonne = False
        self.nb_frequentation = 0

    def ajouter_voiture(self, voiture=None):
        """
        Permet au client d'ajouter une voiture à son compte.
        Si une voiture est fournie, elle est directement associée.
        Sinon, l'utilisateur est invité à en ajouter une via des inputs.

        :param voiture: (Optionnel) Une voiture à ajouter au client.
                        Si None, une nouvelle voiture est créée via l'interaction utilisateur.
        """
        if voiture:
            # Si une voiture est fournie, on l'associe directement au client.
            self.myCar = voiture
        else:
            # Si aucune voiture n'est fournie, on demande à l'utilisateur d'en ajouter une.
            print(f"\n=== Ajout d'une voiture pour {self.nom} ===")

            # Boucle pour gérer les erreurs sur la hauteur de la voiture
            while True:
                try:
                    hauteur = float(input("Entrez la hauteur de votre voiture (en mètres) : "))
                    if hauteur <= 0:
                        print("La hauteur doit être un nombre positif. Essayez à nouveau.")
                        continue
                    break  # Sortie de la boucle si l'entrée est valide
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre pour la hauteur.")

            # Boucle pour gérer les erreurs sur la longueur de la voiture
            while True:
                try:
                    longueur = float(input("Entrez la longueur de votre voiture (en mètres) : "))
                    if longueur <= 0:
                        print("La longueur doit être un nombre positif. Essayez à nouveau.")
                        continue
                    break  # Sortie de la boucle si l'entrée est valide
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre pour la longueur.")

            # Demander et valider l'immatriculation
            while True:
                immatriculation = input("Entrez l'immatriculation de votre voiture : ").strip()
                if not immatriculation:
                    print("L'immatriculation ne peut pas être vide. Essayez à nouveau.")
                    continue
                # Optionnel: Ajouter une validation du format d'immatriculation
                if len(immatriculation) < 5:  # Par exemple, une immatriculation doit avoir au moins 5 caractères
                    print("L'immatriculation doit comporter au moins 5 caractères. Essayez à nouveau.")
                    continue
                break  # Sortie de la boucle si l'immatriculation est valide

            # Création de la voiture et association au client
            self.myCar = Voiture(hauteur, longueur, immatriculation)
            print(f"Voiture ajoutée pour {self.nom}")


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
        acces.direBonjour(self)


    def estAbonne (self):
        return self.est_abonne

    def est_super_abonne(self):
        return self.est_super_abonne


    @staticmethod
    def inscrire_client():
        """
        Inscrit un nouveau client via une interaction directe dans le terminal,
        avec vérification de l'existence du client.
        Si le client existe déjà, l'inscription échoue.
        """
        print("=== Inscription d'un nouveau client ===")
        nom = input("Entrez votre nom : ")
        adresse = input("Donnez votre adresse : ")

        # Vérification si le client existe déjà
        for client in Client.listeClients:
            if client.nom == nom and client.adresse == adresse:
                print(f"\n❌ Un client avec ce nom et cette adresse existe déjà. L'inscription a échoué.\n")
                return client  # Retourner le client existant si trouvé

            # Si le client n'existe pas, on crée et ajoute un nouveau client à la liste
        nouveau_client = Client(nom, adresse)
        Client.listeClients.append(nouveau_client)

        print(f"\n🎉 Vous avez été inscrit avec succès, {nom} !\n")

        # Demander à l'utilisateur s'il souhaite ajouter une voiture
        reponse = input("Souhaitez-vous ajouter une voiture maintenant ? (oui/non) : ").strip().lower()
        if reponse == "oui":
            Client.ajouter_voiture(nouveau_client)
        else:
            print("\n🚗 Vous pourrez ajouter une voiture plus tard si nécessaire.\n")


    @staticmethod
    def afficher_clients():
        """
        Affiche tous les clients inscrits dans la liste des clients.
        """
        print("\n=== Liste des clients inscrits ===")
        if not Client.listeClients:
            print("Aucun client n'est encore inscrit.")
        else:
            print("Voici la liste des clients inscrits :")
            for i, client in enumerate(Client.listeClients, start=1):
                voiture = client.myCar.immatriculation if client.myCar else "Aucune voiture"
                print(f"{i}. Nom : {client.nom}, Adresse : {client.adresse}, Voiture : {voiture}")
        print("\n")

    @classmethod
    def rechercher_client_par_nom(cls, nom_client):
        """
        Recherche un client dans la liste des clients inscrits par son nom.

        :param nom_client: Le nom du client à rechercher (type: str).
        :return: Le client correspondant si trouvé, sinon None.
        """
        for client in cls.listeClients:
            if client.nom.lower() == nom_client.lower():  # Comparaison insensible à la casse
                return client
        return None  # Aucun client trouvé


#pydoc.writedoc("client")
