import random

class RandomPlayer:
    def get_move(self, available_moves):
        return random.choice(available_moves)

