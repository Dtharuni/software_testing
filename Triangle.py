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
    def classify_triangle(self, a, b, c):
        # Your triangle classification logic here
        pass


    def classifyTriangle(a, b, c):
        if a > 200 or b > 200 or c > 200:
            return 'InvalidInput'

        if a <= 0 or b <= 0 or c <= 0:
            return 'InvalidInput'

        if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
            return 'InvalidInput'

        if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
            return 'NotATriangle'

        if a == b == c:
            return 'Equilateral'
        elif (a**2 + b**2) == (c**2):
            return 'Right'
        elif (a != b) and (b != c) and (a != c):
            return 'Scalene'
        else:
            return 'Isosceles'
