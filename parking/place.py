class Place:
    """

    """
    def __init__(self, numero, niveau, longeur, hauteur):
        self.numero = numero
        self.niveau = niveau
        self.longeur = longeur
        self.hauteur = hauteur
        self.est_libre = True
        self.id = niveau+str(self.numero)


    def set_valeur_libre(self, bool):
        est_libre = bool


    def __add_placement__(self, placement):
        pass




