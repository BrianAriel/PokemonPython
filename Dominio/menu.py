import pygame
from functools import partial
from button import Button


class Menu:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.rect = pygame.Rect(0, 400, 160*4, 144*4)
        self.state = 0
        self.mainButtons = [
            Button(160 * 2, 400, 150, 40, "Luchar", partial(self.change_menu_state, new_state=1)),
            Button(160 * 2, 450, 150, 40, "Pokemon", partial(self.change_menu_state, new_state=2)),
            Button(160 * 3, 400, 150, 40, "Mochila", partial(self.change_menu_state, new_state=3)),
            Button(160 * 3, 450, 150, 40, "Huir", partial(self.change_menu_state, new_state=4))
        ]
        self.attackButtons = []

    def handle_event(self, event, game):
        for button in self.mainButtons:
            button.handle_event(event)
        if self.state == 1:
            if len(self.attackButtons) == 0:
                for idx, attack in enumerate(game.pokemon1.attacks):
                    function_turn = partial(game.make_turn, index=idx)
                    self.attackButtons.append(
                        Button(idx * 160, 400, 150, 40, attack.name, function_turn)
                    )
            for button in self.attackButtons:
                button.handle_event(event)

    def change_menu_state(self, new_state):
        if self.state == 1 and new_state != 1:
            # if any button is clicked when LUCHAR mode is ON, return
            self.state = 0
            for button in self.mainButtons:
                button.enable()
        else:
            self.state = new_state
            for button in self.mainButtons:
                button.disable()

    def render(self, game):
        for button in self.mainButtons:
            button.render(game)
        if self.state == 1:
            # Now we draw attack buttons
            for button in self.attackButtons:
                button.render(game)
