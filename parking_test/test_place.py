import unittest
import pydoc

class MyTestCase(unittest.TestCase):
    """
        Auteur de cette classe : ASSANE KANE
    """
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    pydoc.writedoc("test_place")
if __name__ == '__main__':
    unittest.main()
