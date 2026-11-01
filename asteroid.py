import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
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

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new rotated velocity vectors
        velo1 = self.velocity.rotate(random_angle)
        velo2 = self.velocity.rotate(-random_angle)

        # Compute new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the first new asteroid (faster)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velo1 * 1.2

        # Create the second new asteroid (faster)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velo2 * 1.2


    