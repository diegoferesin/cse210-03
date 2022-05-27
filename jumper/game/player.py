
class Player:
    def __init__(self):
        """initialize the lives and the array to store the letters chosen by the player"""
        self._lives = ['  ___  ', '/     \ ', ' ----- ', '\     / ', ' \   /  ','   O   ', '  /|\  ', '  / \  ' ]
        self._letters_used = []

    def get_lives(self):
        """return the number of lives the player has"""
        return self._lives

    def set_lives(self, lives):
        """change the number of lives the player has"""
        self._lives = lives

    def get_letters_used(self):
        letters = ""
        for i in range(len(self._letters_used)):
            letters += f"{self._letters_used[i]} "
        """display the letter chosen by the player"""
        return letters

    def letters_used(self):
        """return the list of letters that the player has used"""
        return self._letters_used
    
    def add_letters_used(self, letter):
        """append letter to list of already-used letters"""
        self._letters_used.append(letter)