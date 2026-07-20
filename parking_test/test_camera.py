import unittest
from parking.camera import Camera
from parking.voiture import Voiture

class TestCamera(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE
    """
    def setUp(self):
        self.camera = Camera(1)
        self.voiture = Voiture(1.5, 4.0, "AB-123-CD")

    def test_capturer_hauteur(self):
        """V rifie que la cam ra retourne bien la hauteur."""
        self.assertEqual(self.camera.capturer_hauteur(self.voiture), 1.5)

    def test_capturer_longueur(self):
        """V rifie que la cam ra retourne bien la longueur."""
        self.assertEqual(self.camera.capturer_longueur(self.voiture), 4.0)

    def test_capturer_immatri(self):
        """V rifie que la cam ra retourne bien l'immatriculation."""
        self.assertEqual(self.camera.capturer_immatri(self.voiture), "AB-123-CD")

if __name__ == '__main__':
    unittest.main()