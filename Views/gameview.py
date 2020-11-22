''' Game View Class 

controls the view for the game

'''


from Views.backgroundview import BackgroundView
from Views.discview import DiscView
from Views.stringview import StringView
from Scripts.loadgraphics import getDiscGraphics
from Scripts.pixelboardmappings import *

board_location = 'Graphics/Board.png'

class GameView():

    def __init__(self, screen):
        ''' setupView - Sets up initial view
        '''
        self.screen = screen

        # Setup board view
        self.board = BackgroundView(self.screen, board_location)

        # Get Tile Graphics
        self.tile_graphics = getDiscGraphics()

        # Get Pixel to board mappings
        self.pixel_to_board = pixel2Board
        self.board_to_pixel = board2Pixel()

        # Setup Pieces Dictionary
        self.discs = {}

        # Setup String Views
        self.black_score = StringView(screen, 10, 25, 20, '')
        self.white_score = StringView(screen, 375, 25, 20, '')
        self.console = StringView(screen, 10, 535, 20, '>>')

    def placePiece(self, colour, position):
        pixel_position = self.board_to_pixel[position[0]][position[1]]
        new_tile = DiscView(self.screen, pixel_position, colour, self.tile_graphics)
        self.discs[str(position)] = new_tile

    def flipList(self, list_to_flip):
        for disc in list_to_flip:
            self.discs[str(disc)].flipPiece()

    def update(self):
        for key in self.discs.keys():
            self.discs[key].update()

    def display(self):
        self.board.display()
        for key in self.discs.keys():
            self.discs[key].display()
        self.black_score.display()
        self.white_score.display()
        self.console.display()
