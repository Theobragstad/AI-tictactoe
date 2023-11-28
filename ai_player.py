# import time

# class AIPlayer:
#     def __init__(self, ai_icon, algorithm_type):
#         self.ai_icon = ai_icon
#         self.algorithm_type = algorithm_type

#     def get_move(self, board, abbreviated_output):
#         start_time = time.time()
#         if self.algorithm_type == "minimax":
#             _, move = self.minimax(board, self.ai_icon)
#             end_time = time.time()  # Record the end time
#             duration = end_time - start_time 
#             if not abbreviated_output:
#                 print(f"Time taken: {duration}")
#             return move
#         elif self.algorithm_type == "alphabeta":
#             _, move = self.minimax_alphabeta(board, self.ai_icon)
#             end_time = time.time()  # Record the end time
#             duration = end_time - start_time 
#             if not abbreviated_output:
#                 print(f"Time taken: {duration}")
#             return move
#         else:
#             raise ValueError("Invalid algorithm type")


#     def minimax(self, board, player_marker, depth=0):
#         if self.check_winner(board, '❌'):
#             return -1, None  # The AI (❌) loses
#         elif self.check_winner(board, '⭕'):
#             return 1, None   # The AI (⭕) wins
#         elif self.is_board_full(board):
#             return 0, None   # It's a tie

#         scores = []

#         for move in self.get_available_moves(board):
#             new_board = self.make_move(board, move, player_marker)
#             score, _ = self.minimax(new_board, '⭕' if player_marker == '❌' else '❌', depth + 1)
#             scores.append(score)

#         if player_marker == '⭕':
#             best_score_index = scores.index(max(scores))
#             return scores[best_score_index], self.get_available_moves(board)[best_score_index]
#         else:
#             best_score_index = scores.index(min(scores))
#             return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        
    
#     def minimax_alphabeta(self, board, player_marker, depth=0, alpha=float('-inf'), beta=float('inf')):
#         if self.check_winner(board, '❌'):
#             return -1, None  # The AI (❌) loses
#         elif self.check_winner(board, '⭕'):
#             return 1, None   # The AI (⭕) wins
#         elif self.is_board_full(board):
#             return 0, None   # It's a tie

#         scores = []

#         for move in self.get_available_moves(board):
#             new_board = self.make_move(board, move, player_marker)
#             score, _ = self.minimax_alphabeta(new_board, '⭕' if player_marker == '❌' else '❌', depth + 1, alpha, beta)
#             scores.append(score)

#             if player_marker == '⭕':
#                 alpha = max(alpha, score)
#             else:
#                 beta = min(beta, score)

#             if alpha >= beta:
#                 break  # Prune the remaining branches

#         if player_marker == '⭕':
#             best_score_index = scores.index(max(scores))
#             return scores[best_score_index], self.get_available_moves(board)[best_score_index]
#         else:
#             best_score_index = scores.index(min(scores))
#             return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        

#     def get_available_moves(self, board):
#         return [move for move in range(1, len(board) ** 2 + 1) if board[(move - 1) // len(board)][(move - 1) % len(board)] == '⬜️']

#     def make_move(self, board, move, player_marker):
#         new_board = [row[:] for row in board]
#         new_board[(move - 1) // len(board)][(move - 1) % len(board)] = player_marker
#         return new_board

#     def is_board_full(self, board):
#         return all(element != '⬜️' for row in board for element in row)

#     def check_winner(self, board, marker):
#         n = len(board)

#         # Check rows and columns
#         for i in range(n):
#             if all(board[i][j] == marker for j in range(n)) or all(board[j][i] == marker for j in range(n)):
#                 return True

#         # Check diagonals
#         if all(board[i][i] == marker for i in range(n)) or all(board[i][n - 1 - i] == marker for i in range(n)):
#             return True

#         return False

#     def update_icons(self, ai_icon):
#         self.ai_icon = ai_icon






import time

class AIPlayer:
    def __init__(self, ai_icon, opp_icon, algorithm_type):
        self.ai_icon = ai_icon
        self.opp_icon = opp_icon
        self.algorithm_type = algorithm_type

    def get_move(self, board, abbreviated_output):
        start_time = time.time()
        if self.algorithm_type == "minimax":
            _, move = self.minimax(board, self.ai_icon)
            end_time = time.time()  # Record the end time
            duration = end_time - start_time 
            if not abbreviated_output:
                print(f"Time taken: {duration}")
            return move
        elif self.algorithm_type == "alphabeta":
            _, move = self.minimax_alphabeta(board, self.ai_icon)
            end_time = time.time()  # Record the end time
            duration = end_time - start_time 
            if not abbreviated_output:
                print(f"Time taken: {duration}")
            return move
        else:
            raise ValueError("Invalid algorithm type")


    def minimax(self, board, player_icon, depth=0):
        if self.check_winner(board, self.opp_icon):
            return -1, None  # The AI (❌) loses
        elif self.check_winner(board, self.ai_icon):
            return 1, None   # The AI (⭕) wins
        elif self.is_board_full(board):
            return 0, None   # It's a tie

        scores = []

        for move in self.get_available_moves(board):
            new_board = self.make_move(board, move, player_icon)
            score, _ = self.minimax(new_board, self.ai_icon if player_icon == self.opp_icon else self.opp_icon, depth + 1)
            scores.append(score)

        if player_icon == self.ai_icon:
            best_score_index = scores.index(max(scores))
            return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        else:
            best_score_index = scores.index(min(scores))
            return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        
    
    def minimax_alphabeta(self, board, player_icon, depth=0, alpha=float('-inf'), beta=float('inf')):
        if self.check_winner(board, self.opp_icon):
            return -1, None  # The AI (❌) loses
        elif self.check_winner(board, self.ai_icon):
            return 1, None   # The AI (⭕) wins
        elif self.is_board_full(board):
            return 0, None   # It's a tie

        scores = []

        for move in self.get_available_moves(board):
            new_board = self.make_move(board, move, player_icon)
            score, _ = self.minimax_alphabeta(new_board, self.ai_icon if player_icon == self.opp_icon else self.opp_icon, depth + 1, alpha, beta)
            scores.append(score)

            if player_icon == self.ai_icon:
                alpha = max(alpha, score)
            else:
                beta = min(beta, score)

            if alpha >= beta:
                break  # Prune the remaining branches

        if player_icon == self.ai_icon:
            best_score_index = scores.index(max(scores))
            return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        else:
            best_score_index = scores.index(min(scores))
            return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        

    def get_available_moves(self, board):
        return [move for move in range(1, len(board) ** 2 + 1) if board[(move - 1) // len(board)][(move - 1) % len(board)] == '⬜️']

    def make_move(self, board, move, player_icon):
        new_board = [row[:] for row in board]
        new_board[(move - 1) // len(board)][(move - 1) % len(board)] = player_icon
        return new_board

    def is_board_full(self, board):
        return all(element != '⬜️' for row in board for element in row)

    def check_winner(self, board, marker):
        n = len(board)

        # Check rows and columns
        for i in range(n):
            if all(board[i][j] == marker for j in range(n)) or all(board[j][i] == marker for j in range(n)):
                return True

        # Check diagonals
        if all(board[i][i] == marker for i in range(n)) or all(board[i][n - 1 - i] == marker for i in range(n)):
            return True

        return False

    def update_icons(self, ai_icon, opp_icon):
        self.ai_icon = ai_icon
        self.opp_icon = opp_icon