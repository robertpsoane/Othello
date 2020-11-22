''' Board View class
'''

import pygame



class BackgroundView():
    
    def __init__(self, screen, img_location):
        self.screen = screen
        self.img_location = img_location
        self.setupBoardImage()
        

    def setupBoardImage(self):
        width, height = self.screen.get_width(), self.screen.get_height()
        image = pygame.image.load(self.img_location)
        self.img = pygame.transform.scale(image,(width, height))
        self.rect = self.img.get_rect()
        self.rect.topleft = (0, 0)

    
    def display(self):
        self.screen.blit(self.img, self.rect)