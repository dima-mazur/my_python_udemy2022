import random
# number = random.randint(1, 50)
# i = 0
# user_number = 0
# result = ''
#
# while i < 6:
#     user_number = int(input('my number is - ' ))
#     if user_number == number:
#         result = 'you did it!'
#         print(result)
#         break
#     elif user_number < number:
#         i = i + 1
#         result = 'your number is less, try again'
#         print(result)
#         continue
#     elif user_number > number:
#         i = i + 1
#         result = 'your number is more, try again'
#         print(result)
#         continue
#
# print(result)

# v2
number = random.randint(1, 50)
tries = 0

while tries < 6:
    guess = int(input('my number is - '))
    tries += 1
    if guess < number:
        print('your number is less, try again')

    if guess > number:
        print('your number is more, try again')

    if guess == number:
        print('you did it!')
        break
    if guess != number and tries == 6:
        print('Looser!')





