import pygame
from pygame.locals import *
from constants import *
from pokemon import *
from battle import *

# First, we define pokemon with its stats

pokemon1 = Pokemon("Bulbasaur", 100, 12, None)
pokemon2 = Pokemon("Bulbasaur", 100, 10, 2)
pokemon1.current_hp = 45
pokemon2.current_hp = 39

# Second, stats
pokemon1.baseStats = {
    HP: 108,
    ATTACK: 130,
    DEFENSE: 95,
    SPATTACK: 80,
    SPDEFENSE: 85,
    SPEED: 102
}

pokemon1.ev = {
    HP: 74,
    ATTACK: 190,
    DEFENSE: 91,
    SPATTACK: 48,
    SPDEFENSE: 84,
    SPEED: 23
}

pokemon1.iv = {
    HP: 24,
    ATTACK: 12,
    DEFENSE: 30,
    SPATTACK: 16,
    SPDEFENSE: 23,
    SPEED: 5
}
pokemon1.compute_stats()

pokemon2.baseStats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

pokemon2.ev = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

pokemon2.iv = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}
pokemon2.compute_stats()

# Third, attacks
pokemon1.attacks = [Attack("Impactrueno", 12, SPECIAL, 10, 10, 100)]
pokemon2.attacks = [Attack("scratch", 0, PHYSICAL, 10, 10, 100)]

# Fourth, start battle
battle = Battle(pokemon1, pokemon2)


def ask_command(pokemon):
    command = None
    while not command:
        # DO ATTACK -> attack 0
        tmp_command = input("What should " + pokemon.name + " do?").split(" ")
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


def load_resources():
    load_pokemon_image(pokemon1, True)
    load_pokemon_image(pokemon2, False)


def update():
    pass


def render(screen):
    screen.fill((255, 255, 255))  # White
    render_pokemons(screen, pokemon1, pokemon2)
    pygame.display.update()


def load_pokemon_image(pokemon, is_player):
    pokemon_name = pokemon.name.lower()

    if is_player:
        pokemon_img = pygame.image.load("C:/Users/brian/PycharmProjects/PokemonPython/res/" + pokemon_name + "_back.png")
        pokemon_img = pygame.transform.scale(pokemon_img, (400, 400))
    else:
        pokemon_img = pygame.image.load("C:/Users/brian/PycharmProjects/PokemonPython/res/" + pokemon_name + "_front.png")
        pokemon_img = pygame.transform.scale(pokemon_img, (400, 400))

    pokemon.renderer = pokemon_img


def render_pokemons(screen, render_pokemon1, render_pokemon2):
    render_pokemon1.render(screen, (10, 200))
    render_pokemon2.render(screen, (440, -50))


def main():

    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption("Pokemon!")
    load_resources()

    clock = pygame.time.Clock()
    clock.tick(60)

    stopped = False
    while not stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopped = True
        update()
        render(screen)


    # Main battle loop
    # First we need the commands
    '''
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)
    
    # New turn
    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2
    
    if turn.can_start():
        # Now we execute the turn
        battle.execute_turn(turn)
        battle.print_current_status()
    '''


if __name__ == "__main__":
    main()
