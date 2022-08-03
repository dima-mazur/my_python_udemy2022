class Animal:
    def set_health(self, health):
        print('set in animal')


class Carnivour(Animal):
    def set_health(self, health):
        super().set_health(health)
        print('set in carnivour')


class Mammal(Animal):
    def set_health(self, health):
        super().set_health(health)
        print('set in mammel')


class Dog(Mammal, Carnivour):
    def set_health(self, health):
        super().set_health(health)
        # Mammal.set_health(self, health)
        # Carnivour.set_health(self, health)

        print('set in dog')


dog = Dog()
dog.set_health(100)

