import random

class Word:
    def __init__(self):
        self._list = ["pearl", "mercedes", "september", "periphery", "rocketman"]
        self._puzzle = self._list[random.randint(0,len(self._list)-1)]
    
    def get_puzzle(self):
        return self._puzzle
