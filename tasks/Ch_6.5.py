import math


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        s = math.pi * self.r**2
        return s

    def get_perimeter(self):
        l = 2 * math.pi * self.r
        return l



