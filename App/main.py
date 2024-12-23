from controller.recuperer_voiture import recuperer_voiture
from controller.se__garer import seGarerSansAbonne
from controller.ticket import Ticket
from parking import teleporteur
from parking.voiture import Voiture
from service.client import Client
from parking.acces import Acces

acces = Acces("Accès Principal")

if __name__ == "__main__":
    while True:
        print("\n=== Bienvenue dans le système de gestion des clients ===")
        print("1. Inscrivez-vous comme nouveau client")
        print("2. Consultez la liste des clients")
        print("3. Garez une voiture")
        print("4. Récupérez une voiture")
        print("5. Voir les tickets")
        print("6. Quittez le programme")
        print("7. Ajouter ou changer de voiture pour un client")

        choix = input("Que souhaitez-vous faire ? (1-7) : ")

        if choix == "1":
            Client.inscrire_client()
        elif choix == "2":
            Client.afficher_clients()
        elif choix == "3":
            nom_client = input("Entrez le nom du client : ")
            client = Client.rechercher_client_par_nom(nom_client)
            if client:
                if client.myCar is None:  # Vérification si le client a une voiture
                    print(f"{client.nom}, vous n'avez pas de voiture enregistrée.")
                    ajouter_voiture = input(
                        "Souhaitez-vous ajouter une voiture maintenant ? (oui/non) : ").strip().lower()
                    if ajouter_voiture == "oui":
                        print(f"=== Ajout d'une voiture pour {client.nom} ===")
                        hauteur = float(input("Entrez la hauteur de votre voiture (en mètres) : "))
                        longueur = float(input("Entrez la longueur de votre voiture (en mètres) : "))
                        immatriculation = input("Entrez l'immatriculation de votre voiture : ")
                        client.myCar = Voiture(hauteur, longueur, immatriculation)
                        print(f"La voiture a été ajoutée avec succès pour {client.nom}.")
                    else:
                        print("Vous pouvez ajouter une voiture plus tard.")
                else:
                    seGarerSansAbonne(acces, client)  # Si le client a une voiture, procéder au stationnement
            else:
                print(f"Aucun client trouvé avec le nom {nom_client}.")
        elif choix == "4":
            num_tkt = input("Entrez le numéro du ticket : ")
            ticket = Ticket.findByNum(int(num_tkt))
            if ticket:
                recuperer_voiture(acces, ticket, teleporteur)
            else:
                print(f"Aucun ticket trouvé avec le numéro {num_tkt}.")
        elif choix == "5":
            Ticket.afficher_tous_les_tickets()  # Nouvelle option pour afficher tous les tickets
        elif choix == "6":
            print("Merci d'avoir utilisé le système de communication de DreamPark. À bientôt !")
            break
        elif choix == "7":
            nom_client = input("Entrez le nom du client : ")
            client = Client.rechercher_client_par_nom(nom_client)
            if client:
                print(f"{client.nom}, que souhaitez-vous faire ?")
                if client.myCar:
                    print(
                        f"Votre voiture actuelle : Hauteur={client.myCar.hauteur}m, Longueur={client.myCar.longueur}m, Immatriculation={client.myCar.immatriculation}")
                else:
                    print("Vous n'avez pas encore enregistré de voiture.")

                confirmation = input("Souhaitez-vous ajouter ou remplacer la voiture ? (oui/non) : ").strip().lower()
                if confirmation == "oui":
                    print(f"=== Ajout d'une nouvelle voiture pour {client.nom} ===")
                    hauteur = float(input("Entrez la hauteur de la voiture (en mètres) : "))
                    longueur = float(input("Entrez la longueur de la voiture (en mètres) : "))
                    immatriculation = input("Entrez l'immatriculation de la voiture : ")
                    client.myCar = Voiture(hauteur, longueur, immatriculation)  # Remplace l'ancienne voiture
                    print(f"La nouvelle voiture a été enregistrée avec succès pour {client.nom}.")
                else:
                    print("Aucune modification effectuée.")
            else:
                print(f"Aucun client trouvé avec le nom {nom_client}.")
        else:
            print("Choix invalide. Veuillez réessayer.\n")
