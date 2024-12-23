from controller.ticket import Ticket
from interface.panneau_affichage import PanneauAffichage
from parking import voiture as v
import pydoc
from parking.camera import Camera

from parking.gestion_parking import Parking

from parking.borne_ticket import BorneTicket

from parking.teleporteur import Teleporteur


panneau = PanneauAffichage()

class Acces:
    """
    Auteur de cette classe : ASSANE KANE
    """
    def __init__(self , nom):
        """
        initialiser la classe acces avec son nom
        """
        self.nom = nom


    def presenterTicket(self, ticket):
        return ticket


    def actionner_camera(self, client):
        """
            parametre: client
            retourne la voiture d'un client
        """

    def direBonjour(self, client):
        print(f"Bonjour {client.nom}, bienvenue chez DreamPark !")

    def actionner_panneau(self , panneau):
        """
        afficher les information mises à jour du parking(places disponibles)
        """
        panneau.afficherPaneau()



    def lancer_procedure_entree(self, client):
        """appelle la methode teleporter() de teleporteur"""
        instanceBorneTicket = BorneTicket(1)
        instanceTeleporteur = Teleporteur(1)

        camera = Camera(1)
        hauteur = camera.capturer_hauteur(client.myCar)

        longueur = camera.capturer_longueur(client.myCar)

        place =  Parking().rechercherPlace(hauteur, longueur)
        if place == None:

            print("Il n y a pas de palce dans lee parking pour cette voitre")
            return
        else:
            payment = instanceBorneTicket.proposer_type_paiement()
            ticket = Ticket(client, place , payment)

            print(ticket)
            instanceTeleporteur.teleporter_voiture("garer")

            self.actionner_panneau(panneau)

    def lancer_procedure_sortie(self, ticket ,  tlptr):
        instanceBorneTicket = BorneTicket(1)
        instanceTeleporteur = Teleporteur(1)

        instanceTeleporteur.teleporter_voiture("recuper")

        service, info = instanceBorneTicket.proposer_services()

        if service == "livraison":
            adresse = info.get("adresse")
            heure = info.get("heure")
            print(f"Votre voiture sera livrée à l'adresse : {adresse} à {heure}.")
            # Ajouter ici la logique de livraison (système de réservation ou d'affectation de voiturier)
            self.informerParking(ticket)
        elif service == "entretien":
            print("Votre voiture sera dirigée vers le service d'entretien.")
            # Ajouter ici la logique pour diriger la voiture au service d'entretien
            self.informerParking(ticket)
        elif service == "maintenance":
            print("Votre voiture sera dirigée vers le service de maintenance.")
            # Ajouter ici la logique pour diriger la voiture au service de maintenance

            self.informerParking(ticket)
        elif service == "annuler":
            instanceTeleporteur.teleporter_voiture("garer")
        else:
            print("Erreur : Service non reconnu.")

        # Libérer la place et mettre à jour le panneau d'affichage
        self.informerParking(ticket)

    def informerParking(self, ticket):
        parking = Parking()
        parking.libererPlace(ticket)

#pydoc.writedoc("acces")

