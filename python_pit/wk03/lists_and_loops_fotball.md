
# Python Workshop: Lists, Loops, and Building a Football Team App

Welcome to this workshop! Today, we’ll learn about **lists** and **loops** in Python. By the end, we’ll build a fun app that lets users guess which country a football team belongs to!

---

## 📝 Workshop Objectives

1. Understand what lists are and how to create them.
2. Learn how to loop through lists using `for` loops.
3. Build an interactive Python app using these concepts.

---

## 🛠️ Step 1: Getting Started with Python Lists

### What are Lists?

A **list** in Python is a collection of items. You can think of it like a box containing multiple things, such as names of football teams or countries.

### Example:

```python
football_teams = ["Manchester United", "Barcelona", "Bayern Munich"]
countries = ["England", "Spain", "Germany"]
```

### Mini Exercise 1:

1. Open Python or your IDE (like Thonny or VS Code).
2. Create a list of your favorite football teams.
3. Print the list.

**Example Code:**
```python
my_favorite_teams = ["Chelsea", "Real Madrid", "Paris Saint-Germain"]
print(my_favorite_teams)
```

---

## 🛠️ Step 2: Looping Through Lists

### What is a `for` Loop?

A `for` loop helps you go through each item in a list, one at a time. It's like saying: "For each team in the list, do something."

### Example:

```python
football_teams = ["Liverpool", "Juventus", "Ajax"]

for team in football_teams:
    print(team)
```

### Mini Exercise 2:

1. Create a list of countries.
2. Write a `for` loop to print each country.

**Example Code:**
```python
countries = ["Italy", "Netherlands", "Portugal"]
for country in countries:
    print(country)
```

---

## 🛠️ Step 3: Combining Lists and Loops

We can use a loop to work with two lists together. For example, if we want to say where each football team is from:

```python
football_teams = ["AC Milan", "Atletico Madrid", "PSG"]
countries = ["Italy", "Spain", "France"]

for i in range(len(football_teams)):
    print(f"{football_teams[i]} is from {countries[i]}")
```

### Mini Exercise 3:

1. Create two lists: one with at least 3 football teams and another with their corresponding countries.
2. Write a loop that prints: "<team> is from <country>."

---

## 🛠️ Step 4: Building the Football Team App

### App Overview:

- The app will show a football team name.
- The user will guess which country the team belongs to.
- If the guess is correct, they score a point!

### Final Code Walkthrough:

#### Step 1: Set Up the Lists
```python
football_teams = ["Chelsea", "Real Madrid", "Bayern Munich"]
countries = ["England", "Spain", "Germany"]
```

#### Step 2: Add User Interaction
We will ask the user to input their guess.

```python
user_score = 0  # Keep track of the score

for i in range(len(football_teams)):
    print(f"Which country is {football_teams[i]} from?")
    guess = input("Your answer: ")
    
    if guess.lower() == countries[i].lower():
        print("Correct!")
        user_score += 1
    else:
        print(f"Wrong! The correct answer is {countries[i]}")
```

#### Step 3: Show the Final Score
At the end of the game, show the user’s score.

```python
print(f"Your final score is: {user_score}/{len(football_teams)}")
```

---

## 🏆 Putting It All Together: Full Code

```python
# Lists of football teams and their countries
football_teams = ["Chelsea", "Real Madrid", "Bayern Munich"]
countries = ["England", "Spain", "Germany"]

# Initialize score
user_score = 0

# Loop through each team
for i in range(len(football_teams)):
    print(f"Which country is {football_teams[i]} from?")
    guess = input("Your answer: ")
    
    # Check the answer
    if guess.lower() == countries[i].lower():
        print("Correct!")
        user_score += 1
    else:
        print(f"Wrong! The correct answer is {countries[i]}")

# Show the final score
print(f"Your final score is: {user_score}/{len(football_teams)}")
```

---

## 🚀 Challenge: Expand the App

1. Add more teams and countries to the lists.
2. Add a feature to keep playing until the user types "quit."
3. Make the app show random teams instead of going in order.

---

## 🎉 Congratulations!

You’ve learned how to use lists and loops to build an interactive app. Keep practicing and try adding your own features to make it even better!
