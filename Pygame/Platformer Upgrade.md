# Upgrading Platformer in Pygame

We are going to modify and upgrade our Pygame Platformer

## Scrolling Screen

We need to add a new method/function in our Level Class to make the screen scroll as the player moves

Below the Level Class:
Copy this code into your python editor!

```python
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
```

Next we need to set a attribute in the Level class aswell to keep track of how far the screen has scrolled
Inside the init method, add this to your code:

```python
    #def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        #self.platform_list = pygame.sprite.Group()
        #self.enemy_list = pygame.sprite.Group()
        #self.player = player

        # How far this world has been scrolled left/right
        self.world_shift = 0
```

## New Level

We are going to create a new level for the player to get to, once the screen has scrolled far enough.
Copy this code into your python editor!

```python
# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -1000
 
        # Array with type of platform, and x, y location of the platform.
        level = [[210, 30, 450, 570],
                 [210, 30, 850, 420],
                 [210, 30, 1000, 520],
                 [210, 30, 1120, 280],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
```

## Updating Game Loop

Next we need to update the game loop to add our scrolling screen into the game.
First we must add our new level into the game:

```python
    # Create all the levels
    #level_list = []
    #level_list.append(Level_01(player))
    level_list.append(Level_02(player))
 
```

Then inside the game loop, after updating everything in the level, add this code to check whether we should scroll the screen.
It does this by checking if the player has moved a certain distance past the screen (set to 500 pixels at the momement)

```python
        # Update items in the level
        #current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
```

Finally, we check to see if the player has moved far enough to get to the next level, add this underneath still inside the game loop.

```python
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
```


## Try and run the game and see what happens!

Run "py *name*.py" in the command prompt to test your game! 


## Moving Platforms

We are going to create a new class, a moving platform that will move the player when they stand on it.
Copy this code into your python editor!

```python
class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0
 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
 
    player = None
 
    level = None
 
    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
```

Inside the players update method, add this at the end, this is to ensure that the player moves with the moving platform

```python
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
 
```

Next we need to set a attribute in the Level class to set a limit on how far the level can go
Inside the init method, add this to your code:

```python
        # How far this world has been scrolled left/right
        #self.world_shift = 0
        self.level_limit = -1000
```

## Add the Moving Platform to a Level

Inside one of the levels, add in this code to create a moving platform.

Copy this code into your python editor!

```python
        # Add a custom moving platform
        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
 
```

## Try and run the game and see what happens!

Run "py *name*.py" in the command prompt to test your game! 


## Customise your game!

Change the layouts and colours of the platforms and make 2 levels for the player to traverse!

```python

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]
 
```