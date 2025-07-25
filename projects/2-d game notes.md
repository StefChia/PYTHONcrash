# PROJECT 1: 2-d game

CH12: A SHIP THAT FIRES BULLETS

Let’s build a game called Alien Invasion! **We’ll use Pygame, a collection of fun, powerful Python modules that manage graphics, animation, and even sound, making it easier for you to build sophisticated games.** With Pygame handling tasks like drawing images to the screen, you can focus on the higher-level logic of game dynamics.”

**In this chapter, you’ll set up Pygame and then create a rocket ship that moves right and left and fires bullets in response to player input. In the next two chapters, you’ll create a fleet of aliens to destroy, and then continue to refine the game by setting limits on the number of ships you can use and adding a scoreboard.**
While building this game, you’ll also learn how to manage large projects that span multiple files. We’ll refactor a lot of code and manage file contents to organize the project and make the code efficient.

“Making games is an ideal way to have fun while learning a language.”

NOTE:

Alien Invasion spans a number of different files, so make a new alien_invasion folder on your system. Be sure to save all files for the project to this folder so your import statements will work correctly.

Also, if you feel comfortable using version control, you might want to use it for this project. If you haven’t used version control before, see Appendix D for an overview.

APPENDIX D: VERSION CONTROL SYSTEMS —STILL TO DO

PLANNING YOUR PROJECT

**When you’re building a large project, it’s important to prepare a plan before you begin to write code. Your plan will keep you focused and make it more likely that you’ll complete the project.
Let’s write a description of the general gameplay.**

In Alien Invasion, the player controls a rocket ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys the aliens. If the player destroys all the aliens, a new fleet appears that moves faster than the previous fleet. If any alien hits the player’s ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.

**For the first development phase, we’ll make a ship that can move right and left when the player presses the arrow keys and fire bullets when the player presses the spacebar(CH12). After setting up this behavior, we can create the aliens(CH13) and refine the gameplay(CH14).**

INSTALLING pygame

Before you begin coding, install Pygame.

```bash
python -m pip install --user pygame
```

**STARTING THE GAME PROJECT**

We’ll begin building the game by creating an empty **Pygame window. Later, we’ll draw the game elements, such as the ship and the aliens, on this window. We’ll also make our game respond to user input, set the background color, and load a ship image.**

CREATING A pygame WINDOW AND RESPONDING TO AN USER INPUT

**We’ll make an empty Pygame window by creating a class to represent the game.**

```python
import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
```

The pygame module contains the functionality we need to make a game. We’ll use tools in the sys module to exit the game when the player quits.

“the pygame.init() function initializes the background settings that Pygame needs to work properly ❶. **Then we call pygame.display.set_mode() to create a display window ❷, on which we’ll draw all the game’s graphical elements. ”**

**The object we assigned to self.screen is called a surface. A surface in Pygame is a part of the screen where a game element can be displayed. Each element in the game, like an alien or a ship, is its own surface.** 

**The surface returned by display.set_mode() represents the entire game window. When we activate the game’s animation loop, this surface will be redrawn on every pass through the loop, so it can be updated with any changes triggered by user input.**

**The game is controlled by the run_game() method. This method contains a while loop ❸ that runs continually. The while loop contains an event loop and code that manages screen updates. An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse. To make our program respond to events, we write an event loop to listen for events and perform appropriate tasks depending on the kinds of events that occur. The for loop ❹ nested inside the while loop is an event loop.**
**To access the events that Pygame detects, we’ll use the pygame.event.get() function. This function returns a list of events that have taken place since the last time this function was called.** Any keyboard or mouse event will cause this for loop to run. **Inside the loop, we’ll write a series of if statements to detect and respond to specific events.** For example, when the player clicks the game window’s close button, a pygame.QUIT event is detected and we call sys.exit() to exit the game ❺.

**The call to pygame.display.flip() ❻ tells Pygame to make the most recently drawn screen visible.** **In this case, it simply draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is visible.** When we move the game elements around, pygame.display.flip() continually updates the display to show the new positions of game elements and hide the old ones, creating the illusion of smooth movement.
**At the end of the file, we create an instance of the game and then call run_game(). We place run_game() in an if block that only runs if the file is called directly.** When you run this alien_invasion.py file, you should see an empty Pygame window.

CONTROLLING THE FRAME RATE

Ideally, games should run at the same speed, or frame rate, on all systems. 

 We’ll make a clock, and ensure the clock ticks once on each pass through the main loop. Anytime the loop processes faster than the rate we define, Pygame will calculate the correct amount of time to pause so that the game runs at a consistent rate.

We’ll define the clock in the **init**() method:

```python
def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
```

After initializing pygame, we create an instance of the class Clock, from the pygame.time module. Then we’ll make the clock tick at the end of the while loop in run_game():

```python
def run_game(self):
    """Start the main loop for the game."""
    while True:
        --snip--
        pygame.display.flip()
        self.clock.tick(60)
```

“The tick() method takes one argument: the frame rate for the game. Here I’m using a value of 60, so Pygame will do its best to make the loop run exactly 60 times per second.”

SETTING THE BACKGROUND COLOR

 Let’s set a different background color. We’ll do this at the end of the **init**() method.

```python
# Set the background color.
❶         self.bg_color = (230, 230, 230)
```

**Colors in Pygame are specified as RGB colors: a mix of red, green, and blue. Each color value can range from 0 to 255.** The color value (255, 0, 0) is red, (0, 255, 0) is green, and (0, 0, 255) is blue. You can mix different RGB values to create up to 16 million colors. The color value (230, 230, 230) mixes equal amounts of red, blue, and green, which produces a light gray background color. We assign this color to self.bg_color ❶.
**We fill the screen with the background color using the fill() method ❷**, which acts on a surface and takes only one argument: a color.

CREATING A SETTING CLASS

