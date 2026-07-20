import unittest
from service.maintenance import Maintenance
from parking.voiture import Voiture

class TestMaintenance(unittest.TestCase):
    """
    Auteur : Ulrich Babbel Mbonihankuye
    cette methode effectue la maintenance d'une voiture.
    """
    def test_effectuer_maintenance(self):
        maintenance = Maintenance("2026-07-20", "16:00", "Rapport de maintenance")
        voiture_test = Voiture(1.5, 4.2, "AB-123-CD")
        
        # On v rifie simplement que la m thode s'ex cute sans erreur
        try:
            maintenance.effectuer_maintenance(voiture_test)
            execution_reussie = True
        except Exception:
            execution_reussie = False
            
        self.assertTrue(execution_reussie)

if __name__ == '__main__':
    unittest.main()