import pygame
from constants import LINE_WIDTH, PLAYER_RADIUS

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, PLAYER_RADIUS: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = PLAYER_RADIUS

    def draw(self, screen: pygame.Surface) -> None:
        # Draws the player
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH )

    def update(self, dt: float) -> None:
        # must override
        pass