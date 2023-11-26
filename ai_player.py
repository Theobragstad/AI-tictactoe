import random

class AIPlayer:
    def __init__(self, available_moves):
        self.available_moves = available_moves

    def get_move(self):
        return random.choice(self.available_moves)
    
    def update_available_moves(self, available_moves):
        self.available_moves = available_moves

