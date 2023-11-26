"""
>2 players
simulation repeat?
menus
save results and stats
AI players
"""

import time
import random_player
import ai_player



class TicTacToe:
    def __init__(self, board_size=3):
        self.player_icons = ['❌', '⭕']
        self.all_icons = ['❌', '⭕','😊','😂','😍','😛','🤓','😎','😟','😤','😳','🥶','😴','😈']
        self.available_icons = [icon for icon in self.all_icons if icon not in self.player_icons]
        self.board = [['⬜️' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 1
        self.available_moves = [i for i in range(1, (board_size ** 2) + 1)]

        self.random_player_1 = random_player.RandomPlayer(self.available_moves)
        self.random_player_2 = random_player.RandomPlayer(self.available_moves)

    def start(self):
        self.display_start()

    def display_start(self):
        print("\n\n❌⭕ tic tac toe\n")
        print("1. 2 player")
        print("2. Random")
        print("3. AI")

        print("\n4. Set icons")
        print("5. Exit\n")
        choice = self.get_start_choice()
        self.handle_start_choice(choice)


    def handle_start_choice(self, choice):            
        if choice == 1:
            self.play("2 player")
        elif choice == 2:
            choice = self.get_random_choice()
            self.handle_random_choice(choice)
        elif choice == 3:
            self.ai_menu()
        elif choice == 4:
            self.set_icons()
            self.display_start()            
        elif choice == 5:
            return


    def play(self, mode, settings=None):
        if settings:
            num_games = p1_wins = p2_wins = ties = moves = sum_moves_p1_win = sum_moves_p2_win= 0

            while num_games < settings["num_games"]:
                p1_move_count = p2_move_count = 0 
                while True:
                    if not settings["abbreviated_output"]:
                        self.display_board()
                        self.display_available_moves()
                    
                    
                    moves += 1
                    if self.current_player == 1:
                        p1_move_count += 1
                    else:
                        p2_move_count += 1

                    self.get_move(mode, settings["abbreviated_output"])
                    
                    checks = self.check_game_over(settings["abbreviated_output"])
                    if True in checks:
                        if checks[0]:
                            sum_moves_p1_win += p1_move_count
                            p1_wins += 1
                        elif checks[1]:
                            sum_moves_p2_win += p2_move_count
                            p2_wins += 1
                        elif checks[2]:
                            ties += 1
                        num_games += 1
                        self.reset_variables()
                        break
                time.sleep(0.05)
            
            p1_icon, p2_icon = self.player_icons

            print("\n\nCalculating stats...")
            time.sleep(1)
            print(f"\n{num_games} game{'s' if num_games > 1 else ''} played\n")
            print(f"{p1_icon} wins: {p1_wins} ({round(p1_wins / num_games, 3)}%)")
            print(f"{p2_icon} wins: {p2_wins} ({round(p2_wins / num_games, 3)}%)")
            print(f"   ties: {ties} ({round(ties / num_games, 1)}%)\n")

            print(f"{p1_icon} average total moves to win: {0 if p1_wins == 0 else round(sum_moves_p1_win / p1_wins, 3)}")
            print(f"{p2_icon} average total moves to win: {0 if p2_wins == 0 else round(sum_moves_p2_win/ p2_wins, 3)}")
            print(f"   average moves to reach end game: {round(moves / num_games, 3)}\n")
            
            exit()
        else:
            while True:
                self.display_board()
                self.display_available_moves()
                self.get_move(mode)
                if True in self.check_game_over():
                    if self.check_play_again():
                        self.reset_variables()
                        self.display_start()
                    else:
                        return

    def reset_variables(self):
        self.board = [['⬜️' for _ in range(len(self.board))] for _ in range(len(self.board))]
        self.current_player = 1
        self.available_moves = [i for i in range(1, (len(self.board) ** 2) + 1)]

        self.random_player_1 = random_player.RandomPlayer(self.available_moves)
        self.random_player_2 = random_player.RandomPlayer(self.available_moves)

    def check_play_again(self):
        while True:
            try:
                repeat_input = input("Play again? y/n: ")
                if repeat_input == "n":
                    return False
                elif repeat_input == "y":
                    return True
            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()


    def handle_random_choice(self, choice):
        if choice == 1:
            self.play("random vs human")
        elif choice == 2:
            self.play("random vs random", self.get_game_settings())
        elif choice == 3:
            pass
        elif choice == 4:
            pass        

    def get_game_settings(self):
        num_games = 1
        abbreviated_output = True
        save_results = False

        try:
            while True:
                num_games = int(input("\n      Number of games: "))
                if 0 < num_games <= 10000:
                    break
        except ValueError:
            pass
        except KeyboardInterrupt:
            print("\n\nGame exited.")
            exit()
        

        while True:
            try:
                abbreviated_output = input("      Abbreviated output? y/n: ")
                if abbreviated_output == "n":
                    abbreviated_output = False
                    break
                elif abbreviated_output == "y":
                    abbreviated_output = True
                    break
            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()

        while True:
            try:
                save_results = input("      Save results? y/n: ")
                if save_results == "n":
                    save_results = False
                    break
                elif save_results == "y":
                    save_results = True
                    break
            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()

        print("\nStarting games...")
        time.sleep(1.5)

        return {"num_games": num_games,
                "abbreviated_output": abbreviated_output,
                "save_results": save_results}


    def get_random_choice(self):
        print("\n   Random game modes:\n")
        print("   1. Random vs human")
        print("   2. Random vs random")
        print("   3. Random vs AI (Minimax)")
        print("   4. Random vs AI (Alpha-beta)\n")
        while True:
            try:
                choice = int(input("   Select an option: "))
                if 1 <= choice <= 4:
                    return choice
                
            except ValueError:
                pass

            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()

    def ai_menu(self):
        pass

    

    def check_game_over(self, abbreviated_output=False):
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
        
        p1_icon, p2_icon = self.player_icons

        if check_winner(p1_icon):
            if not abbreviated_output:
                print(f"\n\n{p1_icon} won!")
            self.display_board(abbreviated_output)
            return [True, False, False]

        elif check_winner(p2_icon):
            if not abbreviated_output:
                print(f"\n\n{p2_icon} won!")
            self.display_board(abbreviated_output)
            return [False, True, False]

        elif all(element != '⬜️' for row in self.board for element in row):
            if not abbreviated_output:
                print("\n\nTie!")
            self.display_board(abbreviated_output)
            return [False, False, True]

        return [False, False, False]



    
    def display_board(self, abbreviated_output=False):
        print()
        for row in self.board:
            print("".join(map(str, row)))
        if not abbreviated_output:
            print()
    
    def display_available_moves(self):
        n = len(self.board)

        available_moves_matrix = [['⬜️' for _ in range(n)] for _ in range(n)]

        num_counter = 1

        for i in range(n):
            for j in range(n):
                if num_counter in self.available_moves:
                    available_moves_matrix[i][j] = num_counter
                num_counter += 1

        print("\nAvailable moves:")
        for row in available_moves_matrix:
            row_str = " ".join(map(lambda x: x if x == '⬜️' else x + ' ', map(str, row)))
            print(row_str)
        print()

    def get_move(self, mode, abbreviated_output=False):
        if not abbreviated_output:
            print(f"{self.player_icons[0 if self.current_player == 1 else 1]}'s turn")
        while True:
            try:
                if mode == "2 player":
                    move = int(input("Enter your move: "))
                elif mode == "random vs human":
                    if self.current_player == 1:
                        move = int(input("Enter your move: "))
                    else:
                        if not abbreviated_output:
                            print("Random player is moving...")
                            time.sleep(1)
                        move = self.random_player_1.get_move()
                        if not abbreviated_output:
                            print(f"Random player's move: {move}")
                            time.sleep(1)

                elif mode == "random vs random":
                    if self.current_player == 1:
                        if not abbreviated_output:
                            print("Random player 1 is moving...")
                            time.sleep(1)
                        move = self.random_player_1.get_move()
                        if not abbreviated_output:
                            print(f"Random player 1's move: {move}")
                            time.sleep(1)
                    else:
                        if not abbreviated_output:
                            print("Random player 2 is moving...")
                            time.sleep(1)
                        move = self.random_player_2.get_move()
                        if not abbreviated_output:
                            print(f"Random player 2's move: {move}")
                            time.sleep(1)

                if move in self.available_moves:
                    self.available_moves.remove(move)
                    for player in [self.random_player_1, self.random_player_2]:
                        if player:
                            player.update_available_moves(self.available_moves)

                    self.update_board(move)
                    self.current_player = 2 if self.current_player == 1 else 1
                    return
                
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
                    self.board[i][j] = self.player_icons[0 if self.current_player == 1 else 1]
                    return

                num_counter += 1


    def get_start_choice(self):
        while True:
            try:
                choice = int(input("Select an option: "))
                if 0 <= choice <= 5:
                    return choice
                
            except ValueError:
                pass

            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()
            
    def set_icons(self):
        print("\nCurrent icons:")
        print(f"P1: {self.player_icons[0]}   P2: {self.player_icons[1]}\n")
        time.sleep(0.5)

        print("Available icons:\n")
        self.display_available_icons()
        while True:
            try:
                icon = int(input("Choose an icon for player 1 (0 to skip): "))
                if icon in range (0, len(self.available_icons) + 1):
                    if icon == 0:
                        break
                    self.available_icons.append(self.player_icons[0])
                    self.player_icons[0] = self.available_icons.pop(icon - 1)
                    break
            except ValueError:
                pass
            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()
            
        time.sleep(0.5)
        print(f"Player 1 icon set to {self.player_icons[0]}.\n")
        time.sleep(0.5)

        self.display_available_icons()
        while True:
            try:
                icon = int(input("Choose an icon for player 2 (0 to skip): "))
                if icon in range (0, len(self.available_icons) + 1):
                    if icon == 0:
                        break

                    self.available_icons.append(self.player_icons[1])
                    self.player_icons[1] = self.available_icons.pop(icon - 1)
                    break
            except ValueError:
                pass
            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()
            
        
        time.sleep(1)
        print(f"Player 2 icon set to {self.player_icons[1]}.")
        time.sleep(1)
        print("\nReturning to start menu...\n")
        time.sleep(1)

        
    def display_available_icons(self):
        for icon, number in zip(self.available_icons, range(1, len(self.available_icons) + 1)):
            time.sleep(0.05)
            print(f"{icon:<2} {number}")






game = TicTacToe(10)
game.start()