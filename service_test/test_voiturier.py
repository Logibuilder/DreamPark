import unittest

class MyTestCase(unittest.TestCase):
    """
    Auteur:Mbonihankuye Ulrich Babbel

    le test_livrer_voiture verifie que la voiture est livrer en compararnt les chaines de caracteres 
    """
    def test_livrer_voiture(self):
        self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
