import random


class Gallows:
    def __init__(self):
        self.limit = self.choose_limit()
        self.player_word = ''
        self.letters = []
        self.word = self.take_word()
        self.play()

    def choose_limit(self):
        self.limit = int(input('please, enter the limit of incorrect input: '))
        if self.limit < 0:
            print('limit must be > 0')
            self.choose_limit()
        else:
            self.limit = self.limit
        return self.limit

    def take_word(self, file=open('WordsStockRus.txt', 'r'),
                  default=None):

        word = default
        for i, line in enumerate(file, start=1):
            if random.randrange(i) == 0:
                word = line
        self.word = word.replace('\n', '')
        print("ok, i'm ready! My word is -")
        self.show_result()
        return self.word

    def show_limit(self):
        print(self.limit)

    def show_letter_list(self):
        self.letters.sort()
        print(self.letters)

    def make_step(self):
        lit = input('enter the letter or word: ')

        if lit == 'list':
            self.show_letter_list()
        elif lit == 'word':
            self.show_word()
        else:
            if lit not in self.letters:
                self.letters.append(lit)

            if lit == self.word:
                self.player_word = self.word
            elif lit in self.word:
                self.show_result()
                print('good, continue')
            else:
                print('oops, wrong...')
                self.limit -= 1
                print(f'you have {self.limit} number of tries')

    def show_result(self):
        result = []
        for i, l in enumerate(self.word):
            if l in self.letters:
                result.insert(i, l)
            else:
                result.insert(i, '_')
        self.player_word = ''.join(result)
        print(self.player_word)

    def show_word(self):
        if self.word:
            print(self.word)
        else:
            print('first you need create new word')

    @staticmethod
    def show_congrats():
        print('congrats! You WIN!')

    def play(self):
        while self.limit > 0:
            self.make_step()
            if self.player_word == self.word:
                self.show_congrats()
                break
        else:
            print('to many incorrect tries! You loose!')


game = Gallows()
