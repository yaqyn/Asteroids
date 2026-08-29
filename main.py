import pygame

from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state


pygame.init()

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")





    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    fill("black")
    display.flip()
















if __name__ == "__main__":
    main()
