from abc import ABC
from abc import abstractmethod

class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        print('calc perimetr')

    def drag(self):
        print('Basic dragging')


# s = Shape()
import math

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f'Drawing triangle with sides - {self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s-self.a) + (s - self.b) + (s - self.c))

    def perimetr(self):
        return self.a + self.b + self.c

    def drag(self):
        super().drag()
        print('Additional actions')


t = Triangle(10, 10, 10)
print(t.perimetr())
t.drag()
