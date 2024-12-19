
class abonnement:
    """

    Classe représentant un abonnement, incluant un libellé, un prix,
    et une indication si l'abonnement est un pack garanti.
    """
    def __init__(self, libelle, prix, est_packGar):
        """
        Initialise un abonnement avec un libellé, un prix et un indicateur
        s'il s'agit d'un pack garanti.

        :param libelle: Le nom ou la description de l'abonnement (type: str).
        :param prix: Le prix de l'abonnement (type: float).
        :param est_packGar: Indique si l'abonnement est un pack garanti (type: bool).
        """
        self.libelle = libelle
        self.prix = prix#float
        self.est_packGar = est_packGar#booleen


    def add_contrat(self, contrat):
        """
        Ajoute un contrat à l'abonnement. Cette méthode est actuellement
        non implémentée et doit être définie selon les besoins spécifiques.

        :param contrat: Un contrat à associer à l'abonnement (type attendu: Contrat ou similaire).
        """
        pass