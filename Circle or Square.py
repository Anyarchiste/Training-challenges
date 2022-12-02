import math

'''
Given the radius of a circle and the area of a square, return True if the
circumference of the circle is greater than the square's perimeter and
False if the square's perimeter is greater than the circumference of
the circle.
'''


def circle_or_square(radius, square, pi):
    circle_circonference = radius * 2 * pi
    square_permimeter = math.sqrt(square) * 4
    if circle_circonference > square_permimeter:
        return True
    else:
        return False


pi = 3.14
radius_circle = 8
area_square = 144
print(circle_or_square(radius_circle, area_square, pi))
