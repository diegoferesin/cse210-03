
class Player:
    def __init__(self):
        """initialize the lives and the array to store the letters chosen by the player"""
        
        self._lives = ['  ___  ', '/     \ ', ' ----- ', '\     / ', ' \   /  ','   O   ', '  /|\  ', '  / \  ' ]
        self._letters_used = []

    def get_lives(self):
        """return the lives of the player"""
        return self._lives

    def set_lives(self, lives):
        """se the initial lives of the game"""
        self._lives = lives

    def get_letters_used(self):
        letters = ""
        for i in range(len(self._letters_used)):
            letters += f"{self._letters_used[i]} "
        
        """display the letter chosen by the player"""
        return letters

    def letters_used(self):

        """return the letter shocen by the player"""
        return self._letters_used
    
    def add_letters_used(self, letter):
        """append the letter if there is not in the array letter"""
        self._letters_used.append(letter)