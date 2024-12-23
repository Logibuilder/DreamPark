import parking
from parking.gestion_parking import Parking


class PanneauAffichage:
    _instance = None  # Attribut de classe pour stocker l'instance unique

    def __new__(cls, *args, **kwargs):
        # Si aucune instance n'a encore été créée, on en crée une
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialisation de l'instance, si nécessaire
        # On peut ajouter des attributs ici si besoin
        self.nom = "Panneau"

    def afficherPaneau(self):
        print( Parking())



