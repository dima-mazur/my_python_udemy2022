set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5}

# проверка является ли подмножеством
print(set1.issubset(set2))
print(set2.issubset(set1))
print(set2.issuperset(set1))

# объединение
set3 = set1.union(set2)
print(set3)

# пересечение
set3 = set1.intersection(set2)
print(set3)

# разница
set1 = {0, 1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5}
set3 = set1.difference(set2)
set4 = set1.symmetric_difference(set2)
print(set3, set4)

# обновление левого множества
set1.update(set2)
print(set1)

# добавить, удалить элемент
set1.add(6)
set1.remove(1)
# set1.pop(42)
set1.discard(42)
print(set1)

print(set1.clear())