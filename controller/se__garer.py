from interface.panneau_affichage import PanneauAffichage
from parking.acces import panneau


def seGarerSansAbonne( acces , client ):
    panneau = PanneauAffichage()

    client.entrer_parking(acces)

    acces.lancer_procedure_entree(client)

    acces.actionner_panneau(panneau)

