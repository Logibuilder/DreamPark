import unittest

from parking.voiture import Voiture


import unittest
from parking.voiture import Voiture


class TestAcces(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE
    """

    def setUp(self):
        self.v1 = Voiture(2.5, 5, "IIIIIAAIIIIIII")

    def tearDown(self):
        self.v1 = None

    def test_actionner_camera(self):
        """
        Vérifier que la voiture retournée est la voiture du client.
        """
        self.assertEqual((2.5, 5, "IIIIIAAIIIIIII"), (self.v1.hauteur , self.v1.longueur , self.v1.immatriculation))


if __name__ == '__main__':
    unittest.main()
