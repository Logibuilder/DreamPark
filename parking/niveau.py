import pydoc

from parking.place import Place
from parking.voiture import Voiture


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
        self.listePlace = [Place(place, nom, longueur, hauteur) for place in range(self.nbplace)]

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
        if self.nbplace_disponible > 0:
            if H <= self.hauteur and L <= self.longueur:
                self.nbplace_occupees += 1
                self.nbplace_disponible -= 1
                return "place", self.nbplace_occupees, self.nom
            else:
                return "null_place", -1, "null_niveau"  # Si la taille de la voiture ne correspond pas
        else:
            return "null_place", -1, "null_niveau"  # Si aucune place disponible

    def afficherCurrentSituation(self):
        print(f"//////////////////////////niveau {self.nom}//////////////////////////////")
        for i in range(1, self.nbplace+1):
            if i <= self.nbplace_occupees :
                print("🚗", end="" )
            else :
                print("🚙", end="")
            if i %5 == 0 :
                print("")
        print(f"Le nombre de paces disponible dans le niveau {self.nom} est {self.nbplace_disponible}\n")
        print(f"Le nombre de paces occupées dans le niveau {self.nom} est {self.nbplace_occupees}\n")
        print(f"Le nombre de paces totales dans le niveau {self.nom} est {self.nbplace}\n")
        print("////////////////////////////////////////////////////////////////////////")

    def  __str__(self):
        res = ""
        for place in self.listePlace:
            res+=f"\033[94m||| \033[0m"
            res+=place.__str__() + " "
        return res


    #pydoc.writedoc("niveau")


A = Niveau("A", 3 , 1.90, 3)

voiture1 = Voiture(1.90, 4 , "OUMOU")

voiture2 = Voiture(1.90, 2, "OUMOU")


print(A)
