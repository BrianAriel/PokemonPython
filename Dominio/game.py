import pygame
from pygame.locals import *
from constants import *
from functools import partial
from pokemon import *
from battle import *
from button import *


class Game:
    def __init__(self):
        self.buttons = []
        pygame.init()

        self.screen = pygame.display.set_mode((160*4, 144*4))
        pygame.display.set_caption("Pokemon!")

        clock = pygame.time.Clock()
        clock.tick(60)

        # Define pokemons and its stats
        self.pokemon1 = Pokemon("Bulbasaur", 100, 11, 3)
        self.pokemon2 = Pokemon("Charmander", 100, 9, 1)
        self.init_pokemon_stats()
        # Attacks
        self.pokemon1.attacks = [
            Attack("latigo cepa", 11, PHYSICAL, 10, 10, 100),
            Attack("placaje", 11, PHYSICAL, 10, 10, 100)
        ]
        self.pokemon2.attacks = [Attack("scratch", 0, PHYSICAL, 10, 10, 100)]

        for idx, attack in enumerate(self.pokemon1.attacks):
            function_turn = partial(self.make_turn, index=idx)
            self.buttons.append(
                Button(idx * 100, 0, 100, 40, attack.name, function_turn)
            )

        self.load_resources()
        print("Resources loaded succesfully")
        # Now we can start the battle
        self.battle = Battle(self.pokemon1, self.pokemon2)

        self.stopped = False
        print("Initialization is finished")

    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stopped = True
            for button in self.buttons:
                button.handle_event(event, self)

    def load_resources(self):
        self.load_pokemon_image(self.pokemon1, True)
        self.load_pokemon_image(self.pokemon2, False)

    def load_pokemon_image(self, pokemon, is_player):
        pokemon_name = pokemon.name.lower()

        if is_player:
            pokemon_img = pygame.image.load(
                "C:/Users/brian/PycharmProjects/PokemonPython/res/" + pokemon_name + "_back.png")
            pokemon_img = pygame.transform.scale(pokemon_img, (200, 200))
        else:
            pokemon_img = pygame.image.load(
                "C:/Users/brian/PycharmProjects/PokemonPython/res/" + pokemon_name + "_front.png")
            pokemon_img = pygame.transform.scale(pokemon_img, (200, 200))

        pokemon.renderer = pokemon_img

    def init_pokemon_stats(self):
        self.pokemon1.current_hp = 45
        self.pokemon2.current_hp = 39

        # Stats

        self.pokemon1.baseStats = {
            HP: 39,
            ATTACK: 52,
            DEFENSE: 43,
            SPATTACK: 80,
            SPDEFENSE: 85,
            SPEED: 65
        }

        self.pokemon1.ev = {
            HP: 0,
            ATTACK: 0,
            DEFENSE: 0,
            SPATTACK: 0,
            SPDEFENSE: 0,
            SPEED: 0
        }

        self.pokemon1.iv = {
            HP: 21,
            ATTACK: 21,
            DEFENSE: 21,
            SPATTACK: 21,
            SPDEFENSE: 21,
            SPEED: 21
        }
        self.pokemon1.compute_stats()

        self.pokemon2.baseStats = {
            HP: 39,
            ATTACK: 52,
            DEFENSE: 43,
            SPATTACK: 80,
            SPDEFENSE: 85,
            SPEED: 65
        }

        self.pokemon2.ev = {
            HP: 0,
            ATTACK: 0,
            DEFENSE: 0,
            SPATTACK: 0,
            SPDEFENSE: 0,
            SPEED: 0
        }

        self.pokemon2.iv = {
            HP: 21,
            ATTACK: 21,
            DEFENSE: 21,
            SPATTACK: 21,
            SPDEFENSE: 21,
            SPEED: 21
        }
        self.pokemon2.compute_stats()

        print(self.pokemon1.stats)
        print(self.pokemon2.stats)

    def render_pokemons(self):
        self.pokemon1.render(self.screen, (10, 200))
        self.pokemon2.render(self.screen, (440, 0))

    def render_buttons(self):
        for button in self.buttons:
            button.render(self)

    def render(self):
        self.screen.fill((255, 255, 255))  # White
        self.render_pokemons()
        self.render_buttons()
        pygame.display.update()

    def make_turn(self, index):
        print("Using attack " + str(index))
        turn = Turn()
        turn.command1 = Command({DO_ATTACK: index})
        turn.command2 = Command({DO_ATTACK: 0})

        if turn.can_start():
            self.battle.execute_turn(turn)
            self.battle.print_current_status()

