from game import YesOrNot
from game_status import GameStatus

game = YesOrNot()
game.set_tries()
game.read_file()


while game.game_status == GameStatus.IN_PROGRESS:
    game.generate_question()


if game.game_status == GameStatus.LOST:
    print('You loose!')
# else:
#     print('Congratulations! You won!')
