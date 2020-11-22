''' AI Player Model

Code for the AI player

'''

import random
import copy
from Scripts.modelscripts import *

class AIPlayer():
    GRADING_STRATEGY = makeGradingStrategy()
    def __init__(self, side, game):
        self.side = side
        if self.side == 'b':
            self.opponent = 'w'
        else:
            self.opponent = 'b'
        self.game = game
        self.depth = 5

    def getMoveInput(self, move_list, board):
        ''' computerPlayer
        This function attempts to compute an optimal move for the computer to 
        play, using a minimax search up to a given depth (default = 5).
        The function aims to achieve the following:
        - Maximise number of moves for computer
        - Minimise number of moves for player
        '''
        min_max_board = copy.deepcopy(board)
        depth = self.depth
        score, move = self.minimax(min_max_board, self.side, self.opponent, True, 
                                depth, -999, 999)
        #print(score)
        if move != ():
            grid_move = (
                        GRID['G2I']['row'][str(move[0])],
                        GRID['G2I']['col'][str(move[1])]
                        )
            return grid_move
        else:
            return 'pass'
    
    def minimax(self, board, player, opponent, maximising, depth, alpha, beta):
        super_move = ()
        if depth == 0:
            return self.scoreBoard(board, player, opponent), super_move
        
        if maximising:
            # players turn
            max_eval = -999999
            moves = self.game.generateMoveList(board, player, opponent)
            random.shuffle(moves)
            if len(moves) == 0:
                next_layer, M = self.minimax(board, player, opponent, False, depth - 1, alpha, beta)
            for move in moves:
                # Copy board
                old_board = copy.deepcopy(board)

                # Make chosen move
                board, taken_list = self.game.makeMove(board, player, opponent, move)
                
                # Recursively call minimax
                next_layer, M = self.minimax(board, player, opponent, False, depth - 1, alpha, beta)

                # Calculate corner addition, subtraction
                #next_layer += numCorner(board, player) * depth
                #next_layer -= numCorner(board, opponent) * depth

                # Resetting board
                board = old_board
                
                # Updating score based on minimax
                if next_layer > max_eval:
                    max_eval = next_layer
                    super_move = move
                alpha = max(alpha, next_layer)
                if beta <= alpha:
                    break
            return max_eval, super_move
        else:
            min_eval = 999999
            moves = self.game.generateMoveList(board, opponent, player)
            random.shuffle(moves)
            if len(moves) == 0:
                next_layer, M = self.minimax(board, player, opponent, True, depth - 1, alpha, beta)
            for move in moves:
                # Copy board
                old_board = copy.deepcopy(board)

                # Make chosen move
                board, taken_list = self.game.makeMove(board, opponent, player, move)

                # Recursively call minimax
                next_layer, M = self.minimax(board, player, opponent, True, depth - 1, alpha, beta)

                # Calculate corner addition, subtraction
                #next_layer -= numCorner(board, player) * depth
                #next_layer += numCorner(board, opponent) * depth

                # Resetting board
                board = old_board

                # Updating score based on minimax
                if next_layer < min_eval:
                    min_eval = next_layer
                    super_move = move
                beta = min(beta, next_layer)
                if beta <= alpha:
                    break
            return min_eval, super_move

    def scoreBoard(self, board, player, opponent):
        player_score = len(self.game.generateMoveList(board, player, opponent))*3
        opponent_score = len(self.game.generateMoveList(board, opponent, player))*3

        if (player_score == 0) and (opponent_score == 0):
            # Have reached game end
            b, w = self.countPieces(board)
            if b > w: 
                winner = 'b'
            if b < w:
                winner = 'w'
            else:
                winner = 'tie'
            winner = winner[0]
            if winner[0].lower() == player:
                return 300
            elif winner[0].lower() == opponent:
                return -300
            else:
                return 0

        for i in range(self.game.DIMS):
            for j in range(self.game.DIMS):
                if board[i][j] == player:
                    player_score += self.GRADING_STRATEGY[i][j]
                if board[i][j] == opponent:
                    opponent_score += self.GRADING_STRATEGY[i][j]

        return player_score - opponent_score
    
    def numCorner(self, board, colour):
        n_corners = 0
        for corner in self.game.CORNERS:
            if board[corner[0]][corner[1]] == colour:
                n_corners += 1
        return n_corners

    def countPieces(self, board):
        ''' countPieces

        Count number of pieces on board of each player
        '''
        b = 0
        w = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'b':
                    b += 1
                elif board[i][j] == 'w':
                    w += 1
        return b, w