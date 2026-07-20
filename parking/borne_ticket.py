import pydoc
from controller.ticket import Ticket

class BorneTicket:
    """
    Auteur de cette classe : ASSANE KANE
    """
    def __init__(self, num_borne):
        self.num = num_borne
        self.tickets = []  # Ajout de la liste des tickets (qui  tait dans l'autre fichier)

    def delivrer_ticket(self, client, voiture):
        """
        Param tres: client, voiture
        Return: ticket (objet Ticket)
        """
        ticket = Ticket(client, voiture, "non d fini") # Ajout d'un mode de paiement par d faut pour la cr ation
        self.tickets.append(ticket)
        return ticket

    def proposer_services(self):
        """
        Propose diff rents services disponibles pour les clients.
        Retourne le choix du client ou 'annuler' si aucun choix n'est fait.
        """
        print("=== Services Disponibles ===")
        print("1. Livraison de voiture   une adresse sp cifique")
        print("2. Entretien du v hicule")
        print("3. Maintenance du v hicule")
        print("4. Annuler")
        
        tentatives = 3
        while tentatives > 0:
            try:
                choix = int(input("Veuillez choisir un service (1-4) : "))
                if choix == 1:
                    adresse = input("Veuillez saisir l'adresse de livraison : ")
                    heure = input("Veuillez saisir l'heure de livraison (format HH:MM) : ")
                    print(f"Service de livraison s lectionn . Adresse : {adresse}, Heure : {heure}.")
                    return "livraison", {"adresse": adresse, "heure": heure}
                elif choix == 2:
                    print("Vous avez choisi le service : Entretien du v hicule.")
                    return "entretien", ""
                elif choix == 3:
                    print("Vous avez choisi le service : Maintenance du v hicule.")
                    return "maintenance", ""
                elif choix == 4:
                    print("Op ration annul e.")
                    return "annuler", ""
                else:
                    tentatives -= 1
                    print(f"Choix invalide. Il vous reste {tentatives} tentative(s).")
            except ValueError:
                tentatives -= 1
                print(f"Entr e invalide. Veuillez entrer un nombre. Il vous reste {tentatives} tentative(s).")
                
        print("Nombre de tentatives d pass  ou choix annul .")
        return "annuler", ""

    def proposer_abonnements(self, client, parking):
        """
        Propose les diff rents types d'abonnements au client
        """
        pass

    def recuper_Info_Carte(self, client):
        """
        R cup re les infos de la carte du client au d but du processus SE GARER
        """
        pass

    def proposer_type_paiement(self):
        """Propose un mode de paiement et v rifie la somme de paiement."""
        paiement = self.choisir_mode_paiement()
        
        if paiement is None:
            return "Op ration annul "
            
        if paiement == 1:  # Paiement par esp ces
            return self.gestion_paiement_espece()
            
        return "Paiement valid "  # Si paiement par carte

    def choisir_mode_paiement(self):
        """Choisir le mode de paiement."""
        tentatives = 3
        while tentatives > 0:
            try:
                paiement = int(input("Veuillez choisir un mode de paiement. Par esp ce tapez 1, par carte tapez 2 : "))
                if paiement in [1, 2]:
                    return paiement
                else:
                    tentatives -= 1
                    print(f"Choix invalide. Il vous reste {tentatives} tentative(s).")
            except ValueError:
                tentatives -= 1
                print(f"Entr e invalide. Veuillez entrer un nombre. Il vous reste {tentatives} tentative(s).")
                
        print("Nombre de tentatives d pass . L'op ration est annul e.")
        return None

    def gestion_paiement_espece(self):
        """G re le paiement par esp ce."""
        tentatives = 3
        while tentatives > 0:
            try:
                somme = int(input("Saisir la somme de stationnement (30 euros) : "))
                if somme == 30:
                    print("Paiement valid .")
                    return "Paiement valid "
                else:
                    tentatives -= 1
                    print(f"Montant incorrect. Il vous reste {tentatives} tentative(s).")
            except ValueError:
                tentatives -= 1
                print(f"Saisie invalide. Il vous reste {tentatives} tentative(s).")
                
        print("Nombre de tentatives d pass . L'op ration est annul e.")
        return "Op ration annul "