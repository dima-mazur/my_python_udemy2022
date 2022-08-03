# all_1 = all([True, True, True])
# all_2 = all([True, False, True])
# all_3 = all([1, 'string', 2])
# all_4 = all([0, 2, 88])
# print(all_1, all_2, all_3, all_4)
#

# names = ['carlsen', 'Caruana', 'Mamedyanov', 'Ding']
# ratings = [2842, 2822, 2801, 2797]
#
# players = dict(zip(names, ratings))
# print(players)

# argument = 'Hello Dima!'
def greeting(argument):
    """
    :param argument: what do you wanna print
    :return: argument in console
    """
    print(argument)


greeting('hello world')
help(greeting)


def save_players(**kwargs):
    for k, v in kwargs.items():
        print(f'Player {k} has rating {v}')


save_players(Carlsen=2800, Giri=2780)

def catc_taxes(*args):
    for x in args:
        print(f'Got payment = {x}')
    return sum(args) * 0.06


print(catc_taxes(10, 20, 30, 40))
