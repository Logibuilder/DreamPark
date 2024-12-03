import pydoc
import unittest


class testParking(unittest.TestCase):
    """
        Auteur de cette classe : ASSANE KANE
    """
    '''à l'initialisation
        tes1 = verifier que nbplacesParNiveau * nbNiveau == nbPlacesDisponibles)

    '''

    def rechercher_place(self, voiture):
        """
            on doit vérifier que la méthode retourne bien une place quand c'est disponibre ou une valeur particulière sinon
        """

    def test_nb_places_libres_par_niveau(self, niveau):
        """
        vérifier que la fonction retourne le nombre de place disponible par niveau
        """
        return 0

    def test_nb_places_libres_libre(self):
        """
        vérifier que la fonction retourne le nombre de place disponible dans tous le parking
        """

    def test_add_abonnement(self, abonnement):
        """
        vérifier l'abonnement ajouté est bien dans la liste des abonnements
        """
        pass



    pydoc.writedoc("test_parking")


if __name__ == '__main__':
    unittest.main()