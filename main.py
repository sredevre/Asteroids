import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    # Start Pygame and create the window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS measurement with Delta time variable (dt) set to 0.0
    clock = pygame.time.Clock()
    dt = 0.0


    # Sprite Groups created
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Defines which groups (containers) each game object belongs to.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    # going to add a comment here as well
    player  = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Start the infinite game loop
    while True:
        
        
        # Going to add a comment here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exits the main() function and closes the game cleanly
        
        # Fill the screen background with black
        screen.fill("black")


        # Object mangement using groups

        # Update all objects in the updatable group at once
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Draw all objects in the drawable group individually by looping through them
        for obj in drawable:
            obj.draw(screen)


        # Log the game state at every single iteration
        log_state()

        # Refresh the screen for every frame
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
