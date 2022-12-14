import pickle

class Character():
    def __init__(self, race, damage=10):
        self.race = race
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0

    # def __getstate__(self):

    def __setstate__(self, state):
        self.race = state.get('race', 'elf')
        self.damage = state.get('damage', 10)
        self.armor = state.get('armor', 20)
        self.health = state.get('health', 100)


c = Character('Elf')
c.hit(10)
print(c.health)


with open(r'game_state1.bin', 'w+b') as f:
    pickle.dump(c, f)

with open(r'game_state1.bin', 'rb') as f:
    c = pickle.load(f)

print(c.health)
print(c.__dict__)