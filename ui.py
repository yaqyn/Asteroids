"""Shared arcade presentation for title, HUD, pause, and results."""

import random
import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND,
    FOREGROUND,
    ACCENT,
    DANGER,
    MUTED,
)


class Renderer:
    def __init__(self):
        self.display_font = pygame.font.Font(None, 116)
        self.body_font = pygame.font.Font(None, 30)
        self.utility_font = pygame.font.Font(pygame.font.match_font("monospace"), 20)
        rng = random.Random(31)
        self.stars = [
            (
                rng.randrange(SCREEN_WIDTH),
                rng.randrange(SCREEN_HEIGHT),
                rng.choice([1, 1, 2]),
            )
            for _ in range(110)
        ]

    def text(self, screen, text, position, color=FOREGROUND, font=None, center=False):
        surface = (font or self.body_font).render(text, True, color)
        rect = (
            surface.get_rect(center=position)
            if center
            else surface.get_rect(topleft=position)
        )
        screen.blit(surface, rect)

    def draw(self, screen, game):
        screen.fill(BACKGROUND)
        for x, y, radius in self.stars:
            pygame.draw.circle(screen, (54, 64, 88), (x, y), radius)
        for sprite in game.drawable:
            if sprite is game.player and game.state == "title":
                continue
            # A steady protection ring replaces blinking in reduced-motion mode.
            if (
                sprite is game.player
                and game.invulnerable > 0
                and not game.reduced_motion
            ):
                if int(game.invulnerable * 8) % 2:
                    continue
            sprite.draw(screen)
        if game.invulnerable > 0 and game.state == "playing":
            pygame.draw.circle(screen, ACCENT, game.player.position, 32, 1)
        for position, velocity, life in game.particles:
            pygame.draw.circle(screen, ACCENT, position, max(1, int(life * 4)))
        pygame.draw.line(screen, (54, 64, 88), (40, 82), (SCREEN_WIDTH - 40, 82))
        self.text(
            screen, f"SCORE  {game.score:06d}", (40, 35), ACCENT, self.utility_font
        )
        self.text(
            screen,
            f"BEST  {max(game.best, game.score):06d}",
            (330, 35),
            MUTED,
            self.utility_font,
        )
        self.text(
            screen,
            f"LIVES  {game.lives}    LEVEL  {game.level:02d}",
            (880, 35),
            FOREGROUND,
            self.utility_font,
        )
        self.text(
            screen,
            "WASD / ARROWS  move     SPACE  fire     P  pause     ESC  quit",
            (40, SCREEN_HEIGHT - 38),
            MUTED,
            self.utility_font,
        )
        if game.state != "playing":
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((16, 19, 39, 205))
            screen.blit(overlay, (0, 0))
            titles = {
                "title": "ASTEROIDS",
                "paused": "PAUSED",
                "game_over": "GAME OVER",
            }
            self.text(
                screen,
                "DEEP SPACE / SURVIVAL ARCADE",
                (640, 225),
                ACCENT,
                self.utility_font,
                True,
            )
            self.text(
                screen,
                titles[game.state],
                (640, 320),
                FOREGROUND,
                self.display_font,
                True,
            )
            detail = {
                "title": "Dodge the field. Split the rocks. Stay alive.",
                "paused": "Your run is frozen. Take your time.",
                "game_over": f"Score {game.score:,}   /   Best {game.best:,}",
            }[game.state]
            self.text(screen, detail, (640, 405), MUTED, center=True)
            action = (
                "ENTER  resume"
                if game.state == "paused"
                else "ENTER  start"
                if game.state == "title"
                else "ENTER / R  play again"
            )
            self.text(screen, action, (640, 476), ACCENT, self.utility_font, True)
            self.text(
                screen,
                "WASD / ARROWS  move    SPACE  fire    ESC  quit",
                (640, 556),
                MUTED,
                self.utility_font,
                True,
            )
            if game.save_error:
                self.text(
                    screen,
                    "Best score could not be saved; this run is still available.",
                    (640, 604),
                    DANGER,
                    center=True,
                )
