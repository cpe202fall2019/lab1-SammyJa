import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr_1(self):
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")
    def test_repr_2(self):
        loc = Location("Area 51", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('Area 51', 35.3, -120.7)")

if __name__ == "__main__":
        unittest.main()
