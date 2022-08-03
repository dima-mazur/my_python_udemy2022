def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

# Возвращает итеррируемый объект
mapped = map(square, numbers)

for x in mapped:
    print(x)

print(list(map(square, numbers)))


# ----

# def is_adult(age):
#     return age >= 18
#
#
ages = [14, 18, 21, 16, 30]
#
# print(list(filter(is_adult, ages)))


is_adult = lambda age: age >= 18
print(list(filter(is_adult, ages)))


multiplier = lambda x, y: x*y
print(multiplier(2, 3))
