class Service:

    """
    Auteur:Mbonihankuye Ulrich Babbel
    
    Attributs :
    date_demande : identifie la date de la demande de service.
    date_service : identifie la date à laquelle le service sera réalisé.
    raport :identifie le rapport ou description du service effectué.
    """

    def __init__(self, date_demande, date_service, raport):
        self.date_demande = date_demande
        self.date_service = date_service
        self.raport = raport
