from parking.niveau import niveau


class Parking:
    """
    classe singleton
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
        return voiture


    def nb_places_libres_par_niveau(self, niveau):
        """
        return le nombre de places libres par niveau
        """
    
    def nb_places_libres_libre(self, libre):
        """
        <h6>return le nombre de places libres dans tout le parking</h6>
        """
        nb = 0
        for niv  in self.lesNiveau:
            nb += niv.get_nbplacedisponible()

    def add_abonnement(self, abonnement):
        pass





