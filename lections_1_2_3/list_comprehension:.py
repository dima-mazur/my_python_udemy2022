greeting = 'hello, world'
chars = []
# for l in greeting:
#     chars.append(l)
#
# print(chars)

chars = [l for l in greeting]
print(chars)

chars2 = [l for l in 'blablabla']
print(chars2)

numbers = [i for i in range(1, 10)]
print(numbers)

numbers2 = [i*i for i in range(1, 10)]
print(numbers2)

numbers3 = [i*i for i in range(1, 10) if i % 2 != 0]
print(numbers3)

len_in_cm = [12, 10, 54, 124]
len_in_inches = [(round(cm / 2.54, 2)) for cm in len_in_cm]
print(len_in_inches)

list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, -3, 5, -2]
pairs = [(x, y) for x in list1 for y in list2 if x + y == 0]
print(pairs)