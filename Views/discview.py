''' Disc View class
'''

import pygame

class DiscView(pygame.sprite.Sprite):
    ANIMATION_SEQUENCE = {'b':('+',8),'w':('-',0)}
    FRAME_UPDATE = 5

    def __init__(self, screen, position, colour, sprites):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = sprites
        self.colour = colour
        self.screen = screen

        # Setting Up Image
        self.current_frame = self.getCurrentFrame()
        self.current_image = self.sprites[self.current_frame]
        self.rect = self.current_image.get_rect()
        self.rect.center = position
        self.display()
        self.target_frame = self.current_frame

    def getCurrentFrame(self):
        if self.colour == 'b':
            return 0
        else:
            return 8

    def flipPiece(self):
        if self.colour == 'w':
            self.colour = 'b'
        else:
            self.colour = 'w'
        self.target_frame = self.ANIMATION_SEQUENCE[self.colour][1]
        self.update_count = 0

    def update(self):
        if self.target_frame == self.current_frame:
            return
        if self.update_count < self.FRAME_UPDATE:
            return
        self.update_count = 0
        self.incrementFrame()
        self.current_image = self.sprites[self.current_frame]

    def incrementFrame(self):
        if self.ANIMATION_SEQUENCE[self.colour][0] == '+':
            self.current_frame += 1
        else:
            self.current_frame -= 1

    def display(self):
        self.screen.blit(self.sprites[self.current_frame], self.rect)
        


 

