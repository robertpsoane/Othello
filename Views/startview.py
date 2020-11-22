''' Start View Class
'''

import pygame
from Views.backgroundview import BackgroundView
from Views.stringview import StringView
import copy

menu_background_location = 'Graphics/Menu/Menu.png'

blank_button_location = 'Graphics/Menu/BlankButton.png'

blank_button = pygame.image.load(blank_button_location)



class StartView():
    
    def __init__(self, screen):
        self.screen = screen

        # Setup board view
        self.background = BackgroundView(self.screen, menu_background_location)
        self.buttons = []

        width, height = self.screen.get_width(), self.screen.get_height()
        button_width = 2 * width // 5
        button_height = height // 8
        x_1, x_2 = width // 4, 3 * width // 4
        y_1, y_2 = 10 * height // 13, 12 * height // 13

        self.button_data = [
            {
                'position': (x_1, y_1),
                'dims': (button_width, button_height),
                'text': 'Play as Black',
                'return': 'black'
            },
            {
                'position': (x_2, y_1),
                'dims': (button_width, button_height),
                'text': 'Play as White',
                'return': 'white'
            },
            {
                'position': (x_1, y_2),
                'dims': (button_width, button_height),
                'text': 'Play PvP',
                'return': 'pvp'
            },  
            {
                'position': (x_2, y_2),
                'dims': (button_width, button_height),
                'text': 'Help',
                'return': 'help'
            }
        ]
        self.button_objs = {}

        for button in self.button_data:
            self.makeButton(button)
    
    def makeButton(self, button_dict):
        position = button_dict['position']
        dims = button_dict['dims']
        text = button_dict['text']
        button = ButtonView(self.screen, position, dims, text)
        self.button_objs[button_dict['return']] = button
        #self.buttons.append(button)

    def getButtonData(self):
        return self.button_data

    def display(self):
        self.background.display()
        for button_key in self.button_objs.keys():
            self.button_objs[button_key].display()


class ButtonView():
    def __init__(self, screen, position, dims, text):
        self.screen = screen
        
        self.text = text
        self.width, self.height = dims[0], dims[1]
        self.x, self.y = position[0], position[1]
        self.makeButton()
    
    def makeButton(self):
        self.img = blank_button
        self.img = pygame.transform.scale(self.img,(self.width, self.height))
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.text_obj = StringView( self.screen,self.x, self.y,
                                    2 * self.height // 5, self.text)

    def hoverOn(self):
        self.text_obj.changeColour((255,186,0))

    def hoverOff(self):
        self.text_obj.changeColour((255,255,255))

    def display(self):
        self.screen.blit(self.img, self.rect)
        self.text_obj.display()
