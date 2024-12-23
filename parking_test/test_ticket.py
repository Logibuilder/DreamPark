from unittest.mock import patch

from controller.ticket import Ticket
from parking.place import Place
from service.client import Client
import unittest
import pydoc

class TestTicket(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE

    Classe de tests pour la classe Ticket.
    """

    def setUp(self):
        """
        Configuration avant chaque test.
        Crée une instance de Client, de Place, et de Ticket pour les tests.
        """
        self.client = Client(nom="Assane", adresse="Paris")
        self.place = Place(numero=1, niveau="A", longeur=3, hauteur=2)  # Place de parking de 3m x 2m
        self.ticket = Ticket(self.client, self.place, "carte")  # Création d'un ticket

    def tearDown(self):
        """
        Nettoyage après chaque test.
        """
        Ticket.listeTickets.clear()  # Vide la liste des tickets pour éviter des interférences entre les tests
        Ticket.nbTickets = 0  # Réinitialise le compteur des tickets

    def test_initialisation_ticket(self):
        """
        Vérifie l'initialisation correcte du ticket.
        """
        self.assertEqual(self.ticket.numticket, 0)  # Le premier ticket doit avoir le numéro 0
        self.assertEqual(self.ticket.client.nom, "Assane")  # Le nom du client doit être "Assane"
        self.assertEqual(self.ticket.place.id, "A001")  # L'id de la place doit être "A001"
        self.assertEqual(self.ticket.mode_paiement, "carte")  # Le mode de paiement doit être "carte"

    def test_findByNum(self):
        """
        Vérifie la méthode findByNum pour retrouver un ticket par son numéro.
        """
        ticket_recherche = Ticket.findByNum(0)
        self.assertIsNotNone(ticket_recherche)  # Le ticket doit être trouvé
        self.assertEqual(ticket_recherche.numticket, 0)  # Le ticket trouvé doit avoir le numéro 0

        ticket_non_trouve = Ticket.findByNum(1)
        self.assertIsNone(ticket_non_trouve)  # Aucun ticket avec le numéro 1 ne doit être trouvé

    def test_afficher_tous_les_tickets(self):
        """
        Vérifie que la méthode afficher_tous_les_tickets affiche correctement tous les tickets.
        """
        ticket_2 = Ticket(self.client, self.place, "espèces")  # Création d'un autre ticket
        Ticket.afficher_tous_les_tickets()  # Devrait afficher les deux tickets dans la liste



if __name__ == "__main__":
    pydoc.writedoc("testTicket")
    unittest.main()
