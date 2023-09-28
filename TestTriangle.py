import unittest
from Triangle import TriangleClassifier

class TestTriangleClassifier(unittest.TestCase):
    def test_equilateral_triangle(self):
        Triangle = TriangleClassifier(5, 5, 5)
        self.assertEqual(triangle.classify_triangle(), "Equilateral")
        print("test_equilateral_triangle is passed")

    def test_isosceles_triangle(self):
        Triangle = TriangleClassifier(5, 5, 8)
        self.assertEqual(triangle.classify_triangle(), "Isosceles")
        print("test_isosceles_triangle is passed")

    def test_scalene_triangle(self):
        Triangle = TriangleClassifier(3, 4, 5)
        self.assertEqual(triangle.classify_triangle(), "Scalene")
        print("test_scalene_triangle is passed")

    def test_right_triangle(self):
        Triangle = TriangleClassifier(3, 4, 5)
        self.assertEqual(triangle.classify_triangle(), "Right")
        print("test_right_triangle is passed")

    def test_invalid_triangle(self):
        Triangle = TriangleClassifier(0, 0, 0)
        self.assertEqual(triangle.classify_triangle(), "Not a valid triangle")

if __name__ == "__main__":
    unittest.main()
    print("Everything is passed")
