import pydoc



class Niveau:
    """

    Auteur de cette classe : ASSANE KANE

    Classe représentant un niveau de parking.
    """
    def __init__(self, nom, nbplace, hauteur, longueur):
        """
        Initialise un niveau avec un nom et un nombre total de places.

        :param nom: Nom ou identifiant du niveau (ex. : "A", "B").
        :param nbplace: Nombre total de places dans le niveau.
        """
        self.hauteur = hauteur
        self.longueur = longueur
        self.nom = nom
        self.nbplace = nbplace
        self.nbplace_disponible = nbplace
        self.nbplace_occupees = 0


    def decrementer_nbplace_disponible(self):
        """
        Diminue le nombre de places disponibles et met à jour les places occupées.
        """
        self.nbplace_disponible -=1
        self.nbplace_occupees +=1


    def incrementer_nbplace_disponible(self):
        """
        Augmente le nombre de places disponibles et met à jour les places occupées.
        """
        self.nbplace_disponible +=1
        self.nbplace_occupees -=1

    def decrementer_nbplace_occupees(self):
        self.nbplace_occupees -=1
        self.nbplace_disponible +=1

    def incrementer_nbplace_occupees(self):
        self.nbplace_occupees +=1
        self.nbplace_disponible -=1

    def get_nbplacedisponible(self):
        """
        Retourne le nombre de places disponibles dans ce niveau.
        """
        return self.nbplace_disponible


    def a_place_diponible(self, H, L):
        if self.nbplace_disponible != 0  and H <= self.hauteur and L <= self.longueur :
            self.nbplace_occupees +=1
            self.nbplace_disponible -=1
            return ( "place", self.nbplace - self.nbplace_disponible )

        else :
            return ("null_place", -1)



    pydoc.writedoc("niveau")


niveau = Niveau("A", 2, 2, 4)
print(niveau.a_place_diponible(2, 1))
print(niveau.nbplace_disponible)