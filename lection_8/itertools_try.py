import itertools

iterable_1 = [1, 2, 3]

iterator = iter(iterable_1) # будет вызван метод __iter__()
print(type(iterator))

print(next(iterator)) # будет вызван метод __next__()

# генерация четных чисел
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

even_numbers = itertools.count(0, 2)
print(list(next(even_numbers) for _ in range(5)))

enum_sim = list(zip(itertools.count(), ['a', 'b', 'c']))
print(enum_sim)


def print_iterable(iterable, end = None):
    for x in iterable:
        if end:
            print(x, end = end)
        else:
            print(x)

ones = itertools.repeat(1, 5) # задает значение, которое повторяется определенное кол-во раз
print_iterable(ones, ' ')


# возведение в квадрат
print(list(map(pow, range(10), itertools.repeat(2))))


# бесконечный итератор по набору значений
pos_neg_ones = itertools.cycle([1, -1])
print(list(next(pos_neg_ones) for _ in range(10)))

# аккумулятор
print(list(itertools.accumulate([1, 2, 3, 4, 5])))


# разложить последовательность
print(list(itertools.chain('ABC', 'DEF')))

# убрать значение пока выражение истинно
print(list(itertools.dropwhile(lambda x: x<3, [1, 2, 3, 4, 5])))
print(list(itertools.takewhile(lambda x: x<3, [1, 2, 3, 4, 5])))
print(list(itertools.filterfalse(lambda x: x%2==0, range(10))))

# пройти несколько раз по итерируемому объекту
iterable1, iterable2 = itertools.tee([1, 2, 3], 2)
print_iterable(iterable1, ' ')
print('\n iterable is exausted')
print_iterable(iterable2, ' ')

# группировка данных по ключу
lst = [1, 2, 1, 2, 2, 3, 3, 2]
for key, grp in itertools.groupby(sorted(lst)):
    print('{}:{}'.format(key, list(grp)))

# комбинаторика
pin = [7, 5, 2, 8]
print(list(itertools.permutations(pin)))

# генерация колоды карт
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']

lst = list(itertools.product(ranks, suits))
print(lst)
