''' Game Controller class
'''

import pygame

from Views.gameview import GameView
from Models.gamemodel import GameModel

class GameController():
    
    def __init__(self, screen, game_type):
        # Storing useful variables to controller
        self.screen = screen
        self.game_type = game_type
        self.setupModelView()        
        self.run = True
        

    def setupModelView(self):
        # Instantiate game view and game model
        self.game_view = GameView(self.screen)
        self.game_model = GameModel()
        self.setupStartPieces()
        self.getStatus()
        self.changeStrings()
        if self.game_type == 'b':
            print('b')
        elif self.game_type == 'w':
            print('w')

    def setupStartPieces(self):
        initial_setup = self.game_model.getInitialSetup()
        for piece in initial_setup:
            colour = piece[2]
            position = (piece[0], piece[1])
            self.game_view.placePiece(colour, position)

    def getStatus(self):
        self.status = self.game_model.getStatus()

    def changeStrings(self):
        black_score = self.status['b']
        white_score = self.status['w']
        black_score_str = f'Black: {black_score}'
        white_score_str = f'White: {white_score}'
        self.game_view.black_score.changeText(black_score_str)
        self.game_view.white_score.changeText(white_score_str)
        if self.status['complete'] == True:
            if black_score > white_score:
                winner = 'Black Won'
            elif white_score > black_score:
                winner = 'White Won'
            else:
                winner = 'Tie'
            console_string = f'>> Game Complete: {winner}!'
            self.gameComplete()
        else:
            if self.status['turn'] == 'b':
                player_turn = 'Black'
            else:
                player_turn = 'White'
            console_string = f'>> {player_turn}\'s Turn...'
        self.game_view.console.changeText(console_string)

    def gameComplete(self):
        pass

    def actionEvent(self, event):
        if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                self.run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            event_x = event.pos[0]
            event_y = event.pos[1]
            square_reference = self.game_view.pixel_to_board(event_x, event_y)
            if square_reference[0]:
                self.tryMakeMove((square_reference[1],square_reference[2]))

    def tryMakeMove(self, move):
        attempted_move, taken = self.game_model.tryTake(move)
        if attempted_move:
            turn = self.game_model.opponent[self.game_model.turn]
            self.game_view.placePiece(turn, move)
            self.game_view.flipList(taken)
            self.getStatus()
            self.changeStrings()

    def update(self):
        model_status = self.game_model.getStatus()
        self.game_view.update()

    def display(self):
        self.game_view.display()


