import math
import random

class Player:
    def __init__(self, letter):
        #letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomPcPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        pass
        # super().get_move(game)

class Player2(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass
        # super().get_move(game)