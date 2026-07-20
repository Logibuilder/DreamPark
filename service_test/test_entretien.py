import unittest
import io
from contextlib import redirect_stdout
from service.entretien import Entretien

class TestEntretien(unittest.TestCase):
    """
    Auteur : Ulrich Babbel Mbonihankuye
    On prend une voiture et on effectue son entretien.
    """
    def test_effectuer_entretien(self):
        entretien = Entretien("2026-07-20", "15:00", "Rapport d'entretien")
        
        # Capture de la sortie standard (print)
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            entretien.effectuer_entretien()
            
        self.assertIn("entretien entretien entretien", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()