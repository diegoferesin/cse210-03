from importlib.abc import InspectLoader
from . import display as display_class
from . import word as word_class
from . import player as player_class

class Manager():    
    def __init__(self):
        """
        initialize the variables of the game:
            - instance of Word object
            - instance of Display object
            - instance of Player object
            - set boolean values to defaults
            - create empty letter variable and list
        """
        self.word = word_class.Word()
        self.display = display_class.Display()
        self.player = player_class.Player()

        self.isPlaying = True
        self.winCondition = False
        self.letter = ""
        self.guessed_letter = []


    def start_game(self):
        self.display.display_jumper(self.player.get_lives())
        """Display the parachute status and validate if the player the player fullfil the conditions to still playing the game"""
        while self.isPlaying:
            self.do_inputs()
            self.do_calculations()
            self.do_outputs()
    def do_inputs(self):
        """Get the input letter from the user" and check if they can keep playing"""
        self.letter = self.display.user_input()
        self.check_lives()

    def do_calculations(self):
        ''''Check if user's guess was correct and change game conditionals if needed'''
        self.check_guess()
        
        if not self.check_puzzle():
            self.isPlaying = False
            self.winCondition = True
        
        
    def do_outputs(self):
        """call the methods from display class"""
        self.display.display_jumper(self.player.get_lives())
        self.display.display_puzzle(self.guessed_letter, self.word.get_puzzle())
        self.display.display_letters_used(self.player.get_letters_used())
        if not self.isPlaying:

            if self.winCondition:
                self.display.display_win_message()
            else:
                self.display.display_loss_message()
                self.display.display_secret_word(self.word.get_puzzle())

    def check_guess(self):
        if self.letter in self.player.letters_used():
            self.display.display_used_letter()
            """validate the if the letter was already chosen and display the message"""
        elif self.letter not in self.word.get_puzzle():
            self.player.add_letters_used(self.letter)
            aux_lives = self.player.get_lives()
            aux_lives.pop(0)
            self.player.set_lives(aux_lives)
            """if the letter is was not chosen, add to the array of the input letters and remove one live to the player"""
        else:
            self.player.add_letters_used(self.letter)
            self.guessed_letter.append(self.letter)

    def check_puzzle(self):
        """checks to see letter is in puzzle"""
        checker = False
        if len(self.guessed_letter)>0:
            for i in self.word.get_puzzle():
                if not i in self.guessed_letter:
                    checker = True
        else:
            checker = True
        return checker

    def check_lives(self):
        """checks whether the player is out of lives and changes game conditional"""
        if len(self.player.get_lives()) == 0:
            self.isPlaying = False



    