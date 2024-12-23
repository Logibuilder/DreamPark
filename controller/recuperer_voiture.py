from controller.se__garer import seGarerSansAbonne
from controller.ticket import Ticket
from parking.acces import Acces
from parking.borne_ticket import BorneTicket
from parking.gestion_parking import Parking
from parking.place import Place
from parking.voiture import Voiture
from service.client import Client
from parking.teleporteur import Teleporteur

instanceBorneTicket = BorneTicket(1)


def recuperer_voiture(acces, ticket, teleporteur):
    ticket = acces.presenterTicket(ticket)

    acces.lancer_procedure_sortie(ticket, teleporteur)

    print("Merci d'avoir utilisé DreamPark !")


acces = Acces("acces A")

# Exemple de voitures avec différentes dimensions pour tester les niveaux du parking

# Voiture 1 : Petite, adaptée à tous les niveaux
voiture_1 = Voiture(1.5, 3.5, "Voiture Petite")




"""client_1 = Client("Assane", "adresse")

client_1.ajouter_voiture(voiture_1)  # Ajouter explicitement une voiture au client

seGarerSansAbonne(Acces("dg"), client_1)

teleporteur = Teleporteur(1)

place = Place(0, "B", 1, 1)

ticket = Ticket(client_1, place, "catre")

recuperer_voiture(Acces("dg"), ticket, teleporteur)

print(Parking)"""