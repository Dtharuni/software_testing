import unittest
from Triangle import TriangleClassifier

class TestTriangleClassifier(unittest.TestCase):
    def test_equilateral_triangle(self):
        triangle = TriangleClassifier(5, 5, 5)
        self.assertEqual(triangle.classify_triangle(), "Equilateral")
        print("test_equilateral_triangle is passed")

    def test_isosceles_triangle(self):
        triangle = TriangleClassifier(3, 3, 4)
        self.assertEqual(triangle.classify_triangle(), "Isosceles")
        print("test_isosceles_triangle is passed")

    def test_scalene_triangle(self):
        triangle = TriangleClassifier(3, 4, 5)
        self.assertEqual(triangle.classify_triangle(), "Scalene")
        print("test_scalene_triangle is passed")

    def test_right_triangle(self):
        triangle = TriangleClassifier(7, 8, 9)
        self.assertEqual(triangle.classify_triangle(), "Right")
        print("test_right_triangle is passed")

    def test_invalid_triangle(self):
        triangle = TriangleClassifier(0, 1, 2)
        self.assertEqual(triangle.classify_triangle(), "Not a valid triangle")

if __name__ == "__main__":
    unittest.main()
    print("Everything is passed")
