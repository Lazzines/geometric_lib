import unittest
import math
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_3_4_5(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0, places=5)

    def test_area_5_5_5(self):
        self.assertAlmostEqual(area(5, 5, 5), 10.8253, places=4)

    def test_perimeter_3_4_5(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_5_5_5(self):
        self.assertEqual(perimeter(5, 5, 5), 15)