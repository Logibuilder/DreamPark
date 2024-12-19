import pydoc

from parking import voiture
from parking.voiture import Voiture
from service.client import Client
from service.service import Service


class Ticket:
    def __init__(self, client, voiture):
        self.client = client
        self.voiture = voiture


    def get_voiture_de_ticket(self):
        return self.voiture


    def __str__(self):
        return (
            f"Client: {self.client.nom}\n"
            f"Voiture: {self.voiture.immatriculation}\n"
            f"Longueur: {self.voiture.longueur}, Hauteur: {self.voiture.hauteur}"
        )


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
        proposer les different types de service au client
        return : { choix }
        """
        return ""

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
        """
        Choisir un mode de paiement : carte ou espèce
        """
        payement = -1
        tentatives1 = 3  # Nombre maximal de tentatives pour choisir le mode de paiement

        # Choix du mode de paiement
        while (payement != 1 and payement != 2) and tentatives1 > 0:
            tentatives1 -= 1
            print(f"Choix invalide. Il vous reste {tentatives1} tentative(s).")
            try:
                payement = int(input("Veillez choisir un mode de paiement.\nPar espèce, taper 1. Par carte, taper 2: "))
            except ValueError:
                print("Saisie invalide. Veuillez entrer un nombre. { 1 ou 2 }")
                tentatives1 -= 1
                continue

        if tentatives1 == 0:
            print("Nombre de tentatives dépassé. L'opération est annulée.")
            return "Opération annulée"

        # Demander la somme de stationnement
        somme = -1
        tentatives2 = 3
        if payement == 1:

            # Vérification de la somme de stationnement
            while tentatives2 > 0:
                try:
                    somme = int(input("Saisir la somme de stationnement (30 euro) : "))
                    if somme == 30:
                        break
                    else:
                        tentatives2 -= 1
                        print(f"Montant incorrect. Il vous reste {tentatives2} tentative(s).")
                except ValueError:
                    print("Saisie invalide. Veuillez entrer un nombre entier(30) .")
                    tentatives2 -= 1
                    continue

        if tentatives2 == 0:
            print("Nombre de tentatives dépassé. L'opération est annulée.")
            return "Opération_annulée"

        return "Paiement_validé"

