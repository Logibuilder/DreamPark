import pydoc

from controller.ticket import Ticket
from parking.niveau import Niveau
from parking.place import Place
from service.client import Client


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

class Parking:
    _instance = None  # Stocke l'unique instance de Parking
    def __new__(cls, *args, **kwargs):
    # Si aucune instance n'existe encore, on en crée une nouvelle
        if cls._instance is None:
            cls._instance = super(Parking, cls).__new__(cls)
        return cls._instance
    def __init__(self):
    # Vérifie si l'instance a déjà été initialisée
        if not hasattr(self, "initialized"):
            self.nbPlacesParNiveau = 50
            self.nbPlacesLibre = 250
            self.prix = 30 # Prix en euros
            self.nbNiveau = 4
            # Création des niveaux du parking
            A = Niveau("A", 3, 1.90, 3)
            B = Niveau("B", 3, 2, 4)
            C = Niveau("C", 4, 2.70, 5)
            D = Niveau("D", 4, 3, 7)
            self.lesNiveau = [A, B, C, D]
            self.initialized = True

    def rechercherPlace(self, hauteur , longueur):
        """
        Recherche une place libre dans le parking pour une voiture donnée.

        :param voiture: L'objet voiture pour lequel une place est recherchée.
        :return: Une place disponible ou `None` si aucune place n'est disponible.
        return place  ou une valeur particulière.
        """
        for level in self.lesNiveau:
            place = level.a_place_diponible(hauteur, longueur)
            if place != None:
                return place
        return None  # Si aucune place n'est trouvée , on revoit none

    def libererPlace(self, ticket):
        for level in self.lesNiveau :
            if ticket.place.id[0] == level.nom :

                status = level.libererPlace(ticket)
                print(status)
                return status
        return "not_ok"


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
        res = ""
        for niveau in self.lesNiveau:
            res+= str(niveau)
        res+="\n\n"

        return res


#pydoc.writedoc("parking")


