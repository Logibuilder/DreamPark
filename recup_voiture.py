#import unittest
from Parking.voiture import Voiture
from service.client import Client
from Parking.borne_ticket import BorneTicket

def main():
    borne = BorneTicket(1)

    client1= Client("Babbel",123456)
    voiture1= Voiture(0,0,"ABC-123")
    ticket1= borne.delivrer_ticket(client1,voiture1)

    client2= Client("Ulrich",456577)
    voiture2=Voiture(9,8,"DEF-456")
    ticket2= borne.delivrer_ticket(client2,voiture2)

    borne.afficher_liste_ticket()
    print("\n")

    print("-----Récuperation des voitures dans le parking-----\n")
    print(f"\nClient 1 présente son ticket à la borne : {borne.num} , avec le ticket numéro : {ticket1}")
    if borne.presenter_ticket(ticket1):
        print(f"La voiture de {client1.nom} est récupérée avec succès !")
    else: 
        print(f"Erreur : Ticket de {client1.nom} invalide.")
    


    print(f"\nClient 2 présente son ticket a la borne : {ticket2}")
    if borne.presenter_ticket(ticket2): 
        print(f"La voiture de {client2.nom} est récupérée avec succès !")
    else : 
        "Ticket invalide"

    borne.afficher_liste_ticket()




if __name__ == "__main__":
    main()


