import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        # Sets the players angle to 0 when starting the game
        self.rotation = 0

        # Calculates the points of the triangle for pygame for the draw function to draw the player
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Makes the players rotation consistent across different frame rates
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    # This function allows for the player icon to update based on what key is pressed e.g. A for left
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # Makes the rotation decrease when pressing A which makes the player turn left
        if keys[pygame.K_a]:
            self.rotate(-dt)

        # Makes the rotation increase when pressing D which makes the player turn right
        if keys[pygame.K_d]:
            self.rotate(dt)

    def move(self, dt: float) -> None:
        pass