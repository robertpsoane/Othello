''' Game Controller class
'''

import pygame

from Views.gameview import GameView



class GameController():
    
    def __init__(self, screen):
        # Storing useful variables to controller
        self.screen = screen

        self.setupModel()
        self.game_view = GameView(screen)

        self.run = True


    def setupModel(self):
        pass

    def setupStartPieces(self):
        self.placePiece('b', (150, 150))

    

    def actionEvent(self, event):
        if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                self.run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            event_x = event.pos[0]
            event_y = event.pos[1]
            pixel_to_board = self.game_view.pixel_to_board(event_x, event_y)
            if pixel_to_board[0]:
                print(pixel_to_board)
            else:
                print('out of range')

    def update(self):
        self.game_view.update()

    def display(self):
        self.game_view.display()


