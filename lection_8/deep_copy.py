import copy

list1 = [1, 2, 3, [4, 5, 6]]

copied_list = list1.copy()
copied_list[3].append(7)

print(list1)
print(copied_list)

list1.append(8)


print(list1)
print(copied_list)

shallow_copy = copy.copy(list1)
shallow_copy[3].append(8)

print(list1)
print(shallow_copy)


deep_copy = copy.deepcopy(list1)
deep_copy[3].append(9)

print(list1)
print(deep_copy)