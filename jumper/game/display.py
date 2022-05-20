from game.word import Word
from game.player import Player

class Display:
    def __init__(self):
        self._word = ""
        self.player = Player()
        self.jumper = ['  ___  ', '/     \ ', ' ----- ', '\     / ', ' \   /  ','   O   ', '  /|\  ', '  / \  ' ]


    def display_jumper(self):
        print("_ _ _ _ _\n")
        for i in range(0,self.player.get_lives()):
            print(self.jumper[i]+"\n")
        print("^^^^^^^\n")
