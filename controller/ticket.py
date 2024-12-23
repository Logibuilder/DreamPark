import ticket
from parking.place import Place
from service.client import Client


class Ticket:
    listeTickets = []
    nbTickets = 0


    def __init__(self, client, place, mode_pay):
        self.client = client
        self.place = place
        self.nom = place.id
        self.mode_paiement = mode_pay
        self.numticket = Ticket.nbTickets  # Fixer le numéro de ticket à la valeur actuelle de nbTickets
        Ticket.nbTickets += 1  # Incrémenter nbTickets après l'assignation
        Ticket.listeTickets.append(self)


    def imprimerTicket(self , bool):
        if bool:
            print(self)
        else :
            print("Au revoir")

    def delivrerTicket(self):
        print(self)

    def __str__(self):
        return (
            "\n"
            "╔═════════════════════════════════════════╗\n"
            "║           🎟️  *** TICKET *** 🎟️         ║\n"
            "╠═════════════════════════════════════════╣\n"
            f"║  Numéro      : {self.numticket: <25}║\n"
            f"║  Client      : {self.client.nom: <25}║\n"
            f"║  Place       : {self.nom: <25}║\n"
            f"║  Paiement    : {self.mode_paiement: <25}║\n"
            "╠═════════════════════════════════════════╣\n"
            "║   Merci de votre visite et à bientôt !  ║\n"
            "╚═════════════════════════════════════════╝\n"
        )

    @classmethod
    def findByNum(cls, num):
        """
        Recherche un ticket dans la liste des tickets par son numéro.
        :param numero_ticket: Numéro du ticket à rechercher.
        :return: Le ticket correspondant ou None si introuvable.
        """
        print(f"Liste des tickets : {[ticket.numticket for ticket in cls.listeTickets]}")  # Debug print
        for ticket in Ticket.listeTickets:
            if ticket.numticket == num:
                return ticket
        return None  # Aucun ticket trouvé
    @staticmethod
    def afficher_tous_les_tickets():
        """
        Affiche tous les tickets présents dans la liste.
        """
        if  Ticket.listeTickets is []:
            print("Aucun ticket trouvé.")
        else:
            print("\n=== Liste des tickets ===")
            for ticket in Ticket.listeTickets:
                print(ticket)





# Exemple de création d'un ticket
client = Client(nom="assane", adresse="adr")
# Correctement initialiser un objet Place avec les bons paramètres
place = Place(numero=1, niveau="A", longeur=3, hauteur=2)  # En supposant que c'est une place de 3m x 2m

ticket = Ticket(client, place, "carte")


ticket_recherche = Ticket.findByNum(0)  # Recherche du ticket numéro 0
if ticket_recherche:
    print("Ticket trouvé : ", ticket_recherche)
else:
    print("Ticket non trouvé.")
