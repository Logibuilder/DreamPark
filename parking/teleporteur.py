import pydoc


class Teleporteur:
    """
        Auteur de cette classe : ASSANE KANE
    """
    def __init__(self, num):
        """
        initialiser le teleporteur avec le num (on a deux teleporteurs au niveau des deux acces)
        """
        self.num = int(num)

    def test_teleporter_voiture(self):
        pass


pydoc.writedoc("teleporteur")