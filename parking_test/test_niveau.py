import unittest
from parking.niveau import Niveau

class TestNiveau(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE
    """
    def setUp(self):
        """Code pour initialiser les donn es de test"""
        # Cr ation d'un niveau "A" de test avec 50 places au total, 
        # acceptant des voitures jusqu'  2.0m de haut et 5.0m de long.
        self.niveau = Niveau("A", 50, 2.0, 5.0)

    def tearDown(self):
        """ Code pour nettoyer apr s le test"""
        self.niveau = None

    def test_decrementer_nbplace_disponible(self):
        """
        V rifie qu'apr s d cr mentation, le nombre de places disponibles 
        a diminu  et que le nombre de places occup es a augment .
        """
        # tat initial : 50 disponibles, 0 occup e
        self.niveau.decrementer_nbplace_disponible()
        
        self.assertEqual(self.niveau.nbplace_disponible, 49)
        self.assertEqual(self.niveau.nbplace_occupees, 1)

    def test_incrementer_nbplace_disponible(self):
        """
        V rifie qu'apr s incr mentation, le nombre de places disponibles 
        a augment  et que le nombre de places occup es a diminu .
        """
        # On force d'abord l'occupation d'une place pour pouvoir la lib rer
        self.niveau.nbplace_disponible = 49
        self.niveau.nbplace_occupees = 1
        
        # On lib re la place (on incr mente les dispos)
        self.niveau.incrementer_nbplace_disponible()
        
        self.assertEqual(self.niveau.nbplace_disponible, 50)
        self.assertEqual(self.niveau.nbplace_occupees, 0)

    def test_decrementer_nbplace_occupees(self):
        """
        V rifie qu'apr s d cr mentation, le nombre de places occup es 
        a diminu  et que le nombre de places disponibles a augment .
        """
        # On part d'une situation o  5 places sont occup es
        self.niveau.nbplace_occupees = 5
        self.niveau.nbplace_disponible = 45
        
        self.niveau.decrementer_nbplace_occupees()
        
        self.assertEqual(self.niveau.nbplace_occupees, 4)
        self.assertEqual(self.niveau.nbplace_disponible, 46)

    def test_incrementer_nbplace_occupees(self):
        """
        V rifie qu'apr s incr mentation, le nombre de places occup es 
        a augment  et que le nombre de places disponibles a diminu .
        """
        # tat initial : 50 disponibles, 0 occup e
        self.niveau.incrementer_nbplace_occupees()
        
        self.assertEqual(self.niveau.nbplace_occupees, 1)
        self.assertEqual(self.niveau.nbplace_disponible, 49)

if __name__ == '__main__':
    unittest.main()