from datetime import date, timedelta
from Parking.placement import Placement
from Parking.ticket import Ticket
from Parking.borne_ticket import BorneTicket


class Teleporteur:
    """
    Classe permettant de gérer la téléportation des voitures à leur emplacement ou à leur client.
    """

    def __init__(self, num):
        """
        Initialise le téléporteur avec un numéro (identifiant).
        """
        self.num = num

    def teleporter_voiture(self, ticket: Ticket, action):
        """
        Téléporte une voiture en fonction de l'action spécifiée.
        :param ticket: Ticket unique pour identifier la voiture.
        :param action: Action à effectuer, soit "garer" soit "recuper".
        :return: Un objet Placement pour "garer" ou un message de confirmation pour "recuper".
        """
        if action == "garer":
            print(f"Voiture avec le ticket {ticket} garée avec succès.")
            # Créer un objet Placement pour indiquer l'endroit et le temps de parking
            placement = Placement(date.today(), date.today() + timedelta(days=1))
            return placement

        elif action == "recuper":
            print(f"Voiture avec le ticket {ticket} récupérée avec succès.")
            return f"Voiture associée au ticket {ticket} récupérée."

        else:
            raise ValueError("Action invalide. Utilisez 'garer' ou 'recuper'.")
