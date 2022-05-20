from game.player import Player

class Display:
    def __init__(self):
        self._puzzle = ""
        self.player = Player()
        self.jumper = ['  ___  ', '/     \ ', ' ----- ', '\     / ', ' \   /  ','   O   ', '  /|\  ', '  / \  ' ]


    def display_jumper(self):
        print("_ _ _ _ _\n")
        for i in range(0,self.player.get_lives()):
            print(self.jumper[i]+"\n")
        print("^^^^^^^\n")

    def display_puzzle(self,word):
        for letter in word:
            if letter in self.player.get_letters_used():
                print(letter + " ")
            else:
                print(" ")
