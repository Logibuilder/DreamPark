import pydoc

from controller.ticket import Ticket


class BorneTicket:
    """
    Auteur de cette classe : ASSANE KANE
    """

    def __init__(self, ticket_no):
        '''

        '''
        pass
    def delivrer_ticket(self, client, voiture):
        """
            parametre: client
            return / ticket (string)
        """
        ticket = Ticket(client, voiture)
        return ticket

    def proposer_services(self):
        """
        Propose différents services disponibles pour les clients.
        Retourne le choix du client ou 'Annuler' si aucun choix n'est fait.
        """
        print("=== Services Disponibles ===")
        print("1. Livraison de voiture à une adresse spécifique")
        print("2. Entretien du véhicule")
        print("3. Maintenance du véhicule")
        print("4. Annuler")

        choix = -1
        tentatives = 3  # Limite des tentatives de choix
        while choix not in [1, 2, 3, 4] and tentatives > 0:
            try:
                choix = int(input("Veuillez choisir un service (1-4) : "))
                if choix not in [1, 2, 3, 4]:
                    tentatives -= 1
                    print(f"Choix invalide. Il vous reste {tentatives} tentative(s).")
            except ValueError:
                tentatives -= 1
                print(
                    f"Entrée invalide. Veuillez entrer un nombre entre 1 et 4. Il vous reste {tentatives} tentative(s).")

        if tentatives == 0 or choix == 4:
            print("Nombre de tentatives dépassé ou choix annulé.")
            return "annuler" , ""

        if choix == 1:
            adresse = input("Veuillez saisir l'adresse de livraison : ")
            heure = input("Veuillez saisir l'heure de livraison (format HH:MM) : ")
            print(f"Service de livraison sélectionné. Adresse : {adresse}, Heure : {heure}.")
            return "livraison", {"adresse": adresse, "heure": heure}
        elif choix == 2:
            print("Vous avez choisi le service : Entretien du véhicule.")
            return "entretien" , ""
        elif choix == 3:
            print("Vous avez choisi le service : Maintenance du véhicule.")
            return "maintenance" , ""

    def prooser_abonnements(self, client, parking):
        """
            proposer les different types d'abonnements au client
            return : { choix }
        """
        return ""

    def recuper_Info_Carte(self, client):
        """
        recupere les info de la carte du client au debut du processus SE GARER
        """
        pass

    '''def proposer_type_paiement(self):
        """
        input("choisir mode de payement {carte, espece")
        """
        payement = -1
        tentatives = 3  # Nombre maximal de tentatives pour choisir le mode de paiement
        while (payement != 1 and payement != 2) and tentatives > 0:
            tentatives -= 1
            print(f"Choix invalide. Il vous reste {tentatives} tentative(s).")
            payement = int(input("Veillez choisir un mode un payement.\nPar espece, taper 1 par carte, tapez 2: "))

        if tentatives == 0:
            print("Nombre de tentatives dépassé. L'opération est annulée.")
            return "Opération annulée"


        somme = 0
        if payement == 1 :
            somme = int(input("saisir la somme de stationnement: "))
            tentatives = 3
        while tentatives > 0 :
            try :
                somme = int(input("saisir la somme de stationnement(30): "))
                if somme == 30 :
                    break
                else :
                    print("Montant incorrect. Il vous reste {tentatives} tentative(s).")
                    tentatives -= 1
            except ValueError:
                print("Saisie invalide. Veuillez entrer un nombre entier.")
                tentatives -= 1
        if tentatives == 0:
            print("Nombre de tentatives dépassé. L'opération est annulée.")
            return "Opération_annulée"

        return "payement_validé"'''

    def proposer_type_paiement(self):
        """Propose un mode de paiement et vérifie la somme de paiement."""
        paiement = self.choisir_mode_paiement()
        if paiement is None:
            return "Opération annulée"

        if paiement == 1:  # Paiement par espèce
            return self.gestion_paiement_espece()

        return "Paiement validé"  # Si paiement par carte, on suppose que c'est validé

    def choisir_mode_paiement(self):
        """Choisir le mode de paiement."""
        paiement = -1
        tentatives = 3
        while paiement not in [1, 2] and tentatives > 0:
            tentatives -= 1
            try:
                paiement = int(input("Veuillez choisir un mode de paiement. Par espèce, tapez 1; par carte, tapez 2: "))
                if paiement not in [1, 2]:
                    print(f"Choix invalide. Il vous reste {tentatives} tentative(s).")
            except ValueError:
                print(f"Entrée invalide. Veuillez entrer un nombre. Il vous reste {tentatives} tentative(s).")

        if tentatives == 0:
            print("Nombre de tentatives dépassé. L'opération est annulée.")
            return None

        return paiement

    def proposer_type_paiement(self):
        """Propose un mode de paiement et vérifie la somme de paiement."""
        paiement = self.choisir_mode_paiement()
        if paiement is None:
            return "Opération annulée"

        if paiement == 1:  # Paiement par espèce
            return self.gestion_paiement_espece()

        return "Paiement validé"  # Si paiement par carte

    def gestion_paiement_espece(self):
        """Gère le paiement par espèce."""
        tentatives = 3
        while tentatives > 0:
            try:
                somme = int(input("Saisir la somme de stationnement (30 euros) : "))
                if somme == 30:
                    print("Paiement validé")
                    return "Paiement validé"
                else:
                    tentatives -= 1
                    print(f"Montant incorrect. Il vous reste {tentatives} tentative(s).")
            except ValueError:
                tentatives -= 1
                print(f"Saisie invalide. Il vous reste {tentatives} tentative(s).")
        print("Nombre de tentatives dépassé. L'opération est annulée.")
        return "Opération annulée"

#pydoc.writedoc("borne_ticket")
