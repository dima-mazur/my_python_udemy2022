# 1 посчитать сколько бонусных чашек при заказе
# buy_cups = input('how many cups of coffee do you want? - ')
# input_cups = int(buy_cups)
#
# print('you win bonus cups in count {} pc'.format(input_cups // 6))

# 2 расстояние между двумя точками на плоскости
# x1 = int(input('coord X1 - '))
# y1 = int(input('coord Y1 - '))
# x2 = int(input('coord X2 - '))
# y2 = int(input('coord Y2 - '))
# import math
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print(round(distance, 3))

# количество лап на ферме
chicken = int(input('chicken - '))
cows = int(input('cows - '))
pigs = int(input('pigs - '))
paws = chicken * 2 + cows * 4 + pigs * 4
print('total paws - ', paws )