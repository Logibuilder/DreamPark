import  pydoc

class Camera:
    """
        Auteur de cette classe : ASSANE KANE
        """
    def __init__(self):
        pass

    def capturer_hauteur(self, voiture):
        """
        return la hauteur de la voiture
        """
        return 1.5#retour float

    def capturer_longueur(self, voiture):
        """
        return la longueur de la voiture
        """
        return 1.5#retour float

    def capturer_immatri(self, voiture):
        """
        return l'immatricule  de la voiture
          """
        return ""


pydoc.writedoc("camera")