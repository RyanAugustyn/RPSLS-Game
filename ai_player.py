from player import Player
import random

class AI_Player(Player):
    def __init__(self):
        super().__init__()

    def get_gesture(self, rpsls_list):
        return random.choice(rpsls_list)
    