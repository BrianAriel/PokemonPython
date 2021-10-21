import pygame
import os
from pygame.locals import *


class Button:
    def __init__(self, x, y, width, height, text, action):
        self.action = action
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.state = 1
        pygame.font.init()
        self.font = pygame.font.Font(os.path.join("C:/Users/brian/PycharmProjects/PokemonPython/res/font.ttf"), 15)
        self.rect = pygame.Rect(x, y, width, height)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.action()

    def disable(self):
        self.state = 0

    def enable(self):
        self.state = 1

    def render(self, game):
        color = "black"
        if self.state == 0:
            color = "gray"
        pygame.draw.rect(game.screen, Color(color), self.rect, 2)
        text_surface = self.font.render(self.text, False, Color(color))
        text_size = text_surface.get_rect().size
        left_padding = (self.width - text_size[0]) / 2
        top_padding = (self.height - text_size[1]) / 2
        game.screen.blit(text_surface, (self.x + left_padding, self.y + top_padding))
