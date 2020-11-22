''' menu controller

controller for start menu

'''

import pygame
import webbrowser
from game import othello
from Views.startview import *

class MenuController():
    def __init__(self, screen):
        self.screen = screen
        self.run = True
        self.view = StartView(self.screen)     
        self.setupButtonData()
        self.highlighted_button = False

    def actionEvent(self, event):
        if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                self.run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.buttonPressed(self.highlighted_button)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            checked_button = self.checkOnButton(event.pos)
            if checked_button[0]:
                self.buttonPressed(checked_button[1])

    def buttonPressed(self, button):
        if button == False:
            return
        elif button == 'help':
            webbrowser.open('https://github.com/robertpsoane/Othello',
                            new=2)
        elif button == 'pvp':
            othello('pvp')
        elif button == 'white':
            othello('w')
        elif button == 'black':
            othello('b')

    def update(self):

        # Checking whether to update highlighted button
        mouse_position = pygame.mouse.get_pos()
        button_check = self.checkOnButton(mouse_position)
        if button_check[0]:
            new_highlight = button_check[1]
            if new_highlight != self.highlighted_button:
                self.unhighlight(self.highlighted_button)
                self.highlighted_button = new_highlight
                self.highlight(self.highlighted_button)

    def checkOnButton(self, position):
        x, y = position[0], position[1]
        for button_key in self.buttons.keys():
            x0, x1 = self.buttons[button_key][0], self.buttons[button_key][1]
            y0, y1 = self.buttons[button_key][2], self.buttons[button_key][3]
            if x < x1 and x > x0:
                if y < y1 and y > y0:
                    return True, button_key
        return (False,)
                    

    def highlight(self, button):
        self.view.button_objs[button].hoverOn()

    def unhighlight(self, button):
        if button == False:
            return
        self.view.button_objs[button].hoverOff()

    def display(self):
        self.view.display()

    def setupButtonData(self):
        button_dicts = self.view.getButtonData()
        self.buttons = {}
        for button in button_dicts:
            x0 = button['position'][0] - (button['dims'][0] // 2)
            y0 = button['position'][1] - (button['dims'][1] // 2)
            x1, y1 = x0 + button['dims'][0], y0 + button['dims'][1]
            button_key = button['return']
            self.buttons[button_key] = [x0, x1, y0, y1]


