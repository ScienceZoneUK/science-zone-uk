# 📝 Python Workshop: Lists & Arrays – Keeping Your Data Together!

Target Age: 10–12 years
Length: 1.5 hours
IDE: Thonny
Theme: Introduction to Lists & Arrays in Python
## 1️⃣ Why This Topic is Important (10 minutes – discussion)

Goal: Students understand why lists/arrays matter in real-world coding.

Discussion prompts:

    - "Imagine you’re building a game that tracks scores for 10 players. How would you store all the scores?"

    - "What if your program needed to store the names of 1,000 animals? Would you create 1,000 variables? 😅"

    Relatable examples:

        - Music playlist – songs stored together.

        - Shopping list – you don’t write each item on a separate page.

        - Minecraft inventory – all your items in one chest.

Key takeaway:
Lists (and arrays) are like containers that can hold many pieces of data together in one place — easier to manage, update, and use.
## 2️⃣ Coding Concepts for This Workshop

Students will learn:

    - What an array/list is.

    - How to create a list in Python.

    - How to store multiple values in a list.

    - Indexing: Accessing items from a list.

    - Modifying list items.

    - Appending and removing elements.

    - Why a list is better than multiple variables in many cases.

    - Printing a list neatly.

    - Looping through a list (bonus if time allows).

## 3️⃣ Problem & Project Requirements

Mini-project:
📜 "Design a Python program that stores the names and scores of players in a game, then allows you to update scores and print them out."

Requirements:

    - Store player names in a list.

    - Store player scores in a separate list.

    - Access and print individual scores.

    - Update a score when a player earns points.

    - Add a new player during the game.

    - Remove a player who leaves.

## 4️⃣ Step-by-Step Activities with Testable Code
### Activity 1: Making Our First List (10 minutes)

Concept: Creating and printing lists.

# Let's make a list of our favorite fruits
```
fruits = ["apple", "banana", "cherry"]
print(fruits)
```
✅ Test: Students see a printed list in Thonny.
🔍 Discussion: "Why is it easier than making fruit1, fruit2, fruit3?"
### Activity 2: Accessing Items (10 minutes)

Concept: Indexing.
```
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # First fruit
print(fruits[2])  # Last fruit
```
✅ Test: Change indexes and predict the output.
⚠️ Introduce IndexError and how to avoid it.
### Activity 3: Updating List Items (10 minutes)
```
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)
```
✅ Test: Everyone changes their own list items.
### Activity 4: Adding & Removing Items (15 minutes)

Concepts: append(), remove()
```
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)
```
✅ Test: Add/remove their own favorite fruit.
### Activity 5: Why Lists Are Better (10 minutes)

Demonstration:

    - Create 5 separate variables for player names.

    - Compare to creating 1 list with 5 names.

    - Show how easy it is to loop through a list compared to separate variables.

#### Without lists
```
p1 = "Alex"
p2 = "Sam"
p3 = "Jamie"
```
#### With a list
```
players = ["Alex", "Sam", "Jamie"]
for p in players:
    print(p)
```
### Activity 6: Player Score Project Build (20 minutes)

Step-by-step:

#### Step 1: Create player and score lists
```
players = ["Alex", "Sam", "Jamie"]
scores = [0, 0, 0]
```
#### Step 2: Print the players and their scores
```
print(players[0], "has", scores[0], "points")
print(players[1], "has", scores[1], "points")
print(players[2], "has", scores[2], "points")
```
#### Step 3: Update a score
```
scores[1] += 10  # Sam earns points
```
#### Step 4: Add a new player
```
players.append("Taylor")
scores.append(0)
```
#### Step 5: Remove a player
```
players.remove("Alex")
scores.pop(0)
```
#### Step 6: Print final scoreboard
```
print("Final scores:")
for i in range(len(players)):
    print(players[i], ":", scores[i])
```
✅ Test: Students change names, points, and see updates in real time.
### Activity 7 (Bonus): Loops & Lists (5 minutes)

Make the scoreboard print automatically without repeating print lines.
```
for i in range(len(players)):
    print(players[i], "has", scores[i], "points")
```
## 5️⃣ Wrap-Up & Reflection (10 minutes)

    Q: "What is a list?"

    Q: "How is it different from using multiple variables?"

    Q: "Why might a game developer use a list?"

    Mini-quiz: Teacher says a requirement, students write 1–2 lines of code to solve it.

    Encourage experimenting in Thonny at home.
