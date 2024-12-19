import unittest
import pydoc

from parking.borne_ticket import BorneTicket


class TestBorneTicket(unittest.TestCase):
    """
        Auteur de cette classe : ASSANE KANE
    """

    def setUp(self):
        """Code pour initialiser les données de test"""
        self.borne1 = BorneTicket(1)

    def tearDown(self):
        """ Code pour nettoyer après le test"""
        self.borne1 = None

    def test_delivrer_ticket(self):
        """
        comparer ticket revoyer à ticket attendu
        """
        pass

    def test_proposer_services(self):
        """
        verifier si service renvoyé egale service attendus
        """
        pass

    def test_proposer_abonnements(self):
        """
        verifier si {abonnements renvoyés} egale {abonnements attendus}
        """
        pass

    def test_recuper_Info_Carte(self):
        """
        vérifier si (info de la carte recuperée) == (info de la carte attendue)
        """
        pass

    def test_proposer_type_paiement(self):
        """
        verifier si modePayement = carte et espece
        """
        res = self.borne1.proposer_type_paiement()
        self.assertEqual(res, "Opération annulée")

    pydoc.writedoc("borne_icket")


if __name__ == '__main__':
    unittest.main()
