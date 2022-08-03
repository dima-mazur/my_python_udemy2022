class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        result = self.a / self.b
        return round(result)


c = Calculator(10, 5)
print(c.add())
print(c.subtract())
print(c.multiply())
print(c.divide())
