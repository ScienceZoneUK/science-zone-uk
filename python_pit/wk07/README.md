# Instagram Followers Comparison Game

## Overview
This is a simple Python game where you compare Instagram followers between two accounts. The goal is to guess which account has more followers. The game shows a logo and a "vs" graphic, displays details about two accounts, and tracks your score as you play.

## Files in This Project
- **main.py**  
  The main file that runs the game.
- **art.py**  
  Contains ASCII art for the game, like the game logo and the "vs" image.
- **game_data.py**  
  Holds the data for Instagram accounts. Each account is stored as a dictionary with the following keys:  
  - `name`
  - `description`
  - `country`
  - `follower_count`

## How to Play
1. **Start the Game**  
   Run the `main.py` file.
2. **See the Comparison**  
   The game displays two accounts (labeled A and B) with details like name, description, and country.
3. **Make a Guess**  
   Type "A" or "B" to guess which account has more followers.
4. **Score Points**  
   If your guess is right, your score increases, and the game continues with new accounts.
5. **Game Over**  
   If your guess is wrong, the game ends and your final score is shown.
6. **Optional Replay**  
   You can later add a feature to let players choose to play again after the game ends.

## How to Set Up and Run the Game
1. **Run Python IDE of choice**  
   Start Thonny
2. **Download the Project**  
   Download or clone this project so that you have the `main.py`, `art.py`, and `game_data.py` files on your computer.
3. **Run the Game**  
   - Open your terminal or command prompt.
   - Navigate to the directory containing the files.
   - Type the following command and press Enter:
     ```
     python main.py
     ```
4. **Enjoy!**  
   Follow the on-screen instructions and have fun guessing!

## Tips for Young Coders
- **Break It Down:**  
  Divide your project into small, manageable parts. Start by writing functions for each task.
- **Test as You Go:**  
  Run your code frequently to see if each part works as expected.
- **Experiment:**  
  Once the basic game works, try adding new features or improvements.
- **Keep Learning:**  
  Enjoy the process of coding and remember that practice is key!

## Future Improvements
- **Replay Option:**  
  Add a feature to let players restart the game after it ends.
- **Enhanced Interface:**  
  Improve the display by clearing the screen between rounds or adding more graphics.
- **More Data:**  
  Expand the list of Instagram accounts in `game_data.py` to make the game even more interesting.

## License
This project is open-source and free to use for learning purposes.
