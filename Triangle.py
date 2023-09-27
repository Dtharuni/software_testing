import unittest
import math
import datetime

def my_brand(hw_name):
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    screen_brand = f"=*=*=*= Tharuni D =*=*=*=\n\n" \
                  f"=*=*=*= Course 2023S-SSW567-WS =*=*=*=\n\n" \
                  f"=*=*=*= {hw_name} =*=*=*=\n\n" \
                  f"=*=*=*= {current_datetime} =*=*=*=\n"
    
    print(screen_brand)

my_brand("HW 00")

class TriangleClassifier:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def classify_triangle(self):
        if self.is_equilateral():
            return "Equilateral"
        elif self.is_isosceles():
            return "Isosceles"
        elif self.is_scalene():
            return "Scalene"
        elif self.is_right():
            return "Right"
        else:
            return "Not a valid triangle"
    
    def is_equilateral(self):
        return self.side_a == self.side_b == self.side_c

    def is_isosceles(self):
        return (
            self.side_a == self.side_b
            or self.side_a == self.side_c
            or self.side_b == self.side_c
        )

    def is_scalene(self):
        return not self.is_equilateral() and not self.is_isosceles()

    def is_right(self):
        sides = [self.side_a, self.side_b, self.side_c]
        sides.sort()
        a, b, c = sides
        return math.isclose(a ** 2 + b ** 2, c ** 2, rel_tol=1e-9)