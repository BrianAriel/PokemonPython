from game import *


def main():

    game = Game()
    while not game.stopped:
        # Main battle loop
        # First we need the commands
        game.process()
        game.render()

    pygame.init()


if __name__ == "__main__":
    main()
