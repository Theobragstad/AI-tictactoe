# import time

# class AIPlayer:
#     def __init__(self, ai_icon, opp_icon, algorithm_type):
#         self.ai_icon = ai_icon
#         self.opp_icon = opp_icon
#         self.algorithm_type = algorithm_type

#     def get_move(self, board, abbreviated_output):
#         start_time = time.time()
#         if self.algorithm_type == "minimax":
#             _, move = self.minimax(board, self.ai_icon)
#         elif self.algorithm_type == "alphabeta":
#             _, move = self.minimax_alphabeta(board, self.ai_icon)
#         else:
#             raise ValueError("Invalid algorithm type")
#         end_time = time.time()
#         return move, end_time - start_time


#     def minimax(self, board, player_icon, depth=0):
#         if self.check_winner(board, self.opp_icon):
#             return -1, None  
#         elif self.check_winner(board, self.ai_icon):
#             return 1, None   
#         elif self.is_board_full(board):
#             return 0, None  

#         scores = []

#         for move in self.get_available_moves(board):
#             new_board = self.make_move(board, move, player_icon)
#             score, _ = self.minimax(new_board, self.ai_icon if player_icon == self.opp_icon else self.opp_icon, depth + 1)
#             scores.append(score)

#         if player_icon == self.ai_icon:
#             best_score_index = scores.index(max(scores))
#             return scores[best_score_index], self.get_available_moves(board)[best_score_index]
#         else:
#             best_score_index = scores.index(min(scores))
#             return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        
    
#     def minimax_alphabeta(self, board, player_icon, depth=0, alpha=float('-inf'), beta=float('inf')):
#         if self.check_winner(board, self.opp_icon):
#             return -1, None  
#         elif self.check_winner(board, self.ai_icon):
#             return 1, None   
#         elif self.is_board_full(board):
#             return 0, None  

#         scores = []

#         for move in self.get_available_moves(board):
#             new_board = self.make_move(board, move, player_icon)
#             score, _ = self.minimax_alphabeta(new_board, self.ai_icon if player_icon == self.opp_icon else self.opp_icon, depth + 1, alpha, beta)
#             scores.append(score)

#             if player_icon == self.ai_icon:
#                 alpha = max(alpha, score)
#             else:
#                 beta = min(beta, score)

#             if alpha >= beta:
#                 break  

#         if player_icon == self.ai_icon:
#             best_score_index = scores.index(max(scores))
#             return scores[best_score_index], self.get_available_moves(board)[best_score_index]
#         else:
#             best_score_index = scores.index(min(scores))
#             return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        

#     def get_available_moves(self, board):
#         return [move for move in range(1, len(board) ** 2 + 1) if board[(move - 1) // len(board)][(move - 1) % len(board)] == '⬜️']

#     def make_move(self, board, move, player_icon):
#         new_board = [row[:] for row in board]
#         new_board[(move - 1) // len(board)][(move - 1) % len(board)] = player_icon
#         return new_board

#     def is_board_full(self, board):
#         return all(element != '⬜️' for row in board for element in row)

#     def check_winner(self, board, marker):
#         n = len(board)

#         for i in range(n):
#             if all(board[i][j] == marker for j in range(n)) or all(board[j][i] == marker for j in range(n)):
#                 return True

#         if all(board[i][i] == marker for i in range(n)) or all(board[i][n - 1 - i] == marker for i in range(n)):
#             return True

#         return False

#     def update_icons(self, ai_icon, opp_icon):
#         self.ai_icon = ai_icon
#         self.opp_icon = opp_icon






import time

class AIPlayer:
    def __init__(self, ai_icon, opp_icon, algorithm_type):
        self.ai_icon = ai_icon
        self.opp_icon = opp_icon
        self.algorithm_type = algorithm_type

    def get_move(self, board, abbreviated_output, max_depth=3):  # Add max_depth parameter with a default value
        start_time = time.time()
        if self.algorithm_type == "minimax":
            _, move = self.minimax(board, self.ai_icon, max_depth=max_depth)
        elif self.algorithm_type == "alphabeta":
            _, move = self.minimax_alphabeta(board, self.ai_icon, max_depth=max_depth)
        else:
            raise ValueError("Invalid algorithm type")
        end_time = time.time()
        return move, end_time - start_time


    def minimax(self, board, player_icon, depth=0, max_depth=float('inf')):  # Add max_depth parameter
        if self.check_winner(board, self.opp_icon):
            return -1, None  
        elif self.check_winner(board, self.ai_icon):
            return 1, None   
        elif self.is_board_full(board):
            return 0, None  

        scores = []

        for move in self.get_available_moves(board):
            new_board = self.make_move(board, move, player_icon)
            if depth < max_depth:  # Add this line to limit the depth
                score, _ = self.minimax(new_board, self.ai_icon if player_icon == self.opp_icon else self.opp_icon, depth + 1, max_depth)
            else:
                score, _ = 0, None  # This line assumes a draw when the depth limit is reached
            scores.append(score)

        if player_icon == self.ai_icon:
            best_score_index = scores.index(max(scores))
            return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        else:
            best_score_index = scores.index(min(scores))
            return scores[best_score_index], self.get_available_moves(board)[best_score_index]
        
    
    def minimax_alphabeta(self, board, player_icon, depth=0, alpha=float('-inf'), beta=float('inf'), max_depth=float('inf')):  # Add max_depth parameter
        if self.check_winner(board, self.opp_icon):
            return -1, None  
        elif self.check_winner(board, self.ai_icon):
            return 1, None   
        elif self.is_board_full(board):
            return 0, None  

        scores = []

        for move in self.get_available_moves(board):
            new_board = self.make_move(board, move, player_icon)
            if depth < max_depth:  # Add this line to limit the depth
                score, _ = self.minimax_alphabeta(new_board, self.ai_icon if player_icon == self.opp_icon else self.opp_icon, depth + 1, alpha, beta, max_depth)
            else:
                score, _ = 0, None  # This line assumes a draw when the depth limit is reached
            scores.append(score)

            if player_icon == self.ai_icon:
                alpha = max(alpha, score)
            else:
                beta = min(beta, score)

            if alpha >= beta:
                break  

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

        for i in range(n):
            if all(board[i][j] == marker for j in range(n)) or all(board[j][i] == marker for j in range(n)):
                return True

        if all(board[i][i] == marker for i in range(n)) or all(board[i][n - 1 - i] == marker for i in range(n)):
            return True

        return False

    def update_icons(self, ai_icon, opp_icon):
        self.ai_icon = ai_icon
        self.opp_icon = opp_icon