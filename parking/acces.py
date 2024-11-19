from parking import voiture as v


class Acces:
    def __init__(self):
        pass


    def actionner_camera(self, client):
        return v.Voiture(1,1,"exemple_voiture")


    def actionner_panneau(self):
        return ""

    def lancer_procedure_entree(self, client):
        return ""