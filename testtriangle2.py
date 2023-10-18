""" testing triangle """
import unittest
from triangle import TriangleClassifier

class TestTriangleClassifier(unittest.TestCase):
    """ class for testing triangle classifier """
    def setUp(self):
        """ Definition to setup """
        self.classifier = TriangleClassifier()

    def test_equilateral_triangle(self):
        """ Definition for equilateral triangle """
        self.assertEqual(self.classifier.classify_triangle(5, 5, 5), "Equilateral")
        self.assertEqual(self.classifier.classify_triangle(10, 10, 10), "Equilateral")

    def test_isosceles_triangle(self):
        """ Definition for Isosceles triangle """
        self.assertEqual(self.classifier.classify_triangle(4, 4, 6), "Isosceles")
        self.assertEqual(self.classifier.classify_triangle(7, 5, 7), "Isosceles")
        self.assertEqual(self.classifier.classify_triangle(3, 4, 3), "Isosceles")

    def test_scalene_triangle(self):
        """ Definition for Scalene triangle """
        self.assertEqual(self.classifier.classify_triangle(7, 9, 12), "Scalene")

    def test_right_triangle(self):
        """ Definition for Right triangle """
        self.assertEqual(self.classifier.classify_triangle(3, 4, 5), "Right")
        self.assertEqual(self.classifier.classify_triangle(5, 12, 13), "Right")
        self.assertEqual(self.classifier.classify_triangle(8, 15, 17), "Right")

    def test_invalid_triangle(self):
        """ Definition for InvalidInput triangle """
        self.assertEqual(self.classifier.classify_triangle(0, 1, 2), "InvalidInput")
        self.assertEqual(self.classifier.classify_triangle(-1, 2, 3), "InvalidInput")

if __name__ == "__main__":
    unittest.main()
