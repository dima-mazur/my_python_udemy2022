# class Character:
#
#     def __new__(cls):
#         obj = super().__new__(cls)
#         return obj
#
#     def __init__(self):
#         self.race = 'Elf'


class Character:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.race = 'Elf'

c = Character()
print(c.race)

d = Character()
d.race = 'Ork'

print(c.race)
print(d.race)