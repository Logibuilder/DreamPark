import unittest
from unittest.mock import MagicMock
from service.client import Client
from parking.voiture import Voiture

# Auteur : Ulrich Babbel Mbonihankuye

class TestClient(unittest.TestCase):
    def setUp(self):
        """
        Initialisation d'un client "frais" avant chaque test pour s'assurer
        qu'il n'y a pas d'interf rence entre les diff rents tests.
        """
        self.client = Client("Alice", "123 Rue de Paris")

    def test_initialisation(self):
        """
        V rifie que les attributs par d faut sont correctement assign s.
        """
        self.assertEqual(self.client.nom, "Alice")
        self.assertEqual(self.client.adresse, "123 Rue de Paris")
        self.assertEqual(self.client.nb_frequentation, 0)
        self.assertFalse(self.client.est_abonne)
        self.assertIsNone(self.client.myCar)

    def test_augmenter_nb_frequentation(self):
        """
        V rifie que la m thode augmenter_nb_frequentation incr mente correctement le compteur de fr quentation.
        """
        self.client.augmenter_nb_frequentation()
        self.assertEqual(self.client.nb_frequentation, 1)

    def test_get_nb_frequentation(self):
        """
        V rifie que la m thode get_nb_frequentation retourne le nombre correct de fr quentations.
        """
        self.client.augmenter_nb_frequentation()
        self.client.augmenter_nb_frequentation()
        self.assertEqual(self.client.get_nb_frequentation(), 2)

    def test_ajouter_voiture(self):
        """
        V rifie que la m thode ajouter_voiture associe correctement une instance de la classe Voiture au client.
        """
        voiture_test = Voiture(1.5, 4.2, "AB-123-CD")
        self.client.ajouter_voiture(voiture_test)
        
        self.assertIsNotNone(self.client.myCar)
        self.assertEqual(self.client.myCar.immatriculation, "AB-123-CD")
        self.assertEqual(self.client.myCar.hauteur, 1.5)

    def test_demander_maintenance(self):
        """
        V rifie que la m thode s'ex cute sans erreur (en attendant son impl mentation future).
        """
        self.client.demander_maintenance()

    def test_demander_livraison(self):
        """
        V rifie que la m thode s'ex cute sans erreur avec les bons param tres.
        """
        self.client.demander_livraison("2026-07-20", "14:00", "123 Rue de Paris")

    def test_entrer_parking(self):
        """
        V rifie que la m thode entrer_parking interagit correctement avec l'objet Acces.
        """
        # On cr e un "Mock" (un faux objet) pour simuler la classe Acces
        mock_acces = MagicMock()
        
        # Le client entre dans le parking
        self.client.entrer_parking(mock_acces)
        
        # On v rifie que le client a bien d clench  la m thode `direBonjour` de la borne d'acc s
        mock_acces.direBonjour.assert_called_once_with(self.client)

if __name__ == '__main__':
    unittest.main()