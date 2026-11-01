import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        # Shot cooldown timer starting at 0
        self.shoot_timer = 0.0

        # Sets the players angle to 0 when starting the game
        self.rotation = 0

        # Calculates the points of the triangle for pygame, for the draw function to draw the player
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Makes the players rotation consistent across different frame rates
    # Also allows for the player to turn left and right by using it in the .update() method
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    # This function allows for the player icon to update based on what key is pressed e.g. A for left
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # Makes the rotation decrease when pressing A which makes the player turn left
        # Optional arrow key method with .K_LEFT to allow use of the left arrow key
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        # Makes the rotation increase when pressing D which makes the player turn right
        # Optional arrow key method with .K_RIGHT to allow use of the right arrow key
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        # Makes the player moove forward when pressing the W key
        # Optional arrow key method with .K_UP to allow use of the up arrow key
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            # The .move is from the .move() method below
            self.move(dt)

        # Makes the player move backward when pressing the S key
        # Optional arrow key method with .K_DOWN to allow use of the down arrow key
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            # The .move is from the .move() method below
            self.move(-dt)

        # Makes the player shoot when pressing the spacebar
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Reduces the shot cooldown every second
        self.shoot_timer -= dt


    # The move method, calculates the vectors and allows the player to move forwards and backwards by using it in the .update() method.
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):

        # Gives a cooldown to the shooting speed of the player.
        if self.shoot_timer > 0:
            return

        # Resets the cooldown clock immediately after a bullet is fired. 
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS


        # Creates and launches a new bullet from the players current position.
        # Spawns the shot
        shot = Shot(self.position.x, self.position.y)

        # Calculates the velocity vector
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
