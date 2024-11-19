class niveau:
    def __init__(self, nom, nbplace):
        self.nom = nom
        self.nbplace = nbplace
        self.nbplace_disponible = nbplace
        self.nbplace_occupees = 0


    def decrementer_nbplace_disponible(self):
        self.nbplace_disponible -=1


    def incrementer_nbplace_disponible(self):
        self.nbplace_disponible +=1

    def decrementer_nbplace_occupees(self):
        self.nbplace_occupees -=1

    def incrementer_nbplace_occupees(self):
        self.nbplace_occupees +=1

    def get_nbplacedisponible(self):
        return self.nbplace_disponible