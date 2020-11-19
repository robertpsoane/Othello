''' Game View Class 

controls the view for the game

'''


from Views.boardview import BoardView
from Views.discview import DiscView
from Scripts.loadgraphics import getDiscGraphics
from Scripts.pixelboardmappings import *

class GameView():

    def __init__(self, screen):
        ''' setupView - Sets up initial view
        '''
        self.screen = screen

        # Setup board view
        self.board = BoardView(self.screen)

        # Get Tile Graphics
        self.tile_graphics = getDiscGraphics()

        # Get Pixel to board mappings
        self.pixel_to_board = pixel2Board
        self.board_to_pixel = board2Pixel()
        
        
        # Setup initial four pieces
        self.placePiece('b', (32, 134))

    def placePiece(self, colour, position):
        self.new_tile = DiscView(self.screen, position, colour, self.tile_graphics)

    def update(self):
        self.new_tile.update()

    def display(self):
        self.board.display()
        self.new_tile.display()
