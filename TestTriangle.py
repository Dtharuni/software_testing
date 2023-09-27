import unittest
from Triangle import classify_triangle

class TestTriangleClassifier(unittest.TestCase):
    def test_equilateral_triangle(self):
        triangle = TriangleClassifier(5, 5, 5)
        self.assertEqual(triangle.classify_triangle(), "Equilateral")
        print("test_equilateral_triangle is passed")

    def test_isosceles_triangle(self):
        triangle = TriangleClassifier(5, 5, 6)
        self.assertEqual(triangle.classify_triangle(), "Isosceles")
        print("test_isosceles_triangle is passed")

    def test_scalene_triangle(self):
        triangle = TriangleClassifier(3, 4, 5)
        self.assertEqual(triangle.classify_triangle(), "Scalene")
        print("test_scalene_triangle is passed")

    def test_right_triangle(self):
        triangle = TriangleClassifier(3, 4, 5)
        self.assertEqual(triangle.classify_triangle(), "Right")
        print("test_right_triangle is passed")

    def test_invalid_triangle(self):
        triangle = TriangleClassifier(1, 2, 3)
        self.assertEqual(triangle.classify_triangle(), "Not a valid triangle")

if __name__ == "__main__":
    print("Everything is passed")
    unittest.main()
