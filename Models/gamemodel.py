''' Game Model class

'''

import copy
from Scripts.modelscripts import *

class GameModel():
    opponent = {'b':'w','w':'b'}
    
    def __init__(self):
        self.makeBoard()
        self.turn = 'b'
        self.move_list = self.generateMoveList( self.board,
                                                self.turn,
                                                self.opponent[self.turn])
        self.game_complete = False
        self.passed = False

    def getStatus(self):
        count = self.countPieces()
        status =  {
            'turn': self.turn,
            'b': count[0],
            'w': count[1],
            'complete': self.game_complete
        }
        return status

    def changeTurn(self):
        self.turn =  self.opponent[self.turn]
        self.move_list = self.generateMoveList(self.board, self.turn,
                                                    self.opponent[self.turn])

    def makeBoard(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append('.')
            board.append(row)
        board[CENTRE_LEFT][CENTRE_LEFT] = 'b'
        board[CENTRE_RIGHT][CENTRE_RIGHT] = 'b'
        board[CENTRE_LEFT][CENTRE_RIGHT] = 'w'
        board[CENTRE_RIGHT][CENTRE_LEFT] = 'w'
        self.board = board

    def getInitialSetup(self):
        initial_pieces = [
            (CENTRE_LEFT, CENTRE_LEFT, 'b'),
            (CENTRE_RIGHT, CENTRE_RIGHT, 'b'),
            (CENTRE_RIGHT, CENTRE_LEFT, 'w'),
            (CENTRE_LEFT, CENTRE_RIGHT, 'w')
        ]
        return initial_pieces

    def generateMoveList(self, board, player, opponent):
        move_list = []
        end_points = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == opponent:
                    possible_moves = self.pointMove(board, player, opponent, i, j)
                    moves, end_points_ij = possible_moves[0], possible_moves[1]
                    for move in moves:
                        grid_move = (
                            GRID['I2G']['row'][str(move[0])],
                            GRID['I2G']['col'][str(move[1])]
                        )
                        move_list.append(grid_move)
                    for end_point in end_points_ij:
                        end_points.append(end_point)
        return move_list
    
    def pointMove(self, board, player, opponent, i, j):
        point_moves = []
        end_points = []
        for i_shift in SHIFTS:
            for j_shift in SHIFTS:
                new_i, new_j = i + i_shift, j + j_shift
                if (new_i in range(8)) and (new_j in range(8)):
                    if board[new_i][new_j] == '.':
                        CP = self.canPlace(board, player, opponent, (new_i, new_j), (i, j))
                        can_move, end_point = CP[0], CP[1]
                        if can_move:
                            point_moves.append((new_i, new_j))
                            end_points.append(end_point)
        return point_moves, end_points

    def canPlace(self, board, player, opponent, empty_square, opponent_square):
        opponent_i, opponent_j = opponent_square[0], opponent_square[1]
        empty_i, empty_j = empty_square[0], empty_square[1]
        step = (opponent_i - empty_i, opponent_j - empty_j)
        test_i, test_j = empty_i + step[0], empty_j + step[1]
        while (test_i in range(8)) and (test_j in range(8)):
            if board[test_i][test_j] == '.':
                break
            if board[test_i][test_j] == player:
                return (True, (test_i, test_j))
            test_i, test_j = test_i + step[0], test_j + step[1]
        return (False, [])

    def makeMove(self, board, player, opponent, move):
        board = copy.deepcopy(board)
        index_move = (GRID['G2I']['row'][move[0]], GRID['G2I']['col'][move[1]])
        i, j = index_move[0], index_move[1]
        # Placing players piece
        board[i][j] = player
        # Taking pieces
        board, taken_list = self.takePieces(board, player, opponent, index_move)
        return board, taken_list

    def listTakenPieces(self, board, player, opponent, move):
        i, j = move[0], move[1]
        taken = []
        for i_shift in SHIFTS:
            for j_shift in SHIFTS:
                shift = (i_shift, j_shift)
                new_i, new_j = i + i_shift, j + j_shift
                potentially_taken = []
                while (new_i in range(8)) and (new_j in range(8)):
                    if board[new_i][new_j] == opponent:
                        potentially_taken.append((new_i, new_j))
                        # Carrying on in the shift direction until reach a player
                        # piece
                        new_i, new_j = new_i + shift[0], new_j + shift[1]
                    elif board[new_i][new_j] == player:
                        taken.append(potentially_taken)
                        break
                    elif board[new_i][new_j] == '.':
                        break
        taken_list = []
        for takes in taken:
            for el in takes:
                taken_list.append(el)
        return taken_list

    def takePieces(self, board, player, opponent, move):
        taken_list = self.listTakenPieces(board, player, opponent, move)
        if taken_list == []:
            print('broken')
        for piece in taken_list:
            i, j = piece[0], piece[1]
            board[i][j] = player
        return board, taken_list

    def tryTake(self, move):
        index_move = (GRID['I2G']['row'][str(move[0])], GRID['I2G']['col'][str(move[1])])
        if (index_move in self.move_list) == False:
            return False, ()
        new_board, taken_pieces = self.makeMove(self.board,
                                                    self.turn,
                                                    self.opponent[self.turn],
                                                    index_move)
        self.passed = False
        self.board = new_board
        self.changeTurn()
        self.checkWinConditions()
        return True, taken_pieces
    
    def checkWinConditions(self):
        if (self.passed == True) and len(self.move_list) == 0:
            self.game_complete = True
        elif len(self.move_list) == 0:
            self.passed = True
            self.changeTurn()
            self.checkWinConditions()

    def countPieces(self):
        b = 0
        w = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'b':
                    b += 1
                elif self.board[i][j] == 'w':
                    w += 1
        return b, w
