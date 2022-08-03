x = 'hello! my name is Dima'

print(len(x))
# длина строки

print(x[len(x)-1])
# последний символ

print(x.count('a'))
# количество вхождений

print(x.capitalize())
# первый символ в верхнем регистре

print(x.upper())
# все символы капсом

print(x.lower())
# все символы в нижнем регистре

print(x.isupper(), x.islower())
# проверка регистра

print(x.find('D'))
# поиск индекса первого вхлждения

print('abc123'.isalnum())
print('abc123!'.isalnum())
print('abc'.isalpha())
# проверка строки на вхождение символов чисел и букв (без спецсимволов)

print('   '.isspace())
print(''.isspace())
# проверка на пустоту

empty_string = ' '
print(empty_string == '')

empty_string2 = '   '
print(empty_string2.strip(' ') == '')
# вариант проверки 2


if not empty_string2:
    print('empty')
else:
    print('not empty')


h = 'hello'
print(h.startswith('he'))
print(h.endswith('lo'))
# проверка начала или конца подстроки

split = h.split('l')
print(type(split))
print(split)
# разделитель, получаем новый объект лист

data = '12; 10; 7; 10'
dataset = data.split(';')
print(dataset)


python = 'python is fun'
print(python.partition('is'))
