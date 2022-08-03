# Вывести лесенкой символ звёздочки по кол-ву строк

# strings = int(input('How many strings do you wont? - '))
# for i in range(0, strings+1):
#     print('*' * i)


# 2.

# number = int(input('input the number - '))
# for i in range(0, number + 1):
#     if i % 2 == 0:
#         print(f'{i} is EVEN')
#     else:
#         print(f'{i} is ODD')

# 3

# limit = int(input('input the number - '))
# arg_list = []
# for i in range(limit+1):
#     if i % 3 == 0 or i % 5 == 0:
#         arg_list.append(i)
# print(sum(arg_list))

# 4
# first_lst = [1, 2, 3, 4, 5, 6, 7, 8]
# second_lst = [0, 13, 25, 10, 8, 7]
# joined_list = []
#
# for i in first_lst:
#     if i % 2 != 0:
#         joined_list.append(i)
# for v in second_lst:
#     if v % 2 == 0:
#         joined_list.append(v)
# print(joined_list)

# 5 вес карт
# cards = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
# current_hand = [2, 3, 4, 10, 'Q', 5]
# cards_list = []
#
# for i in current_hand:
#     cards_list.append(cards.get(i))
#
# cards_sum = sum(cards_list)
# print(cards_sum)

# 6 проверка на Флеш
#
# table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
# hand_cards = ["J_D", "3_D"]
#
# play_cards = table_cards + hand_cards
# mast = []
#
# for i in play_cards:
#     mast.append(i[-1])
# flash = ''
# for suit in 'CHSD':
#     if mast.count(suit) >= 5:
#         flash = True
# if flash:
#     print('Flush!')
# else:
#     print('No Flush!')

# 7 палиндром
number = 12321
check = number
reverse = 0

while number > 0:
    digit = number % 10
    # print(digit)
    number = number // 10
    # print(number)
    reverse = reverse * 10
    # print(reverse)
    reverse = reverse + digit
    # print(reverse)
if check == reverse:
    print('Palindrome')
else:
    print('No Palindrome')




