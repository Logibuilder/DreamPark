class Voiturier:
    def __init__(self, nom, num_voiturier):
        self.nom = nom
        self.num_voiturier = num_voiturier
    """
        Auteur:Mbonihankuye Ulrich Babbel
        
        attributs:
        nom : Nom du voiturier.
        num_voiturier : Numéro d'identification du voiturier.
    """

    def livrer_voiture(self, voiture, date, heure):
        return "Voiture livrer"