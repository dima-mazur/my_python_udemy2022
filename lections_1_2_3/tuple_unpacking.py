person = [('John', 22), ('Bob', 32), ('Dave', 25)]
for (name, age) in person:
    print(f'{name} is {age}')


players = dict(Carlson=2842, Caruana=2822, Mazur=2820)
for item in players:
    print(item)

for item in players.items():
    print(item)

for k, v in players.items():
    print(f'{k} has rating {v}')

for v in players.values():
    print(v)
#
#

# find all pairs sum which equals 0
list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]

pairs = []
for x in list1:
    for y in list2:
        if x+y == 0:
            pairs.append((x, y))
print(pairs)



