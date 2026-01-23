# Maze Runner

## Let's create our game!

### Of course we start with our imports and constants (and a pop of colour)
<img width="453" height="569" alt="image" src="https://github.com/user-attachments/assets/404635d4-a2f5-4c19-9403-85e35c346d57" />

### We're going to need some classes
#### Player
<img width="836" height="595" alt="image" src="https://github.com/user-attachments/assets/797e6f63-c637-4796-8efc-cf5a7e4aeb7d" />

#### Coin
<img width="744" height="234" alt="image" src="https://github.com/user-attachments/assets/ed0fb041-5c11-4229-b144-2fb66c597670" />

### We're going to need some functions too
#### We need to generate the maze somehow
<img width="680" height="332" alt="image" src="https://github.com/user-attachments/assets/50654056-7034-4061-9a36-712fa81c38ee" />

#### To place coins in the maze
<img width="557" height="320" alt="image" src="https://github.com/user-attachments/assets/cd29a626-f35d-4fdd-9ffa-79e47a1c67e2" />

#### Now we need to draw the maze
<img width="760" height="217" alt="image" src="https://github.com/user-attachments/assets/2fd592d0-4ac3-4219-8790-7e9c79dc1318" />

#### We need to make everything work now (main function)
##### Generating maze, player stats, placing coins
<img width="653" height="472" alt="image" src="https://github.com/user-attachments/assets/289ae47b-2d1b-462a-b454-49b9012d0adc" />

##### While running loop
###### Setting up all the boolean variables & if game not won movement, coin collection & reach goal checker
<img width="788" height="1058" alt="image" src="https://github.com/user-attachments/assets/50b12e78-4caf-42cd-94f8-cef5a46f3712" />

###### Draw statements
<img width="799" height="841" alt="image" src="https://github.com/user-attachments/assets/6cd86a6d-b2b4-4ab3-8802-0231245db165" />

## No we can run our game...
What are we missing?

## Challenges
### Easy
1. Change the colors of: the player, walls, and/or background to create your own theme
3. Adjust the speed; can you make the player move faster or slower by changing the "self.speed" value
4. Add more coins, make more coins appear per level
5. Change maze size, make the maze bigger or smaller by changing "maze_width" and "maze_height"
### Medium
7. Add sound effects, use "pygame.mixer.Sound()" to add sounds when collecting coins or winning
8. Create power-ups, add special coins that give double points or temporary speed boost
9. Add enemies, create moving obstacles that reset the player's position if touched (or lose a life)
10. Timer challenge model, add a countdown timer where you must finish before time runs out
11. Particle effects, make coins sparkle or add a trail behind the player
12. Different coin values, create three different coin types and assign different points to them, eg. silver (50 pts), gold (100 pts), and diamond (250 pts)