Each time we introduce new functionality into the game, we’ll typically create some new settings as well. **Instead of adding settings throughout the code, let’s write a module called settings that contains a class called Settings to store all these values in one place. This approach allows us to work with just one settings object anytime we need to access an individual setting. This also makes it easier to modify the game’s appearance and behavior as our project grows. To modify the game, we’ll change the relevant values in [settings.py](http://settings.py/), which we’ll create next, instead of searching for different settings throughout the project.**

```python
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```

We import Settings into the main program file. Then we create an instance of Settings and assign it to self.settings ❶, after making the call to pygame.init(). When we create a screen ❷, we use the screen_width and screen_height attributes of self.settings, and then we use self.settings to access the background color when filling the screen ❸ as well.

```python
import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
            --snip--
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
```

ADDING THE SHIP IMAGE

**Let’s add the ship to our game. To draw the player’s ship on the screen, we’ll load an image and then use the Pygame blit() method to draw the image.**
When you’re choosing artwork for your games, be sure to pay attention to licensing. The safest and cheapest way to start is to use freely licensed graphics that you can use and modify, from a website like [https://opengameart.org](https://opengameart.org/).
**You can use almost any type of image file in your game, but it’s easiest when you use a bitmap (.bmp) file because Pygame loads bitmaps by default.** 

For Alien Invasion, you can use the file ship.bmp (Figure 12-1), which is available in this book’s resources at [https://ehmatthes.github.io/pcc_3e.](https://ehmatthes.github.io/pcc_3e.%E2%80%9D)

CREATING THE SHIP CLASS

After choosing an image for the ship, we need to display it on the screen. **To use our ship, we’ll create a new ship module that will contain the class Ship.** This class will manage most of the behavior of the player’s ship.

```python

import pygame
class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

**Pygame is efficient because it lets you treat all game elements like rectangles (rects), even if they’re not exactly shaped like rectangles.** Treating an element as a rectangle is efficient because rectangles are simple geometric shapes. When Pygame needs to figure out whether two game elements have collided, for example, it can do this more quickly if it treats each object as a rectangle. **This approach usually works well enough that no one playing the game will notice that we’re not working with the exact shape of each game element.** 
We import the pygame module before defining the class. The **init**() method of Ship takes two parameters: the self reference and **a reference to the current instance of the AlienInvasion class.** This will give Ship access to all the game resources defined in AlienInvasion. We then assign the screen to an attribute of Ship ❶, so we can access it easily in all the methods in this class. **We access the screen’s rect attribute using the get_rect() method and assign it to self.screen_rect ❷**. Doing so allows us to place the ship in the correct location on the screen.

To load the image, we call pygame.image.load() ❸ and give it the location of our ship image. This function returns a surface representing the ship, which we assign to self.image. When the image is loaded, we call get_rect() to access the ship surface’s rect attribute so we can later use it to place the ship.
When you’re working with a rect object, you can use the x- and y-coordinates of the top, bottom, left, and right edges of the rectangle, as well as the center, to place the object. You can set any of these values to establish the current position of the rect. When you’re centering a game element, work with the center, centerx, or centery attributes of a rect. When you’re working at an edge of the screen, work with the top, bottom, left, or right attributes. When you’re adjusting the horizontal or vertical placement of the rect, you can just use the x and y attributes, which are the x- and y-coordinates of its top-left corner.

NOTE!

**In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you go down and to the right.** On a 1200×800 screen, the origin is at the top-left corner, and the bottom-right corner has the coordinates (1200, 800). 

DRAWING THE SHIP TO THE SCREEN

```python
self.ship = Ship(self)
```

We import Ship and then make an instance of Ship after the screen has been created ❶. **The call to Ship() requires one argument: an instance of AlienInvasion. The self argument here refers to the current instance of AlienInvasion. This is the parameter that gives Ship access to the game’s resources, such as the screen object.** We assign this Ship instance to self.ship.

REFACTORING: the _check_events() and _*update_*screen() methods

In large projects, you’ll often refactor code you’ve written before adding more code. **Refactoring simplifies the structure of the code you’ve already written, making it easier to build on.** In this section, we’ll break the run_game() method, which is getting lengthy, into two **helper methods. A helper method does work inside a class but isn’t meant to be used by code outside the class. In Python, a single leading underscore indicates a helper method.**

**the _check_events() method**

```python
   def run_game(self):
        """Start the main loop for the game."""
        while True:
❶           self._check_events()

            # Redraw the screen during each pass through the loop.
            --snip--

❷       def _check_events(self):
          """Respond to keypresses and mouse events."""
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()
```

We’ll move the code that manages events to a separate method called _check_events(). This will simplify run_game() and isolate the event management loop. Isolating the event loop allows you to manage events separately from other aspects of the game, such as updating the screen.

**To call a method from within a class, use dot notation with the variable self and the name of the method ❶.**

**The _*update*_screen() method**

```python
def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()
        self._update_screen()
        self.clock.tick(60)

def _update_screen(self):
     # Redraw the screen during each pass through the loop.
     self.screen.fill(self.settings.bg_color)
     self.ship.blitme()
     # Make the most recently drawn screen visible.
     pygame.display.flip()
```

We moved the code that draws the background and the ship and flips the screen to _update_screen(). Now the body of the main loop in run_game() is much simpler. It’s easy to see that we’re looking for new events, updating the screen, and ticking the clock on each pass through the loop.

**!!!This approach gives you an idea of a realistic development process: you start out writing your code as simply as possible, and then refactor it as your project becomes more complex.**

PILOTING THE SHIP

As we add this code, you’ll learn how to control the movement of images on the screen and respond to user input.

RESPONDING TO A KEY PRESS

Whenever the player presses a key, that keypress is registered in Pygame as an event. Each event is picked up by the pygame.event.get() method. We need to specify in our _check_events() method what kinds of events we want the game to check for. Each keypress is registered as a KEYDOWN event.
When Pygame detects a KEYDOWN event, we need to check whether the key that was pressed is one that triggers a certain action. For example, if the player presses the right arrow key, we want to increase the ship’s rect.x value to move the ship to the right.

ALLOWING CONTINUOUS MOVEMENT

When the player holds down the right arrow key, we want the ship to continue moving right until the player releases the key. We’ll have the game detect a pygame.KEYUP event so we’ll know when the right arrow key is released; then we’ll use the KEYDOWN and KEYUP events together with a flag called moving_right to implement continuous motion.
When the moving_right flag is False, the ship will be motionless. When the player presses the right arrow key, we’ll set the flag to True, and when the player releases the key, we’ll set the flag to False again.

We add a self.moving_right attribute in the **init**() method and set it to False initially ❶. Then we add update(), which moves the ship right if the flag is True ❷. The update() method will be called from outside the class, so it’s not considered a helper method.

```python
def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            --snip--
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
❶                     self.ship.moving_right = True
❷             elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
```

Next, we modify the while loop in run_game() so it calls the ship’s update() method on each pass through the loop. The ship’s position will be updated after we’ve checked for keyboard events and before we update the screen. 

MOVING BOTH LEFT AND RIGHT

In update(), we use two separate if blocks, rather than an elif, to allow the ship’s rect.x value to be increased and then decreased when both arrow keys are held down. This results in the ship standing still. If we used elif for motion to the left, the right arrow key would always have priority. Using two if blocks makes the movements more accurate when the player might momentarily hold down both keys when changing directions.

We can use elif blocks here because each event is connected to only one key. If the player presses both keys at once, two separate events will be detected.”

ADJUSTING THE SHIP’S SPEED

“we can take finer control of the ship’s speed by adding a ship_speed attribute to the Settings class. We’ll use this attribute to determine how far to move the ship on each pass through the loop.”

“We’re using a float for the speed setting to give us finer control of the ship’s speed when we increase the tempo of the game later on. However, rect attributes such as x store only integer values, so we need to make some modifications to Ship:”

**You can use a float to set an attribute of a rect, but the rect will only keep the integer portion of that value. To keep track of the ship’s position accurately, we define a new self.x ❷. We use the float() function to convert the value of self.rect.x to a float and assign this value to self.x.
Now when we change the ship’s position in update(), the value of self.x is adjusted by the amount stored in settings.ship_speed ❸. After self.x has been updated, we use the new value to update self.rect.x, which controls the position of the ship ❹. Only the integer portion of self.x will be assigned to self.rect.x, but that’s fine for displaying the ship.**

I.E. GIOCA SU DUE LIVELLI

LIMITING THE SHIP’S RANGE

Let’s correct this so the ship stops moving when it reaches the screen’s edge.

```python
def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
❶         if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
❷         if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
```

REFACTORING _*CHECKS*_EVENTS()

so let’s break _check_events() into two separate methods: one that handles KEYDOWN events and another that handles KEYUP events:

```python
def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True

def _check_keyup_events(self, event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False
```

“The _check_events() method is simpler now with this cleaner code structure, which will make it easier to develop further responses to player input.”

PRESSING Q TO QUIT

so we’ll add a keyboard shortcut to end the game when the player presses Q:

```python
def _check_keydown_events(self, event):
        --snip--
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
```

RUNNING THE GAME IN FULL-SCREEN MODE

“To run the game in fullscreen mode, make the following changes in **init**():”

```python
def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

❶         self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
❷         self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
```

When creating the screen surface, we pass a size of (0, 0) and the parameter pygame.FULLSCREEN ❶. This tells Pygame to figure out a window size that will fill the screen. Because we don’t know the width and height of the screen ahead of time, we update these settings after the screen is created ❷. We use the width and height attributes of the screen’s rect to update the settings object.

SHOOTING BULLETS

**We’ll write code that fires a bullet, which is represented by a small rectangle, when the player presses the spacebar. Bullets will then travel straight up the screen until they disappear off the top of the screen.**

ADDING THE BULLET SETTINGS

we’ll update [settings.py](http://settings.py/) to include the values we’ll need for a new Bullet class.

```python
def __init__(self):
        --snip--
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
```

CREATING THE BULLET CLASS

Now create a [bullet.py](http://bullet.py/) file to store our Bullet class.

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)
```

**The Bullet class inherits from Sprite, which we import from the pygame.sprite module. When you use sprites, you can group related elements in your game and act on all the grouped elements at once (see later). To create a bullet instance, init() needs the current instance of AlienInvasion, and we call super() to inherit properly from Sprite. We also set attributes for the screen and settings objects, and for the bullet’s color.**

“The bullet isn’t based on an image, so we have to build a rect from scratch using the pygame.Rect() class. This class requires the x- and y-coordinates of the top-left corner of the rect, and the width and height of the rect”

We set the bullet’s midtop attribute to match the ship’s midtop attribute ❷. This will make the bullet emerge from the top of the ship, making it look like the bullet is fired from the ship. We use a float for the bullet’s y-coordinate so we can make fine adjustments to the bullet’s speed ❸.

```python
def update(self):
            """Move the bullet up the screen."""
            # Update the exact position of the bullet.
            self.y -= self.settings.bullet_speed
            # Update the rect position.
            self.rect.y = self.y

        def draw_bullet(self):
            """Draw the bullet to the screen."""
            pygame.draw.rect(self.screen, self.color, self.rect)
```

To update the position, we subtract the amount stored in settings.bullet_speed from self.y ❶. We then use the value of self.y to set the value of self.rect.y ❷.

STORING BULLETS IN A GROUP

**Now that we have a Bullet class and the necessary settings defined, we can write code to fire a bullet each time the player presses the spacebar. We’ll create a group in AlienInvasion to store all the active bullets so we can manage the bullets that have already been fired. This group will be an instance of the pygame.sprite.Group class, which behaves like a list with some extra functionality that’s helpful when building games. We’ll use this group to draw bullets to the screen on each pass through the main loop and to update each bullet’s position.**

```python
def __init__(self):
        --snip--
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)
```

**When you call update() on a group, the group automatically calls update() for each sprite in the group. The line self.bullets.update() calls bullet.update() for each bullet we place in the group bullets.**

FIRING BULLETS

In AlienInvasion, we need to modify _check_keydown_events() to fire a bullet when the player presses the spacebar. We also need to modify _update_screen() to make sure each bullet is drawn to the screen before we call flip().
There will be a bit of work to do when we fire a bullet, so let’s write a new method, _fire_bullet(), to handle this work:

```python
def _check_keydown_events(self, event):
        --snip--
        elif event.key == pygame.K_q:
            sys.exit()
❶         elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        --snip--

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
❷         new_bullet = Bullet(self)
❸         self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
❹         for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        pygame.display.flip()
--snip--
```

**We call _fire_bullet() when the spacebar is pressed ❶. In _fire_bullet(), we make an instance of Bullet and call it new_bullet ❷. We then add it to the group bullets using the add() method ❸. The add() method is similar to append(), but it’s written specifically for Pygame groups.
The bullets.sprites() method returns a list of all sprites in the group bullets. To draw all fired bullets to the screen, we loop through the sprites in bullets and call draw_bullet() on each one ❹. We place this loop before the line that draws the ship, so the bullets don’t start out on top of the ship.**

DELETING OLD BULLETS

At the moment, the bullets disappear when they reach the top, but only because Pygame can’t draw them above the top of the screen. **The bullets actually continue to exist; their y-coordinate values just grow increasingly negative. This is a problem because they continue to consume memory and processing power.**
We need to get rid of these old bullets, or the game will slow down from doing so much unnecessary work. **To do this, we need to detect when the bottom value of a bullet’s rect has a value of 0, which indicates the bullet has passed off the top of the screen:**

```python
# Get rid of bullets that have disappeared.
❶             for bullet in self.bullets.copy():
❷                 if bullet.rect.bottom <= 0:
❸                     self.bullets.remove(bullet)
❹             print(len(self.bullets))
```

**When you use a for loop with a list (or a group in Pygame), Python expects that the list will stay the same length as long as the loop is running. That means you can’t remove items from a list or group within a for loop, so we have to loop over a copy of the group. We use the copy() method to set up the for loop ❶,** which leaves us free to modify the original bullets group inside the loop. We check each bullet to see whether it has disappeared off the top of the screen ❷. If it has, we remove it from bullets ❸. We insert a print() call to show how many bullets currently exist in the game and verify they’re being deleted when they reach the top of the screen ❹.

After you run the game and verify that bullets are being deleted properly, remove the print() call. If you leave it in, the game will slow down significantly because it takes more time to write output to the terminal than it does to draw graphics to the game window.

LIMITING THE NUMBER OF BULLETS

Many shooting games limit the number of bullets a player can have on the screen at one time; doing so encourages players to shoot accurately.

```python
# Bullet settings
        --snip--
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
```

```python
def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
```

When the player presses the spacebar, we check the length of bullets. If len(self.bullets) is less than three, we create a new bullet. But if three bullets are already active, nothing happens when the spacebar is pressed.

CREATING THE _*update_*bullets_method()

Now that we’ve written and checked the bullet management code, we can move it to a separate method. We’ll create a new method called _update_bullets() and add it just before _update_screen():

```python
def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    self.bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
             self.bullets.remove(bullet)
```

and 

```python
while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
```

Now our main loop contains only minimal code, so we can quickly read the method names and understand what’s happening in the game. **The main loop checks for player input, and then updates the position of the ship and any bullets that have been fired. We then use the updated positions to draw a new screen and tick the clock at the end of each pass through the loop.**

CH13: ALIENS

**Detecting collisions helps you define interactions between elements in your games. For example, you can confine a character inside the walls of a maze or pass a ball between two characters.**

In this chapter, we’ll do the following:

Add a single alien to the top-left corner of the screen, with appropriate spacing around it.
Fill the upper portion of the screen with as many aliens as we can fit horizontally. We’ll then create additional rows of aliens until we have a full fleet.
Make the fleet move sideways and down until the entire fleet is shot down, an alien hits the ship, or an alien reaches the ground. If the entire fleet is shot down, we’ll create a new fleet. If an alien hits the ship or the ground, we’ll destroy the ship and create a new fleet.
Limit the number of ships the player can use, and end the game when the player has used up the allotted number of ships.

We’ll refine this plan as we implement features, but this is specific enough to start writing code.

CREATING THE FIRST ALIEN

Placing one alien on the screen is like placing a ship on the screen. Each alien’s behavior is controlled by a class called Alien, which we’ll structure like the Ship class. 

CREATING THE ALIEN CLASS

```python
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
```

We initially place each alien near the top-left corner of the screen; we add a space to the left of it that’s equal to the alien’s width and a space above it equal to its height ❶, so it’s easy to see. We’re mainly concerned with the aliens’ horizontal speed, so we’ll track the horizontal position of each alien precisely ❷.
This Alien class doesn’t need a method for drawing it to the screen; instead, we’ll use a Pygame group method that automatically draws all the elements of a group to the screen.

CREATING AN INSTANCE OF THE ALIEN

We want to create an instance of Alien so we can see the first alien on the screen. Because it’s part of our setup work, we’ll add the code for this instance at the end of the **init**() method in AlienInvasion. Eventually, we’ll create an entire fleet of aliens, which will be quite a bit of work, so we’ll make a new helper method called _create_fleet().

```python
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        self.aliens.add(alien)
```

In this method, we’re creating one instance of Alien and then adding it to the group that will hold the fleet. The alien will be placed in the default upper-left area of the screen.

```python
    def _update_screen(self):
        --snip--
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()
```

**When you call draw() on a group, Pygame draws each element in the group at the position defined by its rect attribute. The draw() method requires one argument: a surface on which to draw the elements from the group.**

BUILDING THE ALIEN FLEET

Now we’re ready to generate a full row of aliens. To make a full row, we’ll first make a single alien so we have access to the alien’s width. We’ll place an alien on the left side of the screen and then keep adding aliens until we run out of space:

```python
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += 2 * alien_width
```

**Whenever there’s enough horizontal space to continue the loop, we want to do two things: create an alien at the correct position, and define the horizontal position of the next alien in the row.** We create an alien and assign it to new_alien ❸. Then we set the precise horizontal position to the current value of current_x ❹. We also position the alien’s rect at this same x-value, and add the new alien to the group self.aliens.

**!!!Note
It’s not always obvious exactly how to construct a loop like the one shown in this section. One nice thing about programming is that your initial ideas for how to approach a problem like this don’t have to be correct. It’s perfectly reasonable to start a loop like this with the aliens positioned too far to the right, and then modify the loop until you have an appropriate amount of space on the screen.**

REFACTORING **create**_fleet()

ADDING ROWS

To finish the fleet, we’ll keep adding more rows until we run out of room. We’ll use a nested loop—we’ll wrap another while loop around the current one. The inner loop will place aliens horizontally in a row by focusing on the aliens’ x-values. The outer loop will place aliens vertically by focusing on the y-values. We’ll stop adding rows when we get near the bottom of the screen, leaving enough space for the ship and some room to start firing at the aliens.

```python
def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
❶         alien_width, alien_height = alien.rect.size

❷         current_x, current_y = alien_width, alien_height
❸         while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
❹                 self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

❺             # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height
```

Notice the indentation of the last two lines of code ❺. They’re inside the outer while loop, but outside the inner while loop. This block runs after the inner loop is finished; it runs once after each row is created. After each row has been added, we reset the value of current_x so the first alien in the next row will be placed at the same position as the first alien in the previous rows.

We need to modify _create_alien() to set the vertical position of the alien correctly:

```python
def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
```

MAKING THE FLEET MOVE

Now let’s make the fleet of aliens move to the right across the screen until it hits the edge, and then make it drop a set amount and move in the other direction. We’ll continue this movement until all aliens have been shot down, one collides with the ship, or one reaches the bottom of the screen. Let’s begin by making the fleet move to the right.

MOVING THE ALIENS RIGHT

To move the aliens, we’ll use an update() method in [alien.py](http://alien.py/), which we’ll call for each alien in the group of aliens. First, add a setting to control the speed of each alien:

```python
def update(self):
        """Move the alien to the right."""
❶         self.x += self.settings.alien_speed
❷         self.rect.x = self.x
```

Each time we update an alien’s position, we move it to the right by the amount stored in alien_speed. We track the alien’s exact position with the self.x attribute, which can hold float values ❶. We then use the value of self.x to update the position of the alien’s rect ❷.

```python
def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self.aliens.update()
```

```python
      while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
```

**We update the aliens’ positions after the bullets have been updated, because we’ll soon be checking to see whether any bullets hit any aliens.**
Where you place this method in the module is not critical. But to keep the code organized, I’ll place it just after _update_bullets() to match the order of method calls in the while loop.

CREATING SETTINGS FOR FLEET DIRECTION

Now we’ll create the settings that will make the fleet move down the screen and to the left when it hits the right edge of the screen. Here’s how to implement this behavior.

```python
# Alien settings
        self.alien_speed = 1.0
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
```

The setting fleet_drop_speed controls how quickly the fleet drops down the screen each time an alien reaches either edge. It’s helpful to separate this speed from the aliens’ horizontal speed so you can adjust the two speeds independently.
**To implement the setting fleet_direction, we could use a text value such as 'left' or 'right', but we’d end up with if-elif statements testing for the fleet direction. Instead, because we only have two directions to deal with, let’s use the values 1 and −1 and switch between them each time the fleet changes direction. (Using numbers also makes sense because moving right involves adding to each alien’s x-coordinate value, and moving left involves subtracting from each alien’s x-coordinate value.)**

CHECKING WHETHER AN ALIEN HAS IT THE EDGE

We need a method to check whether an alien is at either edge, and we need to modify update() to allow each alien to move in the appropriate direction. 

```python
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
```

**Rather than put this conditional test in an if block, we put the test directly in the return statement. This method will return True if the alien is at the right or left edge, and False if it is not at either edge.**

**We modify the method update() to allow motion to the left or right by multiplying the alien’s speed by the value of fleet_direction ❷**. If fleet_direction is 1, the value of alien_speed will be added to the alien’s current position, moving the alien to the right; if fleet_direction is −1, the value will be subtracted from the alien’s position, moving the alien to the left.”

DROPPING THE FLEET AND CHANGING DIRECTION

we need to add some code to AlienInvasion because that’s where we’ll check whether any aliens are at the left or right edge. We’ll make this happen by writing the methods _check_fleet_edges() and _change_fleet_direction(), and then modifying _update_aliens().

```python
def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
```

In _check_fleet_edges(), we loop through the fleet and call check_edges() on each alien ❶. If check_edges() returns True, we know an alien is at an edge and the whole fleet needs to change direction; so we call _change_fleet_direction() and break out of the loop ❷. In _change_fleet_direction(), we loop through all the aliens and drop each one using the setting fleet_drop_speed ❸; then we change the value of fleet_direction by multiplying its current value by −1.

```python
def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()
```

SHOOTING ALIENS

**In game programming, collisions happen when game elements overlap. To make the bullets shoot down aliens, we’ll use the function sprite.groupcollide() to look for collisions between members of two groups.**

We want to know right away when a bullet hits an alien so we can make an alien disappear as soon as it’s hit. To do this, we’ll look for collisions immediately after updating the position of all the bullets.
**The sprite.groupcollide() function compares the rects of each element in one group with the rects of each element in another group.** In this case, it compares each bullet’s rect with each alien’s rect and returns a dictionary containing the bullets and aliens that have collided. **Each key in the dictionary will be a bullet, and the corresponding value will be the alien that was hit.** (We’ll also use this dictionary when we implement a scoring system in Chapter 14.)

```python
def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        --snip--

        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
```

The new code we added compares the positions of all the bullets in self.bullets and all the aliens in self.aliens, and identifies any that overlap. Whenever the rects of a bullet and alien overlap, groupcollide() adds a key-value pair to the dictionary it returns. The two True arguments tell Pygame to delete the bullets and aliens that have collided. (**To make a high-powered bullet that can travel to the top of the screen, destroying every alien in its path, you could set the first Boolean argument to False and keep the second Boolean argument set to True. The aliens hit would disappear, but all bullets would stay active until they disappeared off the top of the screen.)**

MAKING LAREGER BULLETS FOR TESTING

You can test many features of Alien Invasion simply by running the game, but some features are tedious to test in the normal version of the game. For example, it’s a lot of work to shoot down every alien on the screen multiple times to test whether your code responds to an empty fleet correctly.
To test particular features, you can change certain game settings to focus on a particular area. For example, you might shrink the screen so there are fewer aliens to shoot down or increase the bullet speed and give yourself lots of bullets at once.
My favorite change for testing Alien Invasion is to use really wide bullets that remain active even after they’ve hit an alien (see Figure 13-6). 

REPOPULATING THE FLEET

**Every time the fleet is destroyed, a new fleet should appear.
To make a new fleet of aliens appear after a fleet has been destroyed, we first check whether the aliens group is empty.** If it is, we make a call to _create_fleet(). **We’ll perform this check at the end of _update_bullets(), because that’s where individual aliens are destroyed.**

```python
def _update_bullets(self):
        --snip--
❶         if not self.aliens:
            # Destroy existing bullets and create new fleet.
❷             self.bullets.empty()
	            self._create_fleet()
```

We check whether the aliens group is empty ❶. An empty group evaluates to False, so this is a simple way to check whether the group is empty. If it is, we get rid of any existing bullets by using the empty() method, which removes all the remaining sprites from a group ❷. We also call _create_fleet(), which fills the screen with aliens again.

SPEEDING UP THE BULLETS

REFACTORING *updates*_bullets()

“We’ll move the code for dealing with bullet-alien collisions to a separate method:”

“We’ve created a new method, _check_bullet_alien_collisions(), to look for collisions between bullets and aliens and to respond appropriately if the entire fleet has been destroyed. ”

ENDING THE GAME

If the player doesn’t shoot down the fleet quickly enough, we’ll have the aliens destroy the ship when they make contact. At the same time, we’ll limit the number of ships a player can use, and we’ll destroy the ship when an alien reaches the bottom of the screen. The game will end when the player has used up all their ships.

DETECTING ALIEN-SHIP COLLISION

We’ll start by checking for collisions between aliens and the ship so we can respond appropriately when an alien hits it. **We’ll check for alien-ship collisions immediately after updating the position of each alien in AlienInvasion.**

```python
def _update_aliens(self):
        --snip--
        self.aliens.update()

        # Look for alien-ship collisions.
❶         if pygame.sprite.spritecollideany(self.ship, self.aliens):
❷             print("Ship hit!!!")
```

The spritecollideany() function takes two arguments: a sprite and a group. The function looks for any member of the group that has collided with the sprite and stops looping through the group as soon as it finds one member that has collided with the sprite. Here, it loops through the group aliens and returns the first alien it finds that has collided with ship.
**If no collisions occur, spritecollideany() returns None and the if block won’t execute ❶. If it finds an alien that has collided with the ship, it returns that alien and the if block executes: it prints Ship hit!!! ❷. When an alien hits the ship, we’ll need to do a number of tasks: delete all remaining aliens and bullets, recenter the ship, and create a new fleet.**

RESPOND TO ALIEN-SHIP COLLISION

Now we need to figure out exactly what will happen when an alien collides with the ship. **Instead of destroying the ship instance and creating a new one, we’ll count how many times the ship has been hit by tracking statistics for the game. Tracking statistics will also be useful for scoring.
Let’s write a new class, GameStats, to track game statistics,** and let’s save it as game_stats.py.

```python
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
```

**We’ll make one GameStats instance for the entire time Alien Invasion is running, but we’ll need to reset some statistics each time the player starts a new game. To do this, we’ll initialize most of the statistics in the reset_stats() method, instead of directly in init(). We’ll call this method from init() so the statistics are set properly when the GameStats instance is first created ❶. But we’ll also be able to call reset_stats() anytime the player starts a new game.**

We import the sleep() function from the time module in the Python standard library, so we can pause the game for a moment when the ship is hit. We also import GameStats.

```python
from time import sleep
```

We’ll create an instance of GameStats in **init**():

```python
def __init__(self):
        --snip--
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
```

**When an alien hits the ship, we’ll subtract 1 from the number of ships left, destroy all existing aliens and bullets, create a new fleet, and reposition the ship in the middle of the screen. We’ll also pause the game for a moment so the player can notice the collision and regroup before a new fleet appears.
Let’s put most of this code in a new method called _ship_hit(). We’ll call this method from _update_aliens() when an alien hits the ship:**

```python
def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships_left.
❶         self.stats.ships_left -= 1

        # Get rid of any remaining bullets and aliens.
❷         self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
❸         self._create_fleet()
        self.ship.center_ship()

        # Pause.
❹         sleep(0.5)
```

**The sleep() call pauses program execution for half a second, long enough for the player to see that the alien has hit the ship. When the sleep() function ends, code execution moves on to the _update_screen() method, which draws the new fleet to the screen.**

**In _update_aliens(), we replace the print() call with a call to _ship_hit() when an alien hits the ship:**

```python
def _update_aliens(self):
        --snip--
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
```

```python
def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
```

ALIENS THAT REACH THE BOTTOM OF THE SCREEN

If an alien reaches the bottom of the screen, we’ll have the game respond the same way it does when an alien hits the ship. To check when this happens, add a new method in alien_invasion.py:

```python
   def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
❶             if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break
```

We’ll call this method from _update_aliens():

```python
def _update_aliens(self):
        --snip--
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
```

GAME OVER!

Alien Invasion feels more complete now, but the game never ends. The value of ships_left just grows increasingly negative. Let’s add a game_active flag, so we can end the game when the player runs out of ships. We’ll set this flag at the end of the **init**() method in AlienInvasion:”

```python
def __init__(self):
        --snip--
        # Start Alien Invasion in an active state.
        self.game_active = True
```

```python
def _ship_hit(self):
        """Respond to ship being hit by alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            --snip--
            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
```

IDENTIFYING WHEN PARTS OF THE GAME SHOULD RUN

**We need to identify the parts of the game that should always run and the parts that should run only when the game is active**

```python
def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)
```

In the main loop, we always need to call _check_events(), even if the game is inactive. For example, we still need to know if the user presses Q to quit the game or clicks the button to close the window. We also continue updating the screen so we can make changes to the screen while waiting to see whether the player chooses to start a new game. **The rest of the function calls need to happen only when the game is active, because when the game is inactive, we don’t need to update the positions of game elements.**

Now when you play Alien Invasion, the game should freeze when you’ve used up all your ships.

CH14: SCORING

ADDING THE PLAY BUTTON

In this section, we’ll add a Play button that appears before a game begins and reappears when the game ends so the player can play again.

```python
# Start Alien Invasion in an inactive state.
        self.game_active = False
```

Now the game should start in an inactive state, with no way for the player to start it until we make a Play button.

CREATING A BUTTON CLASS

we’ll write a Button class to create a filled rectangle with a label. You can use this code to make any button in a game.

```python
import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)
```

**First, we import the pygame.font module, which lets Pygame render text to the screen.** The **init**() method takes the parameters self, the ai_game object, and msg, which contains the button’s text ❶. 

```python
 def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
```

Finally, we create a draw_button() method that we can call to display the button onscreen:

```python
def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
```

We call screen.fill() to draw the rectangular portion of the button. Then we call screen.blit() to draw the text image to the screen, passing it an image and the rect object associated with the image. 

DRAWING THE BUTTON TO THE SCREEN

“We’ll use the Button class to create a Play button in AlienInvasion.”

“Because we need only one Play button, we’ll create the button in the **init**() method of AlienInvasion. We can place this code at the very end of **init**():

```python
# Make the Play button.
        self.play_button = Button(self, "Play")
```

This code creates an instance of Button with the label Play, but it doesn’t draw the button to the screen. To do this, we’ll call the button’s draw_button() method in _update_screen():

To make the Play button visible above all other elements on the screen, we draw it after all the other elements have been drawn but before flipping to a new screen. We include it in an if block, so the button only appears when the game is inactive.

STARTING THE GAME

“To start a new game when the player clicks Play, add the following elif block to the end of _check_events() to monitor mouse events over the button:”

```python
def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                --snip--
❶             elif event.type == pygame.MOUSEBUTTONDOWN:
❷                 mouse_pos = pygame.mouse.get_pos()
❸                 self._check_play_button(mouse_pos)
```

**Pygame detects a MOUSEBUTTONDOWN event when the player clicks anywhere on the screen ❶, but we want to restrict our game to respond to mouse clicks only on the Play button. To accomplish this, we use pygame.mouse.get_pos(), which returns a tuple containing the mouse cursor’s x- and y-coordinates when the mouse button is clicked ❷. We send these values to the new method _check_play_button() ❸.**

“We use the rect method collidepoint() to check whether the point of the mouse click overlaps the region defined by the Play button’s rect ❶. If so, we set game_active to True, and the game begins!

RESETTING THE GAME

```python
def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game statistics.
❶             self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
❷             self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
❸             self._create_fleet()
            self.ship.center_ship()
```

“Now the game will reset properly each time you click Play, allowing you to play it as many times as you want!”

DEACTIVATING THE PLAY BUTTON

“One issue with our Play button is that the button region on the screen will continue to respond to clicks even when the Play button isn’t visible. If you click the Play button area by accident after a game begins, the game will restart!
To fix this, set the game to start only when game_active is False:”

```python
 def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
    
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            
            # Reset the game statistics.
            self.stats.reset_stats()      
```

“The flag button_clicked stores a True or False value ❶, and the game will restart only if Play is clicked and the game is not currently active ❷. ”

HIDING THE MOUSE CURSOR

We want the mouse cursor to be visible when the game is inactive, but once play begins, it just gets in the way. To fix this, we’ll make it invisible when the game becomes active. We can do this at the end of the if block in _check_play_button():

```python
def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            --snip--
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
```

“We’ll make the cursor reappear once the game ends so the player can click Play again to begin a new game. Here’s the code to do that:

```python
def _ship_hit(self):
        """Respond to ship being hit by alien."""
        if self.stats.ships_left > 0:
            --snip--
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
```

We make the cursor visible again as soon as the game becomes inactive, which happens in _ship_hit(). Attention to details like this makes your game more professional looking and allows the player to focus on playing, rather than figuring out the user interface.

LEVELING UP

“ Let’s liven things up a bit and make the game more challenging by increasing the game’s speed each time a player clears the screen.”

MODIFYING THE SPEED SETTINGS

```python
# How quickly the game speeds up
❶         self.speedup_scale = 1.1

❷         self.initialize_dynamic_settings()
```

“We add a speedup_scale setting ❶ to control how quickly the game speeds up: a value of 2 will double the game speed every time the player reaches a new level; a value of 1 will keep the speed constant. A value like 1.1 should increase the speed enough to make the game challenging but not impossible. Finally, we call the initialize_dynamic_settings() method to initialize the values for attributes that need to change throughout the game ❷.”

```python
def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
```

**This method sets the initial values for the ship, bullet, and alien speeds. We’ll increase these speeds as the player progresses in the game and reset them each time the player starts a new game.** We include fleet_direction in this method so the aliens always move right at the beginning of a new game. We don’t need to increase the value of fleet_drop_speed, because when the aliens move faster across the screen, they’ll also come down the screen faster.
To increase the speeds of the ship, bullets, and aliens each time the player reaches a new level, we’ll write a new method called increase_speed():

```python
def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
```

“To increase the speed of these game elements, we multiply each speed setting by the value of speedup_scale.
We increase the game’s tempo by calling increase_speed() in _check_bullet_alien_collisions() when the last alien in a fleet has been shot down:

```python
 def _check_bullet_alien_collisions(self):
        --snip--
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
```

RESETTING THE SPEED

“Now we need to return any changed settings to their initial values each time the player starts a new game; otherwise, each new game would start with the increased speed settings of the previous game:

```python
“""Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            --snip”
```

SCORING

Let’s implement a scoring system to track the game’s score in real time and display the high score, level, and number of ships remaining.
The score is a game statistic, so we’ll add a score attribute to GameStats:

```python
class GameStats:
    --snip--
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
```

DISPLAY THE SCORE

**To display the score on the screen, we first create a new class, Scoreboard. For now, this class will just display the current score. Eventually, we’ll use it to report the high score, level, and number of ships remaining as well.** Here’s the first part of the class; save it as [scoreboard.py](http://scoreboard.py/):

```python
import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
```

To turn the text to be displayed into an image, we call prep_score() ❹, which we define here:

```python
“  def prep_score(self):
        """Turn the score into a rendered image."""
❶         score_str = str(self.stats.score)
❷         self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
❸         self.score_rect = self.score_image.get_rect()
❹         self.score_rect.right = self.screen_rect.right - 20
❺         self.score_rect.top = 20
```

In prep_score(), we turn the numerical value stats.score into a string ❶ and then pass this string to render(), which creates the image ❷. To display the score clearly onscreen, we pass the screen’s background color and the text color to render().
We’ll position the score in the upper-right corner of the screen and have it expand to the left as the score increases and the width of the number grows. To make sure the score always lines up with the right side of the screen, we create a rect called score_rect ❸ and set its right edge 20 pixels from the right edge of the screen ❹. We then place the top edge 20 pixels down from the top of the screen ❺.
Then we create a show_score() method to display the rendered score image:

```python
   def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
```

“This method draws the score image onscreen at the location score_rect specifies.”

MAKING A SCOREBOARD

To display the score, we’ll create a Scoreboard instance in AlienInvasion.

UPDATING THE SCORE AS ALIENS ARE SHOT DOWN

“To write a live score onscreen, we update the value of stats.score whenever an alien is hit, and then call prep_score() to update the score image.”

```python
    def initialize_dynamic_settings(self):
        --snip--

        # Scoring settings
        self.alien_points = 50
```

“Let’s update the score in _check_bullet_alien_collisions() each time an alien is shot down:”

```python
  def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
        --snip
```

“When a bullet hits an alien, Pygame returns a collisions dictionary. We check whether the dictionary exists, and if it does, the alien’s value is added to the score. We then call prep_score() to create a new image for the updated score.”

RESETTING THE SCORE

“prepping the score when starting a new game:”

```python
def _check_play_button(self, mouse_pos):
        --snip--
        if button_clicked and not self.game_active:
            --snip--
            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            --snip
```

MAKING SURE TO SCORE ALL HITS

“As currently written, our code could miss scoring for some aliens. For example, if two bullets collide with aliens during the same pass through the loop or if we make an extra-wide bullet to hit multiple aliens, the player will only receive points for hitting one of the aliens. To fix this, let’s refine the way that bullet-alien collisions are detected.
In _check_bullet_alien_collisions(), any bullet that collides with an alien becomes a key in the collisions dictionary. The value associated with each bullet is a list of aliens it has collided with. We loop through the values in the collisions dictionary to make sure we award points for each alien hit:

“If the collisions dictionary has been defined, we loop through all values in the dictionary. **Remember that each value is a list of aliens hit by a single bullet.** We multiply the value of each alien by the number of aliens in each list and add this amount to the current score”

```python
def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
                for aliens in collisions.values():
                    self.stats.score += self.settings.alien_points * len(aliens)
                    self.sb.prep_score()
```

INCREASING POINT VALUES

“we’ll add code to increase the point value when the game’s speed increases:”

```python
        # Scoring settings
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
```

Now when we increase the game’s speed, we also increase the point value of each hit ❷. We use the int() function to increase the point value by whole integers.

ROUNDING THE SCORE

Most arcade-style shooting games report scores as multiples of 10, so let’s follow that lead with our scores. Also, let’s format the score to include comma separators in large numbers. We’ll make this change in Scoreboard:

```python
def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
        --snip--
```

**The round() function normally rounds a float to a set number of decimal places given as the second argument. However, when you pass a negative number as the second argument, round() will round the value to the nearest 10, 100, 1,000, and so on.** 

We then use a **format specifier in the f-string for the score. A format specifier is a special sequence of characters that modifies the way a variable’s value is presented.** In this case the sequence :, tells Python to insert commas at appropriate places in the numerical value that’s provided. This results in strings like 1,000,000 instead of 1000000.”

HIGH SCORES

“Every player wants to beat a game’s high score, so let’s track and report high scores to give players something to work toward. We’ll store high scores in GameStats:”

```python
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # High score should never be reset.
        self.high_score = 0
```

“**Because the high score should never be reset, we initialize high_score in init() rather than in reset_stats().**
Next, we’ll modify Scoreboard to display the high score. Let’s start with the **init**() method:”

```python
# Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
```

The high score will be displayed separately from the score, so we need a new method, prep_high_score(), to prepare the high-score image ❶.
Here’s the prep_high_score() method:

```python
def prep_high_score(self):
        """Turn the high score into a rendered image."""
❶         high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
❷         self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
❸         self.high_score_rect.centerx = self.screen_rect.centerx
❹         self.high_score_rect.top = self.score_rect.top
```

```python
def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
```

“To check for high scores, we’ll write a new method, check_high_score(), in Scoreboard:”

```python
 def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
```

**“The method check_high_score() checks the current score against the high score. If the current score is greater, we update the value of high_score and call prep_high_score() to update the high score’s image.**

“We need to call check_high_score() each time an alien is hit after updating the score in _check_bullet_alien_collisions():”

```python
   def _check_bullet_alien_collisions(self):
        --snip--
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        --snip--
```

DISPLAYING THE LEVEL

To display the player’s level in the game, we first need an attribute in GameStats representing the current level. To reset the level at the start of each new game, initialize it in reset_stats():”

```python
def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
```

“To have Scoreboard display the current level, we call a new method, prep_level(), from **init**():”

```python
  def __init__(self, ai_game):
        --snip--
        self.prep_high_score()
        self.prep_level()
```

```python
def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
❶         self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
❷         self.level_rect.right = self.score_rect.right
❸         self.level_rect.top = self.score_rect.bottom + 10
```

The prep_level() method creates an image from the value stored in stats.level ❶ and sets the image’s right attribute to match the score’s right attribute ❷. It then sets the top attribute 10 pixels beneath the bottom of the score image to leave space between the score and the level ❸.

“We also need to update show_score():

```python
def show_score(self):
        """Draw scores and level to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
```

“We’ll increment stats.level and update the level image in _check_bullet_alien_collisions():”

```python
def _check_bullet_alien_collisions(self):
        --snip--
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
```

“If a fleet is destroyed, we increment the value of stats.level and call prep_level() to make sure the new level displays correctly.
To ensure the level image updates properly at the start of a new game, we also call prep_level() when the player clicks the Play button:

Note
In some classic games, the scores have labels, such as Score, High Score, and Level. We’ve omitted these labels because the meaning of each number becomes clear once you’ve played the game. **To include these labels, add them to the score strings just before the calls to font.render() in Scoreboard.**

DISPLAYING THE NUMBER OF SHIPS

**Finally, let’s display the number of ships the player has left, but this time, let’s use a graphic.** To do so, we’ll draw ships in the upper-left corner of the screen to represent how many ships are left, just as many classic arcade games do.

**First, we need to make Ship inherit from Sprite so we can create a group of ships:**

```python
import pygame
from pygame.sprite import Sprite

❶ class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
❷         super().__init__()
        --snip--
```

```python
def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        --snip--
        self.prep_level()
        self.prep_ships()
```

“We assign the game instance to an attribute, because we’ll need it to create some ships. We call prep_ships() after the call to prep_level().

```python
   def prep_ships(self):
        """Show how many ships are left."""
❶         self.ships = Group()
❷         for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
❸             ship.rect.x = 10 + ship_number * ship.rect.width
❹             ship.rect.y = 10
❺             self.ships.add(ship)
```

“The prep_ships() method creates an empty group, self.ships, to hold the ship instances ❶. To fill this group, a loop runs once for every ship the player has left ❷. Inside the loop, we create a new ship and set each ship’s x-coordinate value so the ships appear next to each other with a 10-pixel margin on the left side of the group of ships ❸. We set the y-coordinate value 10 pixels down from the top of the screen so the ships appear in the upper-left corner of the screen ❹. Then we add each new ship to the group ships ❺.

“Now we need to draw the ships to the screen:

```python
def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
```

“To display the ships on the screen, we call draw() on the group, and Pygame draws each ship.”

“To show the player how many ships they have to start with, we call prep_ships() when a new game starts. We do this in _check_play_button() in AlienInvasion:”

```python
   def _check_play_button(self, mouse_pos):
        --snip--
        if button_clicked and not self.game_active:
            --snip--
            self.sb.prep_level()
            self.sb.prep_ships()
            --snip--”
```

“We also call prep_ships() when a ship is hit, to update the display of ship images when the player loses a ship:”

```python
def _ship_hit(self):
        """Respond to ship being hit by alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            --snip--
```

“We call prep_ships() after decreasing the value of ships_left, so the correct number of remaining ships displays each time a ship is destroyed.”

**We ave seen how to display information in textual and non-textual ways.**

RECAP: CIRCULAR REFERENCES OR MUTUAL DEPENDENCES

```python
class AlienInvasion:
    def __init__(self):
        self.sb = Scoreboard(self)  # Passes itself to Scoreboard

class Scoreboard:
    def __init__(self, ai_game):
        self.ai_game = ai_game  # Stores reference to AlienInvasion

```

Think of `AlienInvasion` as a game engine.

- `Scoreboard` is a module that plugs into it.
- `Scoreboard` reads values from the engine (`self.ai_game`), but it never **creates** or **owns** the engine.