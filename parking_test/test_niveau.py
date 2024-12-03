import pydoc
import unittest


class TestNiveau(unittest.TestCase):
    """
        Auteur de cette classe : ASSANE KANE
    """

    def setUp(self):
        """Code pour initialiser les données de test"""
        pass


    def tearDown(self):
        """ Code pour nettoyer après le test"""
        pass


    def test_decrementer_nbplace_disponible(self):
        """verifier apres décrémentation que le nombre de place
         disponible a diminuer et que le nombre de place ocupees a augmenté"""
        pass



    def test_incrementer_nbplace_disponible(self):
        """verifier apres incrémentation que le nombre de place
         disponible a augmenter et que le nombre de place ocupées a diminué"""
        pass

    def test_decrementer_nbplace_occupees(self):
        """verifier apres décrémentation que le nombre de place
         occupées a diminué et que le nombre de place disponibles a augmenté"""
        pass

    def test_incrementer_nbplace_occupees(self):
        """verifier apres incrémentation que le nombre de place
         occupées a augmenter et que le nombre de place disponible a diminué"""
        pass

    pydoc.writedoc("test_niveau")



if __name__ == '__main__':
    unittest.main()
    
    
