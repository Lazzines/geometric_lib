import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_rectangle(self):
        res = area(3, 7)
        self.assertEqual(res, 21)

    def test_area_negative(self):
        res = area(-5, 4)
        self.assertEqual(res, -20)

    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_rectangle(self):
        res = perimeter(3, 7)
        self.assertEqual(res, 20)

    def test_perimeter_negative(self):
        res = perimeter(-5, 4)
        self.assertEqual(res, -2)


