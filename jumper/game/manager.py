from game.word import Word
from game.display import Display

class Manager():    
    def __init__(self):
        self.word = Word()
        self.display = Display()

    def guess():
        letter = input("Guess a letter [a-z]: ")
        return letter

    def check_guess(self,letter):
        if letter not in self.word.get_puzzle():
            self.display.set_lives()


    