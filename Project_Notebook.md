# Project Notebook

This is my project notebook for the Year 9 Asteroids project

**Note**: Class Hierarchy Diagram and game state flow diagrams are seperate files in the github repo, and were created using Lucidchart.

<br>

# IPO Table


| Input | Process | Output |
|-------|---------|--------|
| Keyboard input (WASD or the Arrow keys) | Checks which keys are pressed and based on that it updates movement |  Player moves or rotates |
| Spacebar | Checks to see how much cooldown is left before the player can shoot and if it's 0, it generates a new shot |  A bullet is fired |
| Delta time (```dt```) | Calculates movement based on how much time has passed | Consistent movement across different frame rates |
|Asteroid positions and velocities | Updates asteroid positions and and checks for collisions | Asteroids move and may split (if they're not small) when they're shot. |
| Pygame events | Checks to see if the user has closed the game window | The game exits when the window is closed. |

<br>


# Collision Detection Strategy

My game uses circle based collision detection, because using a triangle is much more complex compared to using a circle for the player. This is because using a circle uses one simple formula. A circle collision only requires measuring the distance between two centres of two circles and comparing it to the sum of their radii (distance <= r1 + r2).

This is seen in the code snippet:

```
distance = self.position.distance_to(other.position)
return distance <= self.radius + other.radius
```

The game uses two different collision types:

1. The player and an asteroid (Results in game over)
2. The asteroid and a bullet (Results in a split asteroid or the asteroid completely disappearing if it's small)

#