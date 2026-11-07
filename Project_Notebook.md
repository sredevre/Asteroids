# Project Notebook

This is my project notebook for the Year 9 Asteroids project

**Note**: Class Hierarchy Diagram and game state flow diagrams are seperate files in the GitHub repo, and were created using Lucidchart.

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

<br>

# Reflection

During the development of my Asteroids game I faced a few challenges mainly with small typos, minor mistakes and asteroid splitting.

One challenge was debugging errors. Some errors were difficult to find and fix, which required me to go through my code and test different solutions until I found the problem. Sometime even the smallest typos made the whole game crash, like naming a variable something and when using it elsewhere adding an extra letter which completely broke the game until it was fixed.

I also found asteroid splitting difficult. Getting the original asteroid to disappear and create two smaller asteroids moving in different directions was challenging. Understanding how velocity and vectors controlled the movement of the asteroids also took some time.

If I were to improve my project in the future, I would add more features to make the game more interesting. For example, I could add a scoring system, different difficulty levels and new gameplay features.

Overall I found this project pretty fun, VERY time consuming but still fun. It felt good to see how my hard work created a nice playable game that I could use in my free time or whenever I feel like coming back to it.
