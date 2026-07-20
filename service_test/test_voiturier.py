import unittest
from service.voiturier import Voiturier
from parking.voiture import Voiture

class TestVoiturier(unittest.TestCase):
    """
    Auteur: Mbonihankuye Ulrich Babbel
    le test_livrer_voiture verifie que la voiture est livr e en comparant les chaines de caracteres.
    """
    def test_livrer_voiture(self):
        voiturier = Voiturier("Paul", 1)
        voiture_test = Voiture(1.5, 4.2, "AB-123-CD")
        
        resultat = voiturier.livrer_voiture(voiture_test, "2026-07-20", "17:00")
        
        self.assertEqual(resultat, "Voiture livrer")

if __name__ == '__main__':
    unittest.main()