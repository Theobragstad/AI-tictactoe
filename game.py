"""
Bigger board size long AI movetime
Utilize depth better, Plies
Confirm project requirements.

submit, interview
bugs find
"""

import time
import random
from datetime import datetime

from ai_player import AIPlayer
from random_player import RandomPlayer


class TicTacToe:
    def __init__(self, board_size=3):
        self.player_icons = ['❌','⭕']
        self.all_icons = ['❌','⭕','😊','😍','😛',
                          '🤓','😎','😟','😤','😳',
                          '🥶','😴','😈','🤔','👀',
                          '🐢','🐬','🐊','🦎','✅',
                          '🍔','🍕','🌮','🍰','🧊',
                          '🚗','🛸','🚁','🎨','😹',
                          '😺','🍉','🎲','🌴','🌳']

        self.available_icons = [icon for icon in self.all_icons if icon not in self.player_icons]

        self.board = [['⬜️' for _ in range(board_size)] for _ in range(board_size)]
        self.available_moves = [i for i in range(1, (board_size ** 2) + 1)]

        self.current_player = 1

        self.random_players = [RandomPlayer() for _ in range(2)]
        self.ai_players = None

      
        self.player_type_to_icon = [['Player 1', self.player_icons[0]], ['Player 2', self.player_icons[1]]]

  



 
       
















    def start(self):
        self.display_start()

    def display_start(self):
        print(f"\n\n{self.player_icons[0]} Tic Tac Toe {self.player_icons[1]}\n")
        print("1. 2 player (normal)")
        print("2. Random")
        print("3. AI")

        print("\n4. Set icons")
        # print("5. Set board size")
        print("5. Exit\n")
        choice = self.get_start_choice()
        self.handle_start_choice(choice)


    def handle_start_choice(self, choice):            
        if choice == 1:
            self.play(mode="2 player")
        elif choice == 2:
            random_choice = self.get_random_choice()
            self.handle_random_choice(random_choice)
        elif choice == 3:
            ai_choice = self.get_ai_choice()
            self.handle_ai_choice(ai_choice)
        elif choice == 4:
            self.set_icons()
            self.display_start() 
        # elif choice == 5:
        #     self.set_board_size()
        #     self.display_start()            
        elif choice == 5:
            print("Game exited.")
            return

    def set_board_size(self):
        print()
        while True:
            try:
                board_size = int(input(f"      Enter board size (Current: {len(self.board)}): "))
                if 0 < board_size <= 25:
                    self.board = [['⬜️' for _ in range(board_size)] for _ in range(board_size)]
                    self.available_moves = [i for i in range(1, (board_size ** 2) + 1)]
                    print(f"      Board size set to {board_size}. Returning to start...")
                    time.sleep(1)
                    break
            except ValueError:
                pass
            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()
            


    def play(self, mode, settings=None):
        player_was_swapped = self.current_player == 2


        if settings:
            num_games = p1_wins = p2_wins = ties = moves = sum_moves_p1_win = sum_moves_p2_win= 0

            result_boards = []
            total_time = 0
            p1_time = p1_move_count = p2_time = p2_move_count = 0


            



            while num_games < settings["num_games"]:
                game_duration = 0
                p1_move_count = 0
                p2_move_count = 0
                while True:
                    if not settings["abbreviated_output"]:
                        self.display_board()
                        self.display_available_moves()
                    
                                       
                    moves += 1

                    move_duration = self.get_move(mode, settings["abbreviated_output"])
                    if not settings["abbreviated_output"]:
                        print(f"Move duration (sec): {move_duration}")
                    total_time += move_duration
                    game_duration += move_duration
                    if self.current_player == 2:
                        p1_time += move_duration
                        p1_move_count += 1
                    else:
                        p2_time += move_duration
                        p2_move_count += 1
                    
                    
                    checks = self.check_game_over(settings["abbreviated_output"])
                    if True in checks:
                        result_boards.append(self.board)


                        if checks[0]:
                            sum_moves_p1_win += p1_move_count
                            p1_wins += 1
                        elif checks[1]:
                            sum_moves_p2_win += p2_move_count
                            p2_wins += 1
                        elif checks[2]:
                            ties += 1
                        num_games += 1
                        self.reset_variables(increment_player=player_was_swapped)
                        break

                
                if not settings["abbreviated_output"]:
                    print(f"Game {num_games} duration (moves only) (sec): {game_duration}")
                time.sleep(0.05)


            if player_was_swapped:
                p1_wins, p2_wins = p2_wins, p1_wins
                p1_time, p2_time = p2_time, p1_time
                p1_move_count, p2_move_count = p2_move_count, p1_move_count
                sum_moves_p1_win, sum_moves_p2_win = sum_moves_p2_win, sum_moves_p1_win


            p1_icon = self.player_type_to_icon[0][1]
            p2_icon = self.player_type_to_icon[1][1]

            print("\n\nCalculating stats...")
            time.sleep(1)

            print(f"\n{self.player_type_to_icon[0][0]} ({p1_icon}, P1) vs {self.player_type_to_icon[1][0]} ({p2_icon}, P2)\n")
            

            print(f"\n{num_games} game{'s' if num_games > 1 else ''} played")
            print(f"\nAverage game duration (moves only) (sec): {round(total_time / num_games, 5)}\n\n")
            print(f"{p1_icon} wins: {p1_wins} ({round(p1_wins / num_games * 100, 5)}%)")
            print(f"{p2_icon} wins: {p2_wins} ({round(p2_wins / num_games * 100, 5)}%)")
            
            print(f"   ties: {ties} ({round(ties / num_games * 100, 5)}%)\n")

            print(f"{p1_icon} average move duration (sec): {round(p1_time / p1_move_count, 5)}")
            print(f"{p2_icon} average move duration (sec): {round(p2_time / p2_move_count, 5)}\n")

            print(f"{p1_icon} average total moves to win: {0 if p1_wins == 0 else round(sum_moves_p1_win / p1_wins, 5)}")
            print(f"{p2_icon} average total moves to win: {0 if p2_wins == 0 else round(sum_moves_p2_win/ p2_wins, 5)}")
            print(f"   average moves to reach end game: {round(moves / num_games, 5)}\n")


            if settings["save_results"]:
                current_time = datetime.now().strftime("%a %b %d %Y %I:%M:%S %p")
                with open(f'Tic Tac Toe - {mode} - {current_time}.txt', 'a') as file:
                    file.write(f"{self.player_type_to_icon[0][0]} ({p1_icon}, P1) vs {self.player_type_to_icon[1][0]} ({p2_icon}, P2)\n\n")
                    file.write(f"{num_games} game{'s' if num_games > 1 else ''} played\n")
                    file.write(f"\nAverage game duration (moves only) (sec): {round(total_time / num_games, 5)}\n\n")
                    file.write(f"{p1_icon} wins: {p1_wins} ({round(p1_wins / num_games * 100, 5)}%)\n")
                    file.write(f"{p2_icon} wins: {p2_wins} ({round(p2_wins / num_games * 100, 5)}%)\n")
                    file.write(f"   ties: {ties} ({round(ties / num_games * 100, 5)}%)\n\n")
                    file.write(f"{p1_icon} average move duration (sec): {round(p1_time / p1_move_count, 5)}\n")
                    file.write(f"{p2_icon} average move duration (sec): {round(p2_time / p2_move_count, 5)}\n\n")
                    file.write(f"{p1_icon} average total moves to win: {0 if p1_wins == 0 else round(sum_moves_p1_win / p1_wins, 5)}\n")
                    file.write(f"{p2_icon} average total moves to win: {0 if p2_wins == 0 else round(sum_moves_p2_win/ p2_wins, 5)}\n")
                    file.write(f"   average moves to reach end game: {round(moves / num_games, 5)}\n")

                    file.write("\n\n")
                    for board in result_boards:
                        for row in board:
                            file.write(" ".join(map(str, row)) + "\n")
                        file.write("\n")
                print(f"\nResults saved to Tic Tac Toe - {mode} - {current_time}.txt")
                    
            
            
            if self.check_play_again():
                self.reset_variables(swap_icons=player_was_swapped)
                self.display_start()
            else:
                exit()
        else:
            while True:
                self.display_board()
                self.display_available_moves()
                move_duration = self.get_move(mode)
                if move_duration:
                        print(f"Move duration (sec): {move_duration}")
                if True in self.check_game_over():
                    if self.check_play_again():
                        self.reset_variables(swap_icons=player_was_swapped)
                        self.display_start()
                    else:
                        exit()

    def reset_variables(self, increment_player=False, swap_icons=False):
        self.board = [['⬜️' for _ in range(len(self.board))] for _ in range(len(self.board))]
        
        self.available_moves = [i for i in range(1, (len(self.board) ** 2) + 1)]

        self.random_players = [RandomPlayer() for _ in range(2)]

        if increment_player:
            self.current_player = 2
        else:
            self.current_player = 1

        if swap_icons:
            self.player_icons[0], self.player_icons[1] = self.player_icons[1], self.player_icons[0]


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
            self.set_p1("Random vs You")
            self.play(mode="Random vs You")
        elif choice == 2:
            self.player_type_to_icon[0][0] = "Random"
            self.player_type_to_icon[1][0] = "Random"
            self.play(mode="Random vs Random", settings=self.get_game_settings())


    def handle_ai_choice(self, choice):
        if choice in [1, 2, 3]:
            self.ai_players = [AIPlayer(self.player_icons[0], self.player_icons[1], "minimax"), AIPlayer(self.player_icons[1], self.player_icons[0], "minimax")]
        elif choice in [4, 5, 6]:
            self.ai_players = [AIPlayer(self.player_icons[0], self.player_icons[1], "alphabeta"), AIPlayer(self.player_icons[1], self.player_icons[0], "alphabeta")]
        elif choice == 7:
            self.ai_players = [AIPlayer(self.player_icons[0], self.player_icons[1], "minimax"), AIPlayer(self.player_icons[1], self.player_icons[0], "alphabeta")]
        if choice == 1:
            self.set_p1("AI (Minimax) vs You")
            self.play(mode="AI (Minimax) vs You")
        elif choice == 2:
            self.player_type_to_icon[0][0] = "AI (Minimax)"
            self.player_type_to_icon[1][0] = "AI (Minimax)"

            self.play(mode="AI (Minimax) vs AI (Minimax)", settings=self.get_game_settings())
        elif choice == 3:
            self.set_p1("AI (Minimax) vs Random")
            self.play(mode="AI (Minimax) vs Random", settings=self.get_game_settings())

        elif choice == 4:
            self.set_p1("AI (Alpha-beta) vs You")
            self.play(mode="AI (Alpha-beta) vs You")
        elif choice == 5:
            self.player_type_to_icon[0][0] = "AI (Alpha-beta)"
            self.player_type_to_icon[1][0] = "AI (Alpha-beta)"
            self.play(mode="AI (Alpha-beta) vs AI (Alpha-beta)", settings=self.get_game_settings())
        elif choice == 6:
            self.set_p1("AI (Alpha-beta) vs Random")
            self.play(mode="AI (Alpha-beta) vs Random", settings=self.get_game_settings())

        elif choice == 7:
            self.set_p1("AI (Minimax) vs AI (Alpha-beta)")
            self.play(mode="AI (Minimax) vs AI (Alpha-beta)", settings=self.get_game_settings())
        

    def get_game_settings(self):
        num_games = 1
        abbreviated_output = True
        save_results = False
        
        print()
        while True:
            try:
                num_games = int(input("      Number of games: "))
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
        print("   1. Random vs You") 
        print("   2. Random vs Random\n")
        while True:
            try:
                choice = int(input("   Choose an option: "))
                if 1 <= choice <= 2:
                    return choice
                
            except ValueError:
                pass

            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()

    def get_ai_choice(self):
        print("\n   AI game modes:\n")
        print("   1. AI (Minimax) vs You") 
        print("   2. AI (Minimax) vs AI (Minimax)") 
        print("   3. AI (Minimax) vs Random\n") 

        print("   4. AI (Alpha-beta) vs You") 
        print("   5. AI (Alpha-beta) vs AI (Alpha-beta)") 
        print("   6. AI (Alpha-beta) vs Random\n") 

        print("   7. AI (Minimax) vs AI (Alpha-beta)\n") 
        while True:
            try:
                choice = int(input("   Choose an option: "))
                if 1 <= choice <= 7:
                    return choice
                
            except ValueError:
                pass

            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()

    def set_p1(self, mode):
        if mode == "Random vs You":
            p1 = "You"
            p2 = "Random"
        elif mode == "AI (Minimax) vs You":
            p1 = "You"
            p2 = "AI (Minimax)"
        elif mode == "AI (Minimax) vs Random":
            p1 = "AI (Minimax)"
            p2 = "Random"

        elif mode == "AI (Alpha-beta) vs You":
            p1 = "You"
            p2 = "AI (Alpha-beta)"
            
        
        elif mode == "AI (Alpha-beta) vs Random":
            p1 = "AI (Alpha-beta)"
            p2 = "Random"
        elif mode == "AI (Minimax) vs AI (Alpha-beta)":
            p1 = "AI (Minimax)"
            p2 = "AI (Alpha-beta)"
        
        self.player_type_to_icon[0][0] = p1
        self.player_type_to_icon[1][0] = p2
      
        print()
        while True:
            try:
                choice = int(input(f"      Set P1 (1 for {p1}, 2 for {p2}): "))
                if choice == 1:
                    print(f"      P1 set to {p1}, P2 set to {p2}\n")
                    time.sleep(1)
                    return
                elif choice == 2:
                    print(f"      P1 set to {p2}, P2 set to {p1}\n")
                    time.sleep(1)

                    self.player_icons[0], self.player_icons[1] = self.player_icons[1], self.player_icons[0]
                    self.current_player = 2

                    if self.ai_players:
                        self.ai_players[0].update_icons(self.player_icons[0], self.player_icons[1])
                        self.ai_players[1].update_icons(self.player_icons[1], self.player_icons[0])

                    self.player_type_to_icon[0] = [p2, self.player_icons[1]]
                    self.player_type_to_icon[1] = [p1, self.player_icons[0]]

                    return
                
            except ValueError:
                pass

            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()
    
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
        
        p1_icon = self.player_type_to_icon[0][1]
        p2_icon = self.player_type_to_icon[1][1]

        if check_winner(p1_icon):
            if not abbreviated_output:
                print(f"\n\n{p1_icon} ({self.player_type_to_icon[0][0]}, P1) won!")
            self.display_board(abbreviated_output)
            return [True, False, False]

        elif check_winner(p2_icon):
            if not abbreviated_output:
                print(f"\n\n{p2_icon} ({self.player_type_to_icon[1][0]}, P2) won!")
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
            if len(self.board) > 3:
                row_str = " ".join(map(lambda x: '{: <4}'.format(x) if x == '⬜️' else '{: <4}'.format(x + ' '), map(str, row)))
            else:
                row_str = " ".join(map(lambda x: x if x == '⬜️' else x + ' ', map(str, row)))
            print(row_str)
        print()


    def get_move(self, mode, abbreviated_output=False):
        if not abbreviated_output:
            print(f"{self.player_icons[self.current_player - 1]}'s turn")
        while True:
            try:
                move_duration = 0
                if mode == "2 player":
                    move = int(input("Enter your move: "))
                elif mode == "Random vs You":
                    if self.current_player == 1:
                        move = int(input("Enter your move: "))
                    else:
                        if not abbreviated_output:
                            print("Random player is moving...")
                            time.sleep(1)
                        move, move_duration = self.random_players[self.current_player - 1].get_move(self.available_moves)
                        if not abbreviated_output:
                            print(f"Random player's move: {move}")
                            time.sleep(1)

                elif mode == "Random vs Random":
                    if self.current_player == 1:
                        if not abbreviated_output:
                            print("Random player 1 is moving...")
                            time.sleep(1)
                        move, move_duration = self.random_players[self.current_player - 1].get_move(self.available_moves)
                        if not abbreviated_output:
                            print(f"Random player 1's move: {move}")
                            time.sleep(1)
                    else:
                        if not abbreviated_output:
                            print("Random player 2 is moving...")
                            time.sleep(1)
                        move, move_duration = self.random_players[self.current_player - 1].get_move(self.available_moves)
                        if not abbreviated_output:
                            print(f"Random player 2's move: {move}")
                            time.sleep(1)

                elif mode == "AI (Minimax) vs You":
                    if self.current_player == 1:
                        move = int(input("Enter your move: "))
                    else:
                        if not abbreviated_output:
                            print("AI (Minimax) player is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Minimax) player's move: {move}")
                            time.sleep(1)
                
                elif mode == "AI (Minimax) vs AI (Minimax)":
                    if self.current_player == 1:
                        if not abbreviated_output:
                            print("AI (Minimax) player 1 is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Minimax) player 1's move: {move}")
                            time.sleep(1)
                    else:
                        if not abbreviated_output:
                            print("AI (Minimax) player 2 is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Minimax) player 2's move: {move}")
                            time.sleep(1)

                elif mode == "AI (Minimax) vs Random":
                    if self.current_player == 1:
                        if not abbreviated_output:
                            print("AI (Minimax) player is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Minimax) player's move: {move}")
                            time.sleep(1)
                    else:
                        if not abbreviated_output:
                            print("Random player is moving...")
                            time.sleep(1)
                        move, move_duration = self.random_players[self.current_player - 1].get_move(self.available_moves)
                        if not abbreviated_output:
                            print(f"Random player's move: {move}")
                            time.sleep(1)

                elif mode == "AI (Alpha-beta) vs You":
                    if self.current_player == 1:
                        move = int(input("Enter your move: "))
                    else:
                        if not abbreviated_output:
                            print("AI (Alpha-beta) player is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Alpha-beta) player's move: {move}")
                            time.sleep(1)

                elif mode == "AI (Alpha-beta) vs AI (Alpha-beta)":
                    if self.current_player == 1:
                        if not abbreviated_output:
                            print("AI (Alpha-beta) player 1 is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Alpha-beta) player 1's move: {move}")
                            time.sleep(1)
                    else:
                        if not abbreviated_output:
                            print("AI (Alpha-beta) player 2 is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Alpha-beta) player 2's move: {move}")
                            time.sleep(1)
                
                elif mode == "AI (Alpha-beta) vs Random":
                    if self.current_player == 1:
                        if not abbreviated_output:
                            print("AI (Alpha-beta) player is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Alpha-beta) player's move: {move}")
                            time.sleep(1)
                    else:
                        if not abbreviated_output:
                            print("Random player is moving...")
                            time.sleep(1)
                        move, move_duration = self.random_players[self.current_player - 1].get_move(self.available_moves)
                        if not abbreviated_output:
                            print(f"Random player's move: {move}")
                            time.sleep(1)
                
                elif mode == "AI (Minimax) vs AI (Alpha-beta)":
                    if self.current_player == 1:
                        if not abbreviated_output:
                            print("AI (Minimax) player is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Minimax) player's move: {move}")
                            time.sleep(1)
                    else:
                        if not abbreviated_output:
                            print("AI (Alpha-beta) player is moving...")
                            time.sleep(1)
                        move, move_duration = self.ai_players[self.current_player - 1].get_move(self.board, abbreviated_output)
                        if not abbreviated_output:
                            print(f"AI (Alpha-beta) player's move: {move}")
                            time.sleep(1)


                if move in self.available_moves:
                    self.available_moves.remove(move)
                    
                    


                    self.update_board(move)

                    self.current_player = 2 if self.current_player == 1 else 1
                    return move_duration
                
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
                icon = int(input(f"Choose an icon for player 1 (0 to skip, {len(self.available_icons) + 1} for random): "))
                if icon in range (0, len(self.available_icons) + 2):
                    if icon == 0:
                        break
                    elif icon == len(self.available_icons) + 1:
                        icon = random.randint(1, len(self.available_icons) + 1)   
                    self.available_icons.append(self.player_icons[0])
                    self.player_icons[0] = self.available_icons.pop(icon - 1)
                    self.player_type_to_icon[0][1] = self.player_icons[0]
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
                icon = int(input(f"Choose an icon for player 2 (0 to skip, {len(self.available_icons) + 1} for random): "))
                if icon in range (0, len(self.available_icons) + 2):
                    if icon == 0:
                        break
                    elif icon == len(self.available_icons) + 1:
                        icon = random.randint(1, len(self.available_icons) + 1)   

                    self.available_icons.append(self.player_icons[1])
                    self.player_icons[1] = self.available_icons.pop(icon - 1)
                    self.player_type_to_icon[1][1] = self.player_icons[1]
                    break
            except ValueError:
                pass
            except KeyboardInterrupt:
                print("\n\nGame exited.")
                exit()
            
        
        time.sleep(1)
        print(f"Player 2 icon set to {self.player_icons[1]}.")
        time.sleep(1)
        print("\nReturning to start...\n")
        time.sleep(1)

        
    def display_available_icons(self):
        for icon, number in zip(self.available_icons, range(1, len(self.available_icons) + 1)):
            time.sleep(0.05)
            print(f"{icon:<2} {number}")






    

     



TicTacToe(4).start()