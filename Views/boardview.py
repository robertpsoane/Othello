''' Board View class
'''

import pygame


# Board Location - to go in JSON
board_location = 'Graphics/Board.png'

class BoardView():
    
    def __init__(self, screen):
        self.screen = screen
        self.setupBoardImage()
        


    def setupBoardImage(self):
        width, height = self.screen.get_width(), self.screen.get_height()
        image = pygame.image.load(board_location)
        self.board_img = pygame.transform.scale(image,(width, height))
        self.board_rect = self.board_img.get_rect()
        self.board_rect.topleft = (0, 0)

    
    def display(self):
        self.screen.blit(self.board_img, self.board_rect)