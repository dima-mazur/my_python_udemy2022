from game_status import GameStatus
import random

class YesOrNot:
    def __init__(self, path='Questions.csv', tries=3):
        self.path = path
        self.tries = tries
        self.game_status = GameStatus.NOT_STARTED
        self.questions = {}
        self.user_answer = ''


    def read_file(self):
        file = open(self.path, 'r')
        for i, lines in enumerate(file):
            question = lines.split(';')[0]
            answer = lines.split(';')[1]
            info = lines.split(';')[2][:-2:]

            self.questions[i] = {question: {answer: info}}
            self.game_status = GameStatus.IN_PROGRESS

    def status(self):
        return self.game_status

    def check_life(self):
        if self.tries == 0:
            self.game_status = GameStatus.LOST

    def generate_question(self):

        rand_index = random.randint(0, len(self.questions)-1)
        question_module = self.questions[rand_index]

        question = list(question_module.keys())[0]
        print(question)

        correct_answer = list(list(question_module.values())[0].keys())[0]
        info = list(list(question_module.values())[0].values())[0]
        user_answer = input('how do you mine this is true or false? (y/n) ')
        if user_answer == 'y':
            self.user_answer = 'Yes'
        elif user_answer == 'n':
            self.user_answer = 'No'

        if self.user_answer == correct_answer:
            print("Good! it's correct answer!")
            print(info)
        else:
            print("oops! it's wrong answer!")
            print(info)
            self.tries -= 1

        self.check_life()

    def set_tries(self):
        tries = input('Hello! you have 3 times to try to guess the correct answer.'
                      'Do you want to change the county to times? (y/n) ')
        if tries == 'y':
            player_tries = input('How many tries do you won? (min 0, max 5) ')
            if 0 <= int(player_tries) <= 5:
                self.tries = int(player_tries)
                print(f'OK, you have {self.tries} times to tries')
            else:
                print('incorrect input! you will have 3 tries!')






# game = YesOrNot()
# game.read_file()
# # print(game.questions)
# game.play()