import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    # Start Pygame and create the window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Start the infinite game loop
    while True:
        # Log the state at every single iteration
        log_state()

        # Checks the event queue inside the loop so the window responds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exits the main() function and closes the game cleanly
        
        # Fill the screen background with black
        screen.fill("black")

        # Refresh the screen (this must happen last inside the loop)
        pygame.display.flip()

if __name__ == "__main__":
    main()
