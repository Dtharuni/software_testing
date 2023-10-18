""" Testing Assignment """
import datetime

def my_brand(hw_name):
    """ This is my brand for Testing assignment """
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    screen_brand = f"=*=*=*= Tharuni D =*=*=*=\n\n" \
                  f"=*=*=*= Course 2023S-SSW567-WS =*=*=*=\n\n" \
                  f"=*=*=*= {hw_name} =*=*=*=\n\n" \
                  f"=*=*=*= {current_datetime} =*=*=*=\n"
    print(screen_brand)

my_brand("HW 00")


class TriangleClassifier:
    """ class for triangle classification """

    def classify_triangle(self, a, b, c):
        """ Definition for triangle classification """
        if self._is_invalid_triangle(a, b, c):
            return 'InvalidInput'
        if self._is_not_a_triangle(a, b, c):
            return 'NotATriangle'

        if a == b == c:
            return 'Equilateral'
        if self._is_right_triangle(a, b, c):
            return 'Right'
        if a == b or b == c or a == c:
            return 'Isosceles'
        return 'Scalene'

    def _is_invalid_triangle(self, a, b, c):
        return a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0 or \
            not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int)

    def _is_not_a_triangle(self, a, b, c):
        return a >= (b + c) or b >= (a + c) or c >= (a + b)

    def _is_right_triangle(self, a, b, c):
        return (a**2 + b**2) == (c**2) or (a**2 + c**2) == (b**2) or (b**2 + c**2) == (a**2)
