# print(issubclass.__doc__)

class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


circle = Circle(10)

print(issubclass(Circle, Shape))
print(isinstance(circle, Circle))
print(isinstance(circle, Shape))

print(isinstance('Hi', str))

print(callable(circle))
print(callable(print))

if hasattr(circle, 'radius'):
    print(getattr(circle, 'radius'))
    setattr(circle, 'radius', 20)
    print(getattr(circle, 'radius'))

