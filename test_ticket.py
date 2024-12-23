import unittest
from Parking.ticket import Ticket
from Parking.voiture import Voiture
from service.client import Client

class TestBorneTicket(unittest.TestCase):
    def test_creation_ticket(self):
        Babbel = Client("Ulrich", 123)
        V = Voiture(2, 3.4, "ABC-123")
        
        # Créer un ticket
        ticket = Ticket(Babbel, V)
        
        # Appeler la méthode creationTicket
        creation = ticket.creationTicket()
        
        print(creation)  # Afficher le ticket
