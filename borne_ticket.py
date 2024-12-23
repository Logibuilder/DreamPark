# import pydoc 
from service.client import Client
from Parking.voiture import Voiture 
from Parking.ticket import Ticket
        
class BorneTicket:
    """
    Auteur de cette classe : ASSANE KANE
    """

    def __init__(self, num_borne):
        """
        initialisation  d'une borne avec un num
        """
        self.num=num_borne
        self.tickets=[] #liste pour stocker les tickets livré
        


    def delivrer_ticket(self, client: Client, voiture: Voiture):
        """
            parametre: client, Voiture
            return / ticket (string)
        """
        self.Ticket= Ticket(client, voiture)
        self.Ticket.creationTicket()
        self.tickets.append(self.Ticket)

        return self.Ticket
    
    def afficher_liste_ticket(self):
        for t in range(len(self.tickets)):
            print(self.tickets[t])


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
    def proposer_type_paiement(self):
        """
        Propose à l'utilisateur de choisir un mode de paiement (carte ou espèces).
        :return: Le mode de paiement choisi.
        """
        print("=== Choisissez un mode de paiement ===")
        print("1. Carte")
        print("2. Espèces")

        essais = 3
        while essais > 0:
            choix = input("Entrez le numéro correspondant à votre choix (1 ou 2) : ")
            if choix == "1":
                print("Vous avez choisi le mode de paiement : Carte.")
                return "carte"
            elif choix == "2":
                print("Vous avez choisi le mode de paiement : Espèces.")
                return "espèces"
            else:
                essais -= 1
                print(f"Choix invalide. Il vous reste {essais} essai(s).")

        print("Vous avez dépassé le nombre d'essais autorisés.")
        return None

    def presenter_ticket(self, ticket):
        """
        cette methode permet au client de présenter son ticket pour reccuperer sa voiture
        :param ticket: Numéro du ticket unique présenter par le client

        """
        print("Vérification du ticket en cours")
        if ticket in self.tickets :
            print("préparation du téléporteur pour recupérer votre voiture")
            self.tickets.remove(ticket)
            return True 
        else :
            print("Ticket invalide. Veuillez réessayer.")
            return False 



# pydoc.writedoc("borne_ticket")
