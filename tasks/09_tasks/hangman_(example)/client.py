from game import Game
from game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

letters_cout = len(word)

print(f'The word consist of {letters_cout} letters')
print('Try to guess the word letter by letter')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Pick a letter')
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f'Remaining tries = {game.remaining_tries}')
    print(f'Tried letters: {chars_list_to_str(game.tried_letter)}')

if game.game_status == GameStatus.LOST:
    print('You are hanged!')
    print(f'The word was: {game.word}')
else:
    print('Congratulations! You won!')