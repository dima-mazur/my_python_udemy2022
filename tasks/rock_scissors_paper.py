import random
var = ['R', 'S', 'P']
# comp_choice = random.choice(var)
# print(comp_choice)
trise = True

while trise:
    user_choice = input(f'Do your choice ("R" - Rock, "S" - Scissors, "P" - Paper) - ')
    comp_choice = random.choice(var)
    print(comp_choice)
    if comp_choice == user_choice:
        print('try again!')
        continue
    elif comp_choice == 'R' and user_choice == 'S':
        print('You loose((')
    elif comp_choice == 'R' and user_choice == 'P':
        print('You win!!!')
    elif comp_choice == 'S' and user_choice == 'R':
        print('You win!!!')
    elif comp_choice == 'S' and user_choice == 'P':
        print('You loose((')
    elif comp_choice == 'P' and user_choice == 'S':
        print('You win!!!')
    elif comp_choice == 'P' and user_choice == 'R':
        print('You loose((')
    end_game = input(f'Do you wanna to continue the game? ("Y" - yes, "N" - no) - ')
    if end_game == 'Y':
        continue
    elif end_game == 'N':
        print('Bye')
        break