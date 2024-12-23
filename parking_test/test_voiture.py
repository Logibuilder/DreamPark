import unittest

from parking.voiture import Voiture


class TestVoiture(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE
    """

    def setUp(self):
        """
        Configuration avant chaque test.
        Crée une instance de Voiture pour les tests.
        """
        self.voiture = Voiture(1.5, 4.0, "AB-123-CD")

    def tearDown(self):
        """
        Nettoyage après chaque test.
        """
        self.voiture = None

    def test_initialisation_voiture(self):
        """
        Vérifie que l'initialisation de la voiture est correcte.
        """
        self.assertEqual(self.voiture.hauteur, 1.5)
        self.assertEqual(self.voiture.longueur, 4.0)
        self.assertEqual(self.voiture.immatriculation, "AB-123-CD")
        self.assertFalse(self.voiture.est_dans_parking)

    def test_add_placement(self):
        """
        Vérifie que la méthode add_placement fonctionne correctement.
        """
        # Simule l'ajout d'une place de parking
        placement = "A1"  # Exemple de placement
        self.assertTrue(self.voiture.add_placement(placement))
        self.assertTrue(self.voiture.est_dans_parking)

if __name__ == '__main__':
    unittest.main()
