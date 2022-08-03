class Character():
    max_speed = 100
    dead_health = 0
    # constructor added race

    def __init__(self, actual_race, damage=10, armor=20):

        self.race = actual_race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == Character.dead_health


# unit = Character('Elf', damage=20, armor=30)
# # print(type(unit))
# print(unit.race)
# print(unit.damage)
# print(unit.armor)

unit = Character('Ork')
print(unit.race)
print(Character.max_speed)

unit.hit(20)
print(unit.health)
print(unit.is_dead())
unit.hit(80)
print(unit.is_dead())


