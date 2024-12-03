import pydoc
import unittest

class MyTestCase(unittest.TestCase):
    """
        Auteur de cette classe : ASSANE KANE
    """
    def test_capturer_hauteur(self, voiture):
        """
        return la hauteur de la voiture
        """
        return 1.5  # retour float

    def test_capturer_longueur(self, voiture):
        """
        return la longueur de la voiture
        """
        return 1.5  # retour float

    def test_capturer_immatri(self, voiture):
        """
        return l'immatricule  de la voiture
          """
        return ""  # add assertion here




    pydoc.writedoc("test_camera")


if __name__ == '__main__':
    unittest.main()
