''' Load Graphics script

Script to load grpahics for othello discs.  This is run when DiscView is 
imported so that key graphics are loaded once globally at the beginning of the
game

'''

import pygame

DISC_SPRITE_SHEET_LOCATION = 'Graphics/DiscSpriteSheet.png'



def getDiscGraphics():
    ''' getDiscGraphics - Sets up a SpriteSheet object loading the disc sprite
    sheet.  Returns list of 9 graphics.  Index 0 being a stationary black 
    disc, index 8 being a stationary white disc, and each index in between
    being a frame in the flip animation.
    '''
    sprite_sheet = SpriteSheet(DISC_SPRITE_SHEET_LOCATION)
    
    sprites = []
    for y in range(2):
        for x in range(5):
        
            ith_sprite = sprite_sheet.image_at((y, x), (500, 500), (0, 255, 0))
            
            scaled_size = (50, 50) 

            scaled = pygame.transform.scale(
                ith_sprite,
                scaled_size
            )
            sprites.append(scaled)
    return sprites[:-1]


class SpriteSheet():
    ''' 
    Sprite Sheet Processing class from https://www.pygame.org/wiki/Spritesheet
    '''
    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, position, size, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.

        # Position is a grid position, we need to multiply that by size to 
        # extract correct position
        y = position[0] * size[0]
        x = position[1] * size[1]
        rectangle = (x, y, size[0], size[1])
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

        