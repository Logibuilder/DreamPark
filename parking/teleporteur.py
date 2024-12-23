import pydoc
from datetime import date, timedelta

from parking.placement import Placement


class Teleporteur:
    """
        Auteur de cette classe : ASSANE KANE
    """
    def __init__(self, num):
        """
        initialiser le teleporteur avec le num (on a deux teleporteurs au niveau des deux acces)
        """
        self.num = num

    def teleporter_voiture(self, action):
        if action == "garer" :
            print("voiture garée avec succés")
            return Placement(date.today(), date.today() + timedelta(days=1))

        if action == "recuper" :
            print("voiture sortie avec succès")




#pydoc.writedoc("teleporteur")