import pygame
import sys
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField

pygame.init()
clock = pygame.time.Clock()
dt = 0.0



def main():
    print(f"starting asteroids with pygame version: {pygame.version.ver}")
    print(f"screen width: {SCREEN_WIDTH}\nscreen height: {SCREEN_HEIGHT}")
    
    
    

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                            
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        















if __name__ == "__main__":
    main()
