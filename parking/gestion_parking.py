import pydoc
from parking.niveau import Niveau
from parking.voiture import Voiture


class Parking:
    """
    Auteur de cette classe : ASSANE KANE

    classe singleton
    Classe représentant un parking géré par niveaux.
    Cette classe est conçue pour être un singleton, bien qu'aucune mécanique spécifique ne soit encore mise en place.

    Attributs de classe :
    ---------------------
    - nbPlacesParNiveau : int
        Nombre de places par niveau dans le parking.
    - nbPlacesLibre : int
        Nombre total de places libres dans tout le parking.
    - prix : float
        Prix du stationnement (en euros).
    - nbNiveau : int
        Nombre total de niveaux dans le parking.
    - lesNiveau : list
        Liste des niveaux disponibles dans le parking, initialisée avec des objets de type `niveau`.
    """
    def __init__(self):
        self.nbPlacesParNiveau = 50
        self.nbPlacesLibre = 250
        self.prix = 30#euro
        self.nbNiveau = 4
        A = Niveau("A", 3 , 1.90, 3)
        B = Niveau("B", 3 , 2 , 4 )
        C = Niveau("C", 4 , 2.70 , 5)
        D = Niveau("D", 4 , 3 , 7)
        self.lesNiveau = [A, B, C, D]

    def rechercherPlace(self, hauteur , longueur):
        """
        Recherche une place libre dans le parking pour une voiture donnée.

        :param voiture: L'objet voiture pour lequel une place est recherchée.
        :return: Une place disponible ou `None` si aucune place n'est disponible.
        return place  ou une valeur particulière.
        """
        for level in self.lesNiveau:
            val_particuliere, numplace, nom_niveau = level.a_place_diponible(hauteur, longueur)
            if val_particuliere == "place":
                return val_particuliere, numplace, nom_niveau
        return "null_place", -1, "null_niveau"  # Si aucune place n'est trouvée




    def nb_places_libres_par_niveau(self, niveau):
        """
        return le nombre de places libres par niveau
        """
        return 0
    
    def nb_places_libres_libre(self):
        """
        <h6>return le nombre de places libres dans tout le parking</h6>
        """
        nb = 0
        for niv  in self.lesNiveau:
            nb += niv.get_nbplacedisponible()

        return nb

    def add_abonnement(self, abonnement):
        """
        Ajoute un abonnement au système de gestion du parking.
        La logique d'ajout et de gestion des abonnements doit être développée ici.

        :param abonnement: L'objet abonnement à ajouter.
        """
        pass

    def afficherCurrentSituation(self):
        for niveau in self.lesNiveau:
            niveau.afficherCurrentSituation()


    def __str__(self):
        for niveau in self.lesNiveau:
            print(niveau)
        print("\n\n\n")


#pydoc.writedoc("parking")

