''' Othello.py
'''

import pygame
from Controllers.menucontroller import MenuController


############
# Global Variables
COLOUR = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

WIDTH = 450
HEIGHT = 545
DIMS = WIDTH, HEIGHT

MAXFPS = 60

GAME_NAME = 'Othello v2'



### Setting up Screen and clock
screen = pygame.display.set_mode(DIMS)
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()
########

menu_controller = MenuController(screen)

### Setting up game loop
while menu_controller.run:
    # Limit frame rate
    clock.tick(MAXFPS)

    # Get/action events
    for event in pygame.event.get():
        menu_controller.actionEvent(event)

    # Update screen
    menu_controller.update()

    # Refresh screen
    menu_controller.display()
    
    pygame.display.flip()
