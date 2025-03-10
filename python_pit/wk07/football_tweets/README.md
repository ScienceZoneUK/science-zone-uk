# Python Workshop: Auto-Tweet Generator for a Football Commentator

## Lesson Overview
In this workshop, we will build a Python program step by step to generate automatic football commentary tweets. By the end of this lesson, students will understand:

- **Dictionaries (`dict`)**: How to store structured data.
- **Conditionals (`if` statements)**: How to check if an action exists before generating a tweet.
- **Ternary Expressions** (`"success" if success else "fail"`): A short way to write `if-else`.
- **Random Selection (`random.choice()`)**: How to pick a random phrase.
- **String Formatting (`.format()`)**: How to insert a player's name into the tweet.
- **User Input (`input()`)**: How to make the program interactive.

---

## Step 1: Understanding the Problem

### Discussion Questions
- What does a football commentator do?
- Can we write a Python program that automatically generates tweets about football actions?
- What information do we need to create a football commentary?

### Plan
1. Ask the user for:
   - **Player name** (Who did it?)
   - **Action** (What happened? e.g., goal, pass, tackle, save)
   - **Success or Failure** (Did they succeed?)
2. Use a **dictionary** to store different **phrases** for each action.
3. Pick a **random phrase** from the dictionary.
4. Replace `{player}` in the phrase with the real player’s name.
5. Display the generated tweet.

---

## Step 2: Storing Commentary Phrases in a Dictionary

### What is a Dictionary?
A **dictionary** in Python stores key-value pairs using curly braces `{}`.

### Example: Basic Dictionary
```python
# A dictionary storing simple football actions
phrases = {
    "goal": "GOAL! The crowd goes wild!",
    "pass": "A beautiful pass to the winger.",
    "tackle": "A solid tackle to win the ball back!"
}

print(phrases["goal"])   # Output: GOAL! The crowd goes wild!
print(phrases["tackle"]) # Output: A solid tackle to win the ball back!
```

### Expanding the Dictionary for Success & Failure
Now, we need different phrases for whether the action was **successful** or **not**.
```python
phrases = {
    "goal": {
        "success": ["GOAL! {player} smashes it in! ⚽🔥", "{player} finds the net! 🏆"],
        "fail": ["Oh no! {player} misses a golden opportunity! 😱", "{player} shoots... but it's off target! 😬"]
    }
}
```

---

## Step 3: Checking If an Action Exists

Before selecting a phrase, check if the action exists in our dictionary.
```python
action = "goal"

if action in phrases:
    print("This action exists in our dictionary!")
else:
    print("Unknown action!")
```

---

## Step 4: Using Ternary Expressions (`"success" if success else "fail"`)

### What is a Ternary Expression?
A ternary expression is a **shorter way** to write an `if-else` statement.

### Ternary Expression (Shorter Version)
```python
result = "success" if success else "fail"
```

---

## Step 5: Picking a Random Phrase

We use `random.choice()` to select a random phrase from a list.
```python
import random

phrases = ["GOAL! Amazing strike!", "What a hit!", "A stunning goal!"]
random_phrase = random.choice(phrases)
print(random_phrase)  # Picks a different phrase each time.
```

---

## Step 6: Formatting Strings with `{player}`

Replace `{player}` with the actual player's name using `.format()`.
```python
player_name = "Messi"
phrase = "GOAL! {player} smashes it in! ⚽🔥"
formatted_phrase = phrase.format(player=player_name)
print(formatted_phrase)  # Output: GOAL! Messi smashes it in! ⚽🔥
```

---

## Step 7: Building the Function

Now, put together the logic in a function.
```python
def generate_tweet(player, action, success):
    if action in phrases:
        result = "success" if success else "fail"
        phrase = random.choice(phrases[action][result]).format(player=player)
        return phrase
    else:
        return f"{player} did something unexpected! 🤷‍♂️"
```

---

## Step 8: Getting User Input

Complete the following code by filling in the blanks:
```python
import random

# Ask the user for details
player = input("Enter player name: ")
action = input("Enter action (goal, pass, tackle, save): ").lower()
success = input("Was it successful? (yes/no): ").lower() == "yes"

# Call the function and print the result
tweet = generate_tweet(player, action, success)
print("\nAuto-Tweet:\n", tweet)
```

---

## Step 9: Running the Program

### Example Run
```
Enter player name: Ronaldo
Enter action (goal, pass, tackle, save): goal
Was it successful? (yes/no): yes
```
**Output:**
```
Auto-Tweet:
 GOAL! Ronaldo smashes it in! ⚽🔥
```

---

## Extra Challenges
1. Add more football actions (e.g., dribble, foul, shot).
2. Store multiple tweets in a list.
3. Save tweets to a text file (e.g., `tweets.txt`).
4. Allow the user to generate multiple tweets without restarting the program.

---

Feel free to print this worksheet or modify it for your classroom sessions. Enjoy coding and have fun creating dynamic football commentary tweets!
