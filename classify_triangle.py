import unittest

class TriangleClassifier:
    def classify_triangle(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return "Invalid"
        elif a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            return "Right"
        else:
            return "Scalene"

class TestTriangleClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = TriangleClassifier()

    def test_equilateral(self):
        self.assertEqual(self.classifier.classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(self.classifier.classify_triangle(3, 4, 3), "Isosceles")
        self.assertEqual(self.classifier.classify_triangle(4, 3, 3), "Isosceles")
        self.assertEqual(self.classifier.classify_triangle(3, 3, 4), "Isosceles")

    def test_scalene(self):
        self.assertEqual(self.classifier.classify_triangle(3, 4, 6), "Scalene")
        self.assertEqual(self.classifier.classify_triangle(5, 7, 8), "Scalene")

    def test_right(self):
        self.assertEqual(self.classifier.classify_triangle(3, 4, 5), "Right")
        self.assertEqual(self.classifier.classify_triangle(5, 12, 13), "Right")
        self.assertEqual(self.classifier.classify_triangle(8, 15, 17), "Right")

    def test_invalid(self):
        self.assertEqual(self.classifier.classify_triangle(0, 1, 2), "Invalid")
        self.assertEqual(self.classifier.classify_triangle(-1, 2, 3), "Invalid")

if __name__ == "__main__":
    unittest.main()
