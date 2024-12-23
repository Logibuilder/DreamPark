import unittest
from parking.gestion_parking import Parking
from parking.niveau import Niveau
from parking.place import Place
from service.client import Client
from controller.ticket import Ticket
import io
from contextlib import redirect_stdout

class TestParking(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE

    Classe de test pour la classe Parking.
    """

    def setUp(self):
        """Initialisation avant chaque test."""
        self.parking = Parking()

    def test_singleton(self):
        """Teste si Parking est bien un singleton."""
        parking2 = Parking()
        self.assertIs(self.parking, parking2, "Parking n'est pas un singleton")

    def test_init_attributes(self):
        """Teste l'initialisation des attributs du parking."""
        self.assertEqual(self.parking.nbPlacesParNiveau, 50)
        self.assertEqual(self.parking.nbPlacesLibre, 250)
        self.assertEqual(self.parking.prix, 30)
        self.assertEqual(self.parking.nbNiveau, 4)
        self.assertEqual(len(self.parking.lesNiveau), 4)

    def test_rechercherPlace(self):
        """Teste la recherche d'une place avec différentes hauteurs et longueurs."""
        place = self.parking.rechercherPlace(1.80, 4)  # devrait trouver une place dans A ou B
        self.assertIsInstance(place, Place, "La place trouvée n'est pas une instance de Place")
        self.assertIsNotNone(place, "Aucune place trouvée pour une voiture de hauteur 1.80m et longueur 4m")

        place = self.parking.rechercherPlace(2.80, 8)  # ne devrait pas trouver de place
        self.assertIsNone(place, "Une place a été trouvée pour une voiture trop grande")

    def test_nb_places_libres_libre(self):
        """Teste la méthode pour compter le nombre de places libres dans tout le parking."""
        nb_places_libres = self.parking.nb_places_libres_libre()
        self.assertGreater(nb_places_libres, 0, "Il devrait y avoir des places libres.")

    def test_afficherCurrentSituation(self):
        """Teste si on peut appeler la méthode d'affichage sans erreur."""
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            self.parking.afficherCurrentSituation()
        self.assertGreater(len(captured_output.getvalue()), 0, "Il devrait y avoir une sortie pour chaque niveau.")

    def test_str(self):
        """Teste la représentation en chaîne de caractères du parking."""
        parking_str = str(self.parking)
        self.assertIsInstance(parking_str, str)
        self.assertGreater(len(parking_str), 0, "La représentation en chaîne ne devrait pas être vide")

if __name__ == '__main__':
    unittest.main()