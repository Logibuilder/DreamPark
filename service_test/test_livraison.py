import unittest


class MyTestCase(unittest.TestCase):
    """
    Auteur : Ulrich Babbel Mbonihankuye
 
    Suite a la demande d'un client le voiturier doit livrer sa voiture
    test_effectuer_livraison: prend en parametre un voiturier et une voiture

    on dois retourner "livraison livraison livraison"
    """
    def test_effectuer_livraison(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
