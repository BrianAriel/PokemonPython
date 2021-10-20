from game import *


def main():

    game = Game()
    while not game.stopped:
        # Main battle loop
        # First we need the commands
        game.process()
        game.render()

    pygame.init()
    screen = pygame.display.set_mode((800, 640))


if __name__ == "__main__":
    main()
