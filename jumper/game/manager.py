from importlib.abc import InspectLoader
from . import display as display_class
from . import word as word_class
from . import player as player_class

class Manager():    
    def __init__(self):
        self.word = word_class.Word()
        self.display = display_class.Display()
        self.player = player_class.Player()

        self.isPlaying = True
        self.winCondition = False
        self.letter = ""

        self.guessed_letter = []


    def start_game(self):
        self.display.display_jumper(self.player.get_lives())
        while self.isPlaying:
            self.do_inputs()
            self.do_calculations()
            self.do_outputs()

    def do_inputs(self):
        self.letter = self.display.user_input()

    def do_calculations(self):
        self.check_guess()
        if not self.check_puzzle():
            self.isPlaying = False
            self.winCondition = True

    def do_outputs(self):

        self.display.display_jumper(self.player.get_lives())
        self.display.display_puzzle(self.guessed_letter, self.word.get_puzzle())
        self.player.get_letters_used()
        if not self.isPlaying:

            if self.winCondition:
                self.display.display_win_message()
            else:
                self.display.display_loss_message()

    def check_guess(self):
        if self.letter in self.player.letters_used():
            self.display.display_used_letter()
        elif self.letter not in self.word.get_puzzle():
            self.player.add_letters_used(self.letter)
            aux_lives = self.player.get_lives()
            aux_lives.pop(0)
            self.player.set_lives(aux_lives)
        else:
            self.player.add_letters_used(self.letter)
            self.guessed_letter.append(self.letter)

    def check_puzzle(self):
        checker = False
        if len(self.guessed_letter)>0:
            for i in self.word.get_puzzle():
                if not i in self.guessed_letter:
                    checker = True
        else:

            checker = True

        return checker

    def check_lives(self):

        if len(self.player.get_lives()) == 0:
            self.isPlaying = False



    