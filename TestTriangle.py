import unittest
from Triangle import TriangleClassifier

class TestTriangleClassifier(unittest.TestCase):
    def test_equilateral_triangle(self):
        triangle = TriangleClassifier(5, 5, 5)
        self.assertEqual(triangle.classify_triangle(), "Equilateral")

    def test_isosceles_triangle(self):
        triangle = TriangleClassifier(8, 6, 8)
        self.assertEqual(triangle.classify_triangle(), "Isosceles")

    def test_scalene_triangle(self):
        triangle = TriangleClassifier(7, 9, 11)
        self.assertEqual(triangle.classify_triangle(), "Scalene")

    def test_right_triangle(self):
        triangle = TriangleClassifier(6, 8, 10)
        self.assertEqual(triangle.classify_triangle(), "Right")

    def test_invalid_triangle(self):
        triangle = TriangleClassifier(-1, 2, 3)
        self.assertEqual(triangle.classify_triangle(), "Not a valid triangle")

if __name__ == "__main__":
    unittest.main()
