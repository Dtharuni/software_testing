import unittest
from Triangle import TriangleClassifier

class TestTriangleClassifier(unittest.TestCase):
    def test_equilateral_triangle(self):
        triangle = TriangleClassifier(5, 5, 5)
        self.assertEqual(triangle.classify(), "Equilateral")

    def test_isosceles_triangle(self):
        triangle = TriangleClassifier(4, 4, 5)
        self.assertEqual(triangle.classify(), "Isosceles")

    def test_scalene_triangle(self):
        triangle = TriangleClassifier(3, 4, 5)
        self.assertEqual(triangle.classify(), "Scalene")

    def test_right_triangle(self):
        triangle = TriangleClassifier(3, 4, 5)
        self.assertEqual(triangle.classify(), "Right")

if __name__ == "__main__":
    unittest.main()
