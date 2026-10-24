import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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

    # going to add a comment here as well
    player  = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Start the infinite game loop
    while True:
        
        # Log the game state at every single iteration
        log_state()
        
        # Going to add a comment here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exits the main() function and closes the game cleanly
        
        # Fill the screen background with black
        screen.fill("black")

        # Update the player each frame
        player.update(dt)

        # Refreshes the triangle icon (player) every frame
        player.draw(screen)

        # Refresh the screen for every frame
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
