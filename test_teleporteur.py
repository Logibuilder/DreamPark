import unittest
import pydoc
from Parking.ticket import Ticket 
from Parking.teleporteur import Teleporteur

class MyTestCase(unittest.TestCase):
    """
        Auteur de cette classe : ASSANE KANE
    """
    def setUp(self):
        """valeur pour simuler le test de téléportation de la voiture"""
        self.num=Teleporteur(1)
        self.ticket= Ticket("Ulrich", "ABC-123")

    def test_teleporter_voiture_garer(self):
        pass
    def test_teleporter_voiture_recuperer(self):
        """verifie que le message de téléportation est bien confirmé"""
        self.resultat = Teleporteur.teleporter_voiture(self, self.ticket, "recuper")
        self.assertEqual(self.resultat,f"Voiture associée au ticket {self.ticket} récupérée.")

if __name__ == '__main__':
    unittest.main()
