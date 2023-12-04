import random
import time

class RandomPlayer:
    def get_move(self, available_moves):
        start_time = time.time()
        return random.choice(available_moves), time.time() - start_time

