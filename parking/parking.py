import pydoc
from parking import place
from parking.niveau import niveau


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
    nbPlacesParNiveau = 50
    nbPlacesLibre = 250
    prix = 30#euro
    nbNiveau = 4
    A = niveau("A", 50)
    B = niveau("B", 50)
    C = niveau("C", 50)
    D = niveau("D", 50)

    lesNiveau = [A, B, C, D]

    def rechercher_place(self, voiture):
        """
        Recherche une place libre dans le parking pour une voiture donnée.

        :param voiture: L'objet voiture pour lequel une place est recherchée.
        :return: Une place disponible ou `None` si aucune place n'est disponible.
        return place  ou une valeur particulière.
        """

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


pydoc.writedoc("parking")


