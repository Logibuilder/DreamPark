# import pydoc
import unittest
from Parking.ticket import Ticket
from Parking.voiture import Voiture
from service.client import Client
from Parking.borne_ticket import BorneTicket


class TestBorneTicket(unittest.TestCase):
    """
        Auteur de cette classe : ASSANE KANE
    """

    def setUp(self):
        """Code pour initialiser les données de test"""
        self.borne= BorneTicket(1)#initialisation de la borne
        self.client= Client("Babbel",31200)
        self.voiture= Voiture(1.5,4.2,"123-ABC")
        self.valid_ticket = self.borne.delivrer_ticket(self.client, self.voiture)


    def tearDown(self):
        """ Code pour nettoyer après le test"""
        pass

    def test_delivrer_ticket(self):
        """
        comparer ticket revoyer à ticket attendu
        """
        """creation d'une borne"""
        self.borne= BorneTicket(1)

        """Creation d'un client et d'une voiture"""
        self.client= Client("Babbel",31200)
        self.voiture= Voiture(1.5,4.2,"123-ABC")
        self.Ticket= Ticket(self.client, self.voiture)
        """Génération d'un ticket"""
        self.Ticket.creationTicket()

        self.assertEqual(self.Ticket.creationTicket(),"T-Babbel-123-ABC")

        # """affichage des tickets se trouvant dans la liste"""
        # self.borne.afficher_liste_ticket()

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
        pass

#     import io
# import sys

def test_presenter_ticket_valide(self,ticket):
        """
        Vérifie qu'un ticket valide est reconnu par la borne.
        """
        res= self.borne.presenter_ticket(ticket)
        self.assertTrue(res,"Le ticket devrait être accepté")
        

# pydoc.writedoc("borne_icket")


if __name__ == '__main__':
    unittest.main()
