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
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def classify(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "Invalid"
        elif self.is_equilateral():
            return "Equilateral"
        elif self.is_isosceles():
            return "Isosceles"
        elif self.is_right():
            return "Right"
        else:
            return "Scalene"
        
    def is_equilateral(self):
        return self.a == self.b == self.c

    def is_isosceles(self):
        return self.a == self.b or self.a == self.c or self.b == self.c

    def is_right(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)
