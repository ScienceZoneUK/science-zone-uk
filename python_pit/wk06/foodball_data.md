
# Functions, Dictionaries, and Activities in Football

## Introduction
This README provides step-by-step instructions and examples for learning about functions that return values, as well as activities involving dictionaries and nested data structures. By the end of this guide, you will understand the importance of functions, how to use them effectively, and how to work with real-world problems like player ratings and team auctions.

---

## Table of Contents
1. [Functions That Return Values](#functions-that-return-values)
   - What are Functions that Return Values?
   - Examples and Explanations
   - Practice Activities

2. [Player Ratings Using Dictionaries](#player-ratings-using-dictionaries)
   - Problem Breakdown
   - Solution and Code
   - Activity

3. [Team Auction Using Nested Dictionaries](#team-auction-using-nested-dictionaries)
   - Problem Breakdown
   - Solution and Code
   - Activity

4. [Homework and Extensions](#homework-and-extensions)

---

## Functions That Return Values

### What Are Functions That Return Values?
The Python return statement marks the end of a function and specifies the value or values to pass back from the function. Return statements can return data of any type, including integers, floats, strings, lists, dictionaries, and even other functions.

### *Tip*
**Do not modify global variables inside of functions. It can cause misery in debugging.** Instead, use a function that returns a value and modify the global variable in the main code!
[W3Schools](https://www.w3schools.com/python/gloss_python_function_return_value.asp)

**Syntax:**
```python
def function_name(parameters):
    # Perform some operation
    return value
```

### Examples and Explanations
#### Example 1: Player Performance
```python
def calculate_player_score(goals, assists):
    score = (goals * 5) + (assists * 3)
    return score

output = calculate_player_score(2, 1)  # Call the function
print(output)  # Prints: 13
```

### Custom return function
Write a function to check if a player is eligible to play in the championship based on a minimum average score of 7.

```python
def can_play_championship():
   ???
   ???
   return True
```

#### Example 2: Is Matchday?
Create a function to check if today is a matchday by verifying the day of the week.
```python
def is_matchday(day):
    if day.lower() in ['saturday', 'sunday']:
        return True
    return False

# Test Cases
print(is_matchday('Saturday'))  # True
print(is_matchday('Wednesday'))  # False
```

#### Example 3: Check Hat-Trick
Write a function to check if a player has scored a hat-trick (3 or more goals in one match).
```python
def has_hat_trick(goals):
    if goals >= 3:
        return True
    return False

# Test Cases
print(has_hat_trick(3))  # True
print(has_hat_trick(2))  # False
```

### Practice Activity
- Write a function that calculates the total points of a team based on wins, draws, and losses.
- Write a function that checks if a player's name is a palindrome.

---

## Player Ratings Using Dictionaries

### Problem Breakdown
You have a dictionary of player scores. Write a program to assign player ratings based on the following criteria:
- **91 - 100:** World-Class
- **81 - 90:** Star Player
- **71 - 80:** Reliable Performer
- **70 or below:** Needs Improvement

### Solution and Code
```python
# Input data
player_scores = {
    'Messi': 95,
    'Ronaldo': 89,
    'Mbappe': 92,
    'Neymar': 78,
    'Haaland': 68
}

# Initialize player ratings dictionary


# Rating function that checks a score against the rating criteria
def get_rating(score):
   # Add code here to return the rating based on score



# Assign ratings using a loop, store ratings in a dictionary
for ???, ??? in ???.items():
    player_ratings[???] = get_rating(???)

# Output the dictionary
print(player_ratings)
```

### Activity
- Modify the program to include an additional rating category for scores between 50 and 60.

---

## Team Auction Using Nested Dictionaries

### Problem Breakdown
1. Collect team names and their bid amounts for a player.
2. Store each entry in a dictionary.
3. Determine the highest bidder.

### Solution and Code
```python
# A function that takes a dictionary, sorts it, and returns the highest bidder. Use the '.max(key=lambda x: x['???'])' method on the dictionary
def get_highest_bidder(bidders):
    highest_bidder = ???
    return ???

# Input logic
bidders = []
bidding_active = True

while bidding_active:
    team_name = input("Enter team name: ")
    bid = int(input("Enter bid amount: "))
   # Append a dictionary with team name and bid amount
   ???.append({????})

    more_bids = input("Are there more bids? (yes/no): ").lower()
    if more_bids == 'no':
        bidding_active = False

# Determine winner
winner = get_highest_bidder(bidders)
print(f"The winning team is {winner['Team']} with a bid of ${winner['Bid']}")
```

### Activity
- Add functionality to validate that bids are positive integers.
- Extend the program to handle ties by restarting the auction.

---

## Homework and Extensions

1. **Modify the Player Ratings Program**
   - Add a new rating category for scores below 50.
   - Allow users to input their own rating criteria.

2. **Extend the Team Auction**
   - Add an option for users to view all bids before deciding to add more.
   - Implement a feature to remove a bid.

3. **Practice Functions**
   - Write a function that calculates the total number of goals scored in a season.
   - Write a function that calculates the nth Golden Boot winner (Fibonacci-style).

---

## Final Notes
Understanding functions, dictionaries, and loops is essential for solving real-world problems. These football-themed activities build foundational skills that can be extended to more complex tasks in programming.
