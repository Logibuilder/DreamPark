import pydoc
import unittest


class MyTestCase(unittest.TestCase):
    """
        Auteur de cette classe : ASSANE KANE
    """
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    pydoc.writedoc("test_placement")
if __name__ == '__main__':
    unittest.main()
