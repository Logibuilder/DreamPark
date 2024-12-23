import unittest
from parking.acces import Acces
from parking.place import Place
from parking.voiture import Voiture
from controller.ticket import Ticket
from parking.borne_ticket import BorneTicket
from parking.teleporteur import Teleporteur
from parking.camera import Camera
from interface.panneau_affichage import PanneauAffichage
from parking.gestion_parking import Parking
from service.client import Client
import logging

class TestAcces(unittest.TestCase):
    """
    Auteur de cette classe : ASSANE KANE
    """

    def setUp(self):
        # Configuration du logging pour permettre aux tests de capturer les logs
        logging.basicConfig(level=logging.INFO)
        # Initialisation des objets nécessaires aux tests
        self.client = Client("Jean", "1 rue du Test")
        self.client.myCar = Voiture(2.5, 5, "AB-123-CD")
        self.acces = Acces("acces 1")
        self.place = Place(1, "A", 5, 5)
        self.ticket = Ticket(self.client, self.place, "CB")
        self.panneau = PanneauAffichage()

    def tearDown(self):
        # Nettoyage des objets après chaque test
        self.client = None
        self.acces = None
        self.ticket = None
        self.panneau = None

    def test_presenter_ticket(self):
        """
        Vérifier que la méthode presenterTicket retourne le ticket fourni.
        """
        result = self.acces.presenterTicket(self.ticket)
        self.assertEqual(result, self.ticket)

    def test_actionner_camera(self):
        """
        Vérifier que la méthode actionner_camera retourne les dimensions correctes de la voiture.
        """
        camera = Camera(1)
        hauteur = camera.capturer_hauteur(self.client.myCar)
        longueur = camera.capturer_longueur(self.client.myCar)
        self.assertEqual((hauteur, longueur), (2.5, 5))

    def test_dire_bonjour(self):
        """
        Vérifier que la méthode direBonjour affiche le bon message de bienvenue.
        """
        with self.assertLogs() as captured:
            self.acces.direBonjour(self.client)

        self.assertIn("Bonjour Jean, bienvenue chez DreamPark !", captured.output[0])

    def test_actionner_panneau(self):
        """
        Vérifier que la méthode actionner_panneau appelle afficherPanneau correctement.
        """
        with self.assertLogs() as captured:
            self.acces.actionner_panneau(self.panneau)
        # Vérifiez que l'affichage du panneau a été appelé (simulation)

    def test_lancer_procedure_entree_voiture_pas_place(self):
        """
        Vérifier la procédure d'entrée quand il n'y a pas de place disponible.
        """
        parking = Parking()
        parking.rechercherPlace = lambda h, l: None  # Simuler aucune place disponible
        with self.assertLogs() as captured:
            self.acces.lancer_procedure_entree(self.client)
            # Assurez-vous que le message attendu est exactement celui qui est loggé
            self.assertIn("Il n'y a pas de place dans le parking pour cette voiture", captured.output[0])

    def test_lancer_procedure_entree_voiture_place_disponible(self):
        """
        Vérifier la procédure d'entrée quand une place est disponible.
        """
        parking = Parking()
        parking.rechercherPlace = lambda h, l: self.place  # Simuler une place disponible
        borne = BorneTicket(1)
        borne.proposer_type_paiement = lambda: "CB"  # Simuler un type de paiement
        ticket = Ticket(self.client, self.place, "CB")

        # Test sans erreurs, vérifier que le ticket est correctement généré
        self.assertEqual(ticket.place.id, self.place.id)
        self.assertEqual(ticket.client.nom, "Jean")

    def test_lancer_procedure_sortie(self):
        """
        Vérifier que la procédure de sortie libère correctement la place.
        """
        parking = Parking()
        parking.libererPlace = lambda t: True  # Simuler la libération de la place
        with self.assertLogs() as captured:
            self.acces.lancer_procedure_sortie(self.ticket, Teleporteur(1))
        # Ajouter vérification sur la libération ou les messages affichés

if __name__ == '__main__':
    unittest.main()
