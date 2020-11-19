''' Game Controller class
'''

from Views.boardview import BoardView

class GameController():
    
    def __init__(self, screen):
        # Storing useful variables to controller
        self.screen = screen

        self.setupModel()
        self.setupView()
           

    def setupView(self):
        ''' setupView - Sets up initial view
        '''
        # Setup board view
        self.board = BoardView(self.screen)

        # Setup initial four pieces

    def setupModel(self):
        pass

    def display(self):
        self.board.display()

