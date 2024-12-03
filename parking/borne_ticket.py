import pydoc
class borneTicket:
    """
    Auteur de cette classe : ASSANE KANE
    """

    def __init__(self, ticket_no):
        '''

        '''
        pass
    def delivrer_ticket(self, client):
        """
            parametre: client
            return / ticket (string)
        """
        return ""

    def proposer_services(self):
        """
        proposer les different types de service au client
        return : { choix }
        """
        return ""

    def prooser_abonnements(self, client, parking):
        """
            proposer les different types d'abonnements au client
            return : { choix }
        """
        return ""

    def recuper_Info_Carte(self, client):
        """
        recupere les info de la carte du client au debut du processus SE GARER
        """
        pass

    def proposer_type_paiement(self):
        """
        input("choisir mode de payement {carte, espece")
        """
        pass


pydoc.writedoc("borne_icket")
