import time
from random_player import RandomPlayer


class TicTacToe:
    def __init__(self, board_size=1, num_players=12):
        self.player_icons = ['😊','😂','😍','😛','🤓','😎','😟','😤','😳','🥶','😴','😈']
        self.board = [["⬜️" for _ in range(board_size)] for _ in range(board_size)]
        self.available_moves = [i for i in range(1, (board_size**2) + 1)]

        self.current_player = 1

        self.random_players = [RandomPlayer() for _ in range(num_players)]

    def start(self):
        self.display_start()

    def display_start(self):
        print("1. lol")

        choice = self.get_start_choice()
        self.handle_start_choice(choice)

    def handle_start_choice(self, choice):
        if choice == 1:
            self.play()

    def reset_variables(self):
        self.board = [
            ["⬜️" for _ in range(len(self.board))] for _ in range(len(self.board))
        ]
        self.current_player = 1
        self.available_moves = [i for i in range(1, (len(self.board) ** 2) + 1)]

        self.random_players = [RandomPlayer() for _ in range(len(self.random_players))]

    def play(self):
        counter = 0
        while True:
            while True:
                counter += 1
                print(counter)
                # self.display_board()
                # self.display_available_moves()
                self.get_move()
                if self.check_someone_won():
                    return
                elif self.check_tie():
                    break
            
            self.reset_variables()

    def check_someone_won(self):
        def check_winner(char):
            n = len(self.board)

            for i in range(n):
                if all(self.board[i][j] == char for j in range(n)):
                    return True

            for j in range(n):
                if all(self.board[i][j] == char for i in range(n)):
                    return True

            if all(self.board[i][i] == char for i in range(n)):
                return True

            if all(self.board[i][n - 1 - i] == char for i in range(n)):
                return True

            return False

        for icon in self.player_icons:
            if check_winner(icon):
                self.display_board()
                return True
        return False

    def check_tie(self):
        if all(element != "⬜️" for row in self.board for element in row):
            # self.display_board()
            return True
        return False

    def display_board(self):
        for row in self.board:
            print("".join(map(str, row)))
        print()

    def display_available_moves(self):
        n = len(self.board)

        available_moves_matrix = [["⬜️" for _ in range(n)] for _ in range(n)]

        num_counter = 1

        for i in range(n):
            for j in range(n):
                if num_counter in self.available_moves:
                    available_moves_matrix[i][j] = num_counter
                num_counter += 1

        print("\nAvailable moves:")
        for row in available_moves_matrix:
            row_str = " ".join(
                map(lambda x: x if x == "⬜️" else x + " ", map(str, row))
            )
            print(row_str)
        print()

    def get_move(self):
        # print(f"{self.player_icons[self.current_player - 1]}'s turn")
        while True:
            try:
                current_random_player = self.random_players[self.current_player - 1]
                # print(f"Random player {self.current_player} is moving...")
                # time.sleep(0.1)
                move, _ = current_random_player.get_move(self.available_moves)
                # print(f"Random player {self.current_player}'s move: {move}")

                if move in self.available_moves:
                    self.available_moves.remove(move)

                    self.update_board(move)

                    if self.current_player == len(self.random_players):
                        self.current_player = 1
                    else:
                        self.current_player += 1

                return False

            except ValueError:
                pass

            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()

    def update_board(self, move):
        num_counter = 1

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if num_counter == move:
                    self.board[i][j] = self.player_icons[self.current_player - 1]
                    return

                num_counter += 1

    def get_start_choice(self):
        while True:
            try:
                choice = int(input("Choose an option: "))
                if 1 <= choice <= 1:
                    return choice

            except ValueError:
                pass

            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()


TicTacToe(5, 4).start()
