# coord = {0: '0.0', 1: '0.2', 2: '0.4', 3: '2.0', 4: '2.2',
#            5: '2.4', 6: '4.0', 7: '4.2', 8: '4.4'}
#
# for i in range(5):
#
#     for k in range(5):
#         if k % 2:
#             print('|', end='')
#         elif i % 2 and k % 2 == 0:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print('')

# pool = {0: {'x': 0, 'y': 0},
#         1: {'x': 0, 'y': 2},
#         2: {'x': 0, 'y': 4},
#         3: {'x': 2, 'y': 0},
#         4: {'x': 2, 'y': 2},
#         5: {'x': 2, 'y': 4},
#         6: {'x': 4, 'y': 0},
#         7: {'x': 4, 'y': 2},
#         8: {'x': 4, 'y': 4}
#         }

# for keys in pool:
#         print(keys)
# print(pool[5]['x'])


# class x_or_o:
#         def __init__(self):
#                 pass
#
#         def make_lines(self):
#                 line = ''
#                 for i in range(3):
#                         for k in range(3):
#                                 line += '-'
#                         print(line)
#
# x = x_or_o()
# x.make_lines()

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')


def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'x' or state[x] == '0'):
            return state[x]
    return ''


def play_game(board):
    current_sign = 'x'
    while(get_winner(board, winning_combinations) == ''):
        index = int(input(f'Where do you want to draw {current_sign}? - '))
        board[index] = current_sign

        print_state(board)

        winner_sign = get_winner(board, winning_combinations)
        if winner_sign != '':
            print(f'{winner_sign} is a winner!')

        current_sign = 'x' if current_sign == '0' else '0'


play_game(board)
