import pygame
from constants import LINE_WIDTH
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    # Override the draw method to draw the Asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # Override the update method so that the Asteroid moves in a straight line at a constant speed.
    def update(self, dt: float):
        self.position += self.velocity * dt

    