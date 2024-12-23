import unittest


class MyTestCase(unittest.TestCase):
    """
    Auteur : Ulrich Babbel Mbonihankuye
    on prend une voiture et on effectue son entretient 
    """
    def test_effectuer_entretien(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
