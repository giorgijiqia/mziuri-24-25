#exercise 1

class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def add(self, other):
        new_top = self.top * other.bottom + other.top * self.bottom
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)

    def inverse(self):
        return Fraction(self.bottom, self.top)

fraction1 = Fraction(3, 5)
fraction2 = Fraction(2, 7)

result_addition = fraction1.add(fraction2)
print("ჯამი:", result_addition)

inverse_fraction = fraction1.inverse()
print("შებრუნებული წილადი:", inverse_fraction)

#exercise 2

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

point1 = Point(3, 5)
point2 = Point(6, 9)

print("Point 1 distance from origin:", point1.distance_from_origin())
print("Point 2 distance from origin:", point2.distance_from_origin())



#exercise 3


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def distance_to(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

x1, y1 = map(int, input("Enter coordinates for point a (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates for point b (x2 y2): ").split())

point_a = Point(x1, y1)
point_b = Point(x2, y2)

print("Point a:", point_a)
print("Point b:", point_b)
print("Distance between a and b:", point_a.distance_to(point_b))