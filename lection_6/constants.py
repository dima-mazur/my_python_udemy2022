class Character():
    MAX_SPEED = 100

    def __init__(self, race, damage=10):
        self.__race = race
        self.damage = damage
        self._health = 100

        self._current_speed = 20

    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed

#
# print(Character.MAX_SPEED)
# Character.MAX_SPEED = 10
# print(Character.MAX_SPEED)

c = Character('Elf')
# c.race = 'ork'
#
# print(c._Character__race)
# c._Character__race = 'Ork'
# print(c._Character__race)
#
# print(c.health)

print(c.current_speed)
c.current_speed = 80
print(c.current_speed)
c.current_speed = 200
print(c.current_speed)