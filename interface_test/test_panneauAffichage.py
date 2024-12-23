import unittest
from unittest.mock import patch

from interface.panneau_affichage import PanneauAffichage
from parking.gestion_parking import Parking


class TestPanneauAffichage(unittest.TestCase):

    @patch("builtins.print")
    def test_afficher_panneau(self, mock_print):
        """
        Teste que la méthode afficherPaneau appelle la fonction print.
        """
        panneau = PanneauAffichage()

        # Appeler la méthode afficherPaneau
        panneau.afficherPaneau()

        # Vérifier que print a été appelé
        mock_print.assert_called()


if __name__ == "__main__":
    unittest.main()
