import unittest


class MyTestCase(unittest.TestCase):
    """
    Auteur : Ulrich Babbel Mbonihankuye

    test_effectuer_maintenance: cette methode effectue la maintenance d'une voiture 
    """
    def test_effectuer_maintenance(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
