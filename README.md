# Starting off

## Contents

This is the README for the **Asteroids** project.

In the Github repository, there will be 16 files in total.

3 of the files:

- ```pyproject.toml```
- ```uv.lock```
- ```.python-version```

These files are essential for the running of the project, if you download the github repo without these files, the game will not work.

There is another file:

- ```.gitignore```

This file makes sure no extra junk files are sent to the github repo when pushing the code.

log file for game events:

- ```game_events.jsonl```

This file logs everything that happens in the game from the moment it is launched.

Then the main project files:

- ```main.py```
- ```asteroid.py```
- ```circleshape.py```
- ```logger.py```
- ```player.py```
- ```constants.py```
- ```shot.py```
- ```asteroidfield.py```

These files contain the core functions that is required to make the asteroids game work, more details explained below.

Finally the 2 documentation files:

- ```README.md (this file)```
- ```Project Notebook.md```

The project notebook file will contain the IPO table, design decisions, test cases and a reflection on the project.

# Constants.py

This is a very important file, it contains constants for many aspects of the game which is then imported into other files to complete many core functions.

The file contains set constants to control:

- Player dimensions (The triangle)
- Player speed
- The pygame window size
- Asteroid types (amount of types)
- Asteroid spawn rate
- Asteroid dimensions (min and max radius)
- Player shoot speed
- Player shot cooldown
- The shot radius (radius of the bullet)

# Main.py

## Quick Summary

This is the core file for the whole project, it acts as the master controller of the game. It coordinates everything in the game by doing 3 main things:

1. Open a window and sets up a clock to keep the game running smoothly

2. Runs an endless game loop 60 times a second (60fps)

3. Cleans up after you hit a rock

## More detail (The game loop)

### Starting the game

The first three print lines print some basic information to the terminal when the game starts, showing pygame and screen resolutions.

### Initialising Pygame and the game window

The lines:

```
    def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
```

Is where all the pygame modules needed for the game are initialised and where the game window is created by using the dimensions set in constants.py

### Game clock and DT (Delta Time)

```
    clock = pygame.time.Clock()
    dt = 0.0
```

The dt (Delta Time) variable measures how many miliseconds pass between every frame. It's used to make sure the player and the asteroids move at the same speed no matter what sort of harware you're playing on, whether you're playing on a toaster or a NASA level supercomputer.

### Sprite Groups

```
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
```

Sprite group containers are used to organise and manage game objects

Each of these groups holds a different purpose:

- ```Updatable()```: contains objects that need their ```update()``` method called every frame.
- ```drawable```: contains objects that need to be drawn onto the screen
- ```asteroids```: contains all active asteroids
- ```shots```: contains all active bullets fired by the player

Using groups is efficient because that way it managed multiple objects instead of drawing and updating each one individually and manually

### Assigning objects to sprite groups

```
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)
```

This code tells each class which sprite groups its objects should automatically join when they are created

For example:

- The player is added to the ```updatable``` and ```drawable``` groups.
- Asteroids are added to the ```asteroids```, ```updatable``` and ```drawable``` groups.
- Asteroid Field is only added to the ```updatable``` group because it manages asteroid spawning and doesn't need to be drawn.

This approach is much easier for managing game objects, especially when new asteroids and bullets are constantly being created.

### Creating the player and Asteroid Field

```
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()
```

This created the initial game objects

- ```Player()``` creates the players spaceship in the center of the screen.
- ```AsteroidField``` creates the asteroid field, which periodically spawns new asteroids into the game.

These objects automatically join their respective sprite groups.

### The Main Game Loop

```
while True:
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return
```

This starts an infinite loop that keeps the game running.

Everything inside the loop happens repeatedly, once per frame, until either the player closes the window or loses the game.

Pygame collects events such as keyboard presses, mouse clicks and window closing.

In the ```if event.type == pygame.QUIT:``` section, pygame checks for a ```QUIT``` event, which happens when the player clicks the widnow close button.

If this happens , ```return``` exits the ```main()``` function and stops the game.

### Clearing the screen (Still in the main game loop)

```
screen.fill("black")
```

Fills the entire window with black.

This happens every frame to clear the previous frame's drawings before the updated positions of the game objects are drawn.

### Updating game objects (Still in the main game loop)

```
updatable.update(dt)
```

Calls the ```update()``` method on every object in the ```updatable``` group.

This allows players, asteroids, asteroid field and shots to update their positions and behavior.

Passing ```dt``` ensures that movement is based on elapsed time rather than simply moving a fixed amount per frame.

### Checking for player collisions

```
for asteroid in asteroids:
    if asteroid.collides_with(player):
        log_event("player_hit")
        print("Game over!")
        sys.exit()
```

Loops through every active asteroid and checks whether it's collided with the player.

If a collision does occur:

- ```log_event("player_hit")``` records a collision in the game log.
- ```print("Game over!")``` displays a message in the terminal.
- ```sys.exit()``` immediately terminates the game.

### Checking for bullet and asteroid collisions

```
for asteroid in asteroids:
    for shot in shots:
        if asteroid.collides_with(shot):
            log_event("asteroid_shot")
            shot.kill()
            asteroid.split()
```

This loop checks whether any bullets have collided with asteroids.

It uses a nested loop (a loop within a loop) to compare every asteroid against every active bullet.

When a collision happens:

- ```log_event("asteroid_shot")``` record the collision
- ```shot.kill()``` removes the bullet from all sprite groups
- ```asteroid.split()``` destroys the original asteroid and created smaller asteroids depending on its size.

This is what allows players to shoot at asteroids and break them into smaller pieces.

### Drawing game objects

```
for obj in drawable:
    obj.draw(screen)
```

Loops through every objects in the ```drawable``` group and calls its ```draw()``` method.

This displays the player, asteroids and bullets on the screen at their current positions.

### Logging game state

```
log_state()
```

Records the game state in every frame

This is useful for debugging and monitoring whats happening during gameplay.

### Refreshing the screens and controlling FPS

```
pygame.display.flip()
dt = clock.tick(60) / 1000
```

These two lines handle the final stages of each frame:

- ```pygame.display.flip()``` Updates the display so that everything drawn during the current frame becomes visible
- ```clock.tick(60)``` limits the game to a maximum of 60 FPS and returns the time takes since the previous call in miliseconds
- ```/ 1000``` converts the time returned from ```clock.tick(60)``` into seconds and stores it into ```dt``` for the next frame.

### Running the game

```
if __name__ == "__main__":
    main()
```

This checks whether the Python file is being run directly rather than imported into another file.

If it is being run directly, it calles ```main()``` to start the game.

If another Python file wants to import something from main.py, perhaps a function or variable.

Without this condition, importing main.py would automatically start the entire game.

Although this is unlikely to be used in this project but it is there just in case.