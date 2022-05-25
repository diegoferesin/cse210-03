
class Player:
    def __init__(self):
        self._lives = ['  ___  ', '/     \ ', ' ----- ', '\     / ', ' \   /  ','   O   ', '  /|\  ', '  / \  ' ]
        self._letters_used = []

    def get_lives(self):
        return self._lives

    def set_lives(self, lives):
        self._lives = lives

    def get_letters_used(self):
        letters = ""
        for i in range(len(self._letters_used)):
            letters += f"{self._letters_used[i]} "
        
        print(f"Letters used: {letters}")

    def add_letters_used(self, letter):
        self._letters_used.append(letter)