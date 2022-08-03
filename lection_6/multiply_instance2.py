class Animal:
    def set_health(self, health):
        print('set in animal')


class Carnivour(Animal):
    def set_health(self, health):
        print('set in carnivour')


class Mammal(Animal):
    def set_health(self, health):
        print('set in mammel')


class Dog(Mammal, Carnivour):
    pass


dog = Dog()
dog.set_health(100)

