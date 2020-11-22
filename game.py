''' Othello.py
'''

import pygame
from Controllers.gamecontroller import GameController



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

############
def othello(game_type = 'pvp'):

    ### Setting up Screen and clock
    screen = pygame.display.set_mode(DIMS)
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    ########

    game_controller = GameController(screen, game_type)

    ### Setting up game loop
    while game_controller.run:
        # Limit frame rate
        clock.tick(MAXFPS)

        # Get/action events
        for event in pygame.event.get():
            game_controller.actionEvent(event)

        # Update States
        game_controller.update()

        # Refresh screen
        game_controller.display()
        
        pygame.display.flip()

if __name__ == '__main__':
    othello()