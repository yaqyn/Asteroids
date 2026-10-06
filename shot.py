import pygame
from constants import (
    LINE_WIDTH,
    SHOT_RADIUS,
    SHOT_LIFETIME_SECONDS,
    ACCENT,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.lifetime = SHOT_LIFETIME_SECONDS

    def draw(self, screen):
        pygame.draw.circle(screen, ACCENT, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0 or not (
            0 <= self.position.x <= SCREEN_WIDTH
            and 0 <= self.position.y <= SCREEN_HEIGHT
        ):
            self.kill()
