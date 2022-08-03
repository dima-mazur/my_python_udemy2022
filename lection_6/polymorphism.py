import math

class Shape():

    def __init__(self):
        print('Shape created')

    def draw(self):
        print('Drawing a shape')

    def area(self):
        print('Calc area')

    def perimetr(self):
        print("Calc perimetr")


shape = Shape()
# print(shape)


class Rectangle(Shape):

    def __init__(self, width, height):
        Shape.__init__(self)

        self.width = width
        self.height = height

        print('Rectangle create')

        Shape.area(self)

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return 2*(self.width + self.height)

    def draw(self):
        print(f'Drawing rectangle with width={self.width} and height={self.height}')


rect = Rectangle(10, 15)
# print(rect.area())
# shape.area()
# print(rect.perimetr())
# print(rect.draw())


class Triangle(Shape):

    def __init__(self, a, b, c):
        Shape.__init__(self)

        self.a = a
        self.b = b
        self.c = c

        print('Triangle created')

    def draw(self):
        print(f'Drawing triangle with sides={self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))

    def perimetr(self):
        return self.a + self.b + self.c


triangle = Triangle(10, 10, 10)
print(triangle.area())
print(triangle.perimetr())
print(triangle.draw())


for shape in [rect, triangle]:
    shape.draw()