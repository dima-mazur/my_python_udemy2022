def game_of_steak():
    stick = 10
    p1 = 0
    p2 = 0
    while stick > 0:
        print(f'Total sticks = {stick}')

        while True:
            p1 = int(input('Player 1 input number of sticks to remove (1, 2 or 3) - '))

            if p1 > 3 or p1 < 1:
                print('the number of sticks should be from 1 to 3')
                continue
            else:
                break

        stick -= p1
        print(f'Total sticks = {stick}')

        if stick == 0:
            print('Player 2 win!')
            break

        while True:
            p2 = int(input('Player 2 input number of sticks to remove (1, 2 or 3) - '))

            if p2 > 3 or p2 < 1:
                print('the number of sticks should be from 1 to 3')
                continue
            else:
                break

        stick -= p2

        if stick == 0:
            print('Player 1 win!')
            break


game_of_steak()



