import  pydoc
import unittest
from parking.place import Place  # Assurez-vous que le chemin d'importation est correct


class TestPlace(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE
    """

    def setUp(self):
        """
        Configuration avant chaque test.
        Crée une instance de Place pour les tests.
        """
        self.place = Place(1, "A", 5.0, 2.5)

    def tearDown(self):
        """
        Nettoyage après chaque test.
        """
        self.place = None

    def test_initialisation_place(self):
        """
        Vérifie que l'initialisation de la place est correcte.
        """
        self.assertEqual(self.place.numero, 1)
        self.assertEqual(self.place.niveau, "A")
        self.assertEqual(self.place.longeur, 5.0)
        self.assertEqual(self.place.hauteur, 2.5)
        self.assertTrue(self.place.est_libre)
        self.assertEqual(self.place.id, "A001")

    def test_set_valeur_libre(self):
        """
        Vérifie que la méthode set_valeur_libre modifie correctement l'état de la place.
        """
        self.place.set_valeur_libre(False)
        self.assertFalse(self.place.est_libre)
        self.place.set_valeur_libre(True)
        self.assertTrue(self.place.est_libre)

    def test_str(self):
        """
        Vérifie que la méthode __str__ retourne la bonne représentation de la place.
        """
        # Vérifie que l'état initial est libre
        self.assertEqual(str(self.place), "\033[92mA001\033[0m ✅")

        # Changer l'état de la place à occupée et vérifier à nouveau
        self.place.set_valeur_libre(False)
        self.assertEqual(str(self.place), "\033[91mA001\033[0m ❌")


if __name__ == '__main__':
    pydoc.writedoc("TestPlace")
    unittest.main()
