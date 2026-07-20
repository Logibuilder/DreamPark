import unittest
from unittest.mock import patch
from parking.borne_ticket import BorneTicket

class TestBorneTicket(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE
    """

    def setUp(self):
        """Code pour initialiser les données de test"""
        self.borne1 = BorneTicket(1)

    def tearDown(self):
        """Code pour nettoyer après le test"""
        self.borne1 = None

    @patch('builtins.input', side_effect=['1', '30'])  # Simuler un paiement valide (espèces)
    def test_proposer_type_paiement_valide(self, mock_input):
        """Test avec un choix valide et une somme correcte"""
        res = self.borne1.proposer_type_paiement()
        self.assertEqual(res, "Paiement valid ")



if __name__ == '__main__':
    unittest.main()
