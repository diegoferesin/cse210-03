import random

class Word:
    def __init__(self):
        self._list = ["pearl","mercedes","september","periphery","rocketman"]
        self._puzzle = self._list[random.randint(1,len(self._list))]
    
    def get_puzzle(self):
        return self._puzzle
