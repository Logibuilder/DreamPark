import unittest
from service.client import Client
"""
Auteur : Ulrich Babbel Mbonihankuye
"""

class MyTestCase(unittest.TestCase):
    def test_initialisation(self):
      pass

    def test_augmenter_nb_frequentation(self):
        """
        Vérifie que la méthode augmenter_nb_frequentation incrémente correctement le compteur de fréquentation.
        """
        pass

    def test_get_nb_frequentation(self):
        """
        Vérifie que la méthode get_nb_frequentation retourne le nombre correct de fréquentations.        
        """
        pass

    def test_nouvelle_voiture(self):
        """
        Vérifie que la méthode nouvelle_voiture crée correctement une instance de la classe Voiture.
        """
    def test_demander_maintenance(self):
        """
        Vérifie que la méthode demander_maintenance enregistre correctement une demande de maintenance.
        """
    def test_demander_livraison(self):
        """
        Vérifie que la méthode demander_livraison enregistre correctement une demande de livraison.
        """
    def entrer_parking(self):
        """
        Vérifie que la méthode entrer_parking fonctionne correctement, 
        notamment qu'elle interagit avec l'objet Acces (ou équivalent).
        """
if __name__ == '__main__':
    unittest.main()

