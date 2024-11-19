from parking import parking


class PanneauAffichage:

    def afficher_nbPlacesDisponibles(self):
        print(parking.get_nbPlacesDisponibles())