from time import sleep

from parking.borne_ticket import BorneTicket, Ticket
from parking.camera import Camera
from parking.gestion_parking import Parking
from parking.teleporteur import Teleporteur
from parking.voiture import Voiture
from service.client import Client

instance_parking = Parking()
instance_camera = Camera()
instanceBorneTicket = BorneTicket(1)

instanceTeleporteur = Teleporteur(1)



def seGarerSansAbonne ( voiture, client ):

    hauteur = instance_camera.capturer_hauteur(voiture)
    longueur = instance_camera.capturer_longueur(voiture)

    place  , numplace , nom_niveau = instance_parking.rechercherPlace(hauteur , longueur)
    if place == "null_place" :
        print("Il n y a pas de palce dans lee parkong pour cette voitre")
        return
    if client.estAbonne :
        print("client abonné")
    else :
        print("client non abonné")

    status_payement = instanceBorneTicket.proposer_type_paiement()
    ticket = None
    if status_payement == "Paiement_validé" :

        ticket = Ticket(client , voiture)
        print(f"Ticket généré : {ticket}, Niveau : {nom_niveau}, Place : {place}, Numéro : {numplace}")
        instanceTeleporteur.teleporter_voiture(voiture, "garer" )
    else :
        print("l'opération se garer est annulée, Veiller reprendre une nouvelle fois")




voiture = Voiture(3, 7 , "OUMOU")
client = Client("Assane" , "adresse")

seGarerSansAbonne(voiture, client)


def garrerAvecAbonner( voiture, client ):
    pass