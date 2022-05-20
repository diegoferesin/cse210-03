
class Player:
    def __init__(self):
        self._lives = 8
        self._letters_used = []

    def get_lives(self):
        return self._lives

    def set_lives(self):
        self._lives -= 1

    def get_letters_used(self):
        return self._letters_used

    def add_letters_used(self,letter):
        self._letters_used.append(letter)