import unittest
from Triangle import TriangleClassifier

class TriangleClassifier:
    def classify_triangle(self, a, b, c):
        # Your triangle classification logic here
        pass

class TestTriangleClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = TriangleClassifier()

    def test_equilateral_triangle(self):
        self.assertEqual(self.classifier.classify_triangle(5, 5, 5), "Equilateral")
        self.assertEqual(self.classifier.classify_triangle(10, 10, 10), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(self.classifier.classify_triangle(4, 4, 6), "Isosceles")
        self.assertEqual(self.classifier.classify_triangle(7, 5, 7), "Isosceles")
        self.assertEqual(self.classifier.classify_triangle(3, 4, 3), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(self.classifier.classify_triangle(3, 4, 5), "Scalene")
        self.assertEqual(self.classifier.classify_triangle(7, 9, 12), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(self.classifier.classify_triangle(3, 4, 5), "Right")
        self.assertEqual(self.classifier.classify_triangle(5, 12, 13), "Right")
        self.assertEqual(self.classifier.classify_triangle(8, 15, 17), "Right")

    def test_invalid_triangle(self):
        self.assertEqual(self.classifier.classify_triangle(0, 1, 2), "Invalid")
        self.assertEqual(self.classifier.classify_triangle(-1, 2, 3), "Invalid")
        self.assertEqual(self.classifier.classify_triangle(1, 1, 2), "Invalid")


if __name__ == "__main__":
    unittest.main()
