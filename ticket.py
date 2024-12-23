from parking.voiture import Voiture
from service.client import Client
class Ticket:
    def __init__(self, client: Client, voiture: Voiture):
        self.nomclient = client
        self.immatvoiture = voiture
        self.numticket=""

    def creationTicket(self):
        self.numticket= f"T-{self.nomclient.nom}-{self.immatvoiture.immatriculation}"
        return self.numticket

    def __str__(self):
        #Retourne une représentation lisible d'un ticket
        return f"{self.numticket}, Client: {self.nomclient}"