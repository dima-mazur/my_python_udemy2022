from typing import Literal, Final, final


def open_file(file, mode: Literal['r', 'w']):
    pass


open_file('file.txt', 'r')

# constants
pi: Final = 3.14
pi = 1.2  # doesn't change


# запрет наследования класса
@final
class Dog:
    def __init__(self):
        self.paws = 4
        self.health = 100

    def bark(self):
        print('woof-woof')


class SuperDog(Dog):
    def __init__(self):
        super().__init__()
        self.health = 200


dog = SuperDog()
print(dog.health)
dog.bark()
