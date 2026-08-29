import pygame
from player import Player
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state


pygame.init()
clock = pygame.time.Clock()
dt = 0.0

def main():
    print(f"starting asteroids with pygame version: {pygame.version.ver}")
    print(f"screen width: {SCREEN_WIDTH}\nscreen height: {SCREEN_HEIGHT}")
    
    
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        print(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
















if __name__ == "__main__":
    main()
