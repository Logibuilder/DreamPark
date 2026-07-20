import unittest
import io
from contextlib import redirect_stdout
from service.livraison import Livraison

class TestLivraison(unittest.TestCase):
    """
    Auteur : Ulrich Babbel Mbonihankuye
    Suite a la demande d'un client le voiturier doit livrer sa voiture.
    """
    def test_effectuer_livraison(self):
        livraison = Livraison("2026-07-20", "14:00", "Rapport de livraison")
        
        # Capture de la sortie standard (print)
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            livraison.effectuer_livraison()
            
        self.assertIn("livraison livraison livraison", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()