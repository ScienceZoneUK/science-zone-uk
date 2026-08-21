# Python Exercises --- Set 3

## Random Numbers & Simulation (1--5)

### 1. Dice Roll

Generate a random number between `1` and `6` and print it as a dice
roll. Use Python's `random` library.

### 2. Coin Flip

Randomly choose between `Heads` and `Tails` and print the result.

### 3. Two Dice Total

Roll two random dice and print the first dice, second dice, and total.

### 4. Random Password Number

Generate a random 4-digit number between `1000` and `9999`.

### 5. Rock, Paper, Scissors

Ask the user to enter `rock`, `paper`, or `scissors`. The computer
randomly chooses one too. Print who wins.

------------------------------------------------------------------------

# String Processing (6--10)

### 6. Initials Generator

Ask for a first name and surname and print the initials.

### 7. Email Checker

Ask for an email address and check whether it contains `@`. Print
`Valid email format` or `Invalid email format`.

### 8. Word Length Checker

Ask for a word. Print `Short` if fewer than 5 letters, `Medium` if 5--8
letters, otherwise `Long`.

### 9. Hidden Word

Print the first and last letter normally, but replace all letters in
between with `*`.

Example: `computer → c******r`

### 10. Remove Spaces

Ask for a sentence and create a new version without spaces.

**Challenge:** Do not use `.replace()`.

------------------------------------------------------------------------

# Nested Loops & Patterns (11--15)

### 11. Rectangle of Stars

Ask for a width and height and print a rectangle using `*`.

### 12. Triangle Pattern

Use loops to print:

``` text
*
**
***
****
*****
```

### 13. Number Triangle

Print:

``` text
1
12
123
1234
12345
```

### 14. Multiplication Grid

Print a multiplication grid from `1 × 1` to `5 × 5`.

### 15. Coordinate Printer

Use nested loops to print coordinates from `(0, 0)` through combinations
where both values range from `0` to `2`.

------------------------------------------------------------------------

# Lists with Different Operations (16--20)

### 16. Add User Items

Start with:

``` python
items = []
```

Ask the user to enter five items, add each to the list, and print the
final list.

### 17. Replace an Item

Given:

``` python
colours = ["red", "green", "blue", "yellow"]
```

Ask which index to replace, then ask for a new colour and update the
list.

### 18. Combine Two Lists

Combine:

``` python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
```

into `[1, 2, 3, 4, 5, 6]`.

### 19. Remove All Negative Numbers

Given:

``` python
numbers = [5, -2, 8, -7, 3, -1, 10]
```

Create a new list containing only positive numbers.

### 20. Double Every Value

Given:

``` python
numbers = [2, 4, 6, 8]
```

Create a new list where every number is doubled.

------------------------------------------------------------------------

# Dictionaries & Records (21--24)

### 21. Character Record

Create a dictionary for a game character containing `name`, `health`,
`level`, and `weapon`. Print each value.

### 22. Update Health

Given:

``` python
player = {
    "name": "Alex",
    "health": 100,
    "level": 3
}
```

The player takes `25` damage. Update and print the health.

### 23. Inventory Dictionary

Create an inventory dictionary with item quantities. Ask which item the
user wants to check and print its quantity.

### 24. Student Marks

Given:

``` python
marks = {
    "Maths": 72,
    "English": 65,
    "Computer Science": 88
}
```

Print only subjects where the score is `70` or above.

------------------------------------------------------------------------

# Functions with More Variety (25--28)

### 25. Character Counter

Create:

``` python
def count_character(text, character):
```

Return how many times `character` appears in `text`.

### 26. Clamp a Number

Create:

``` python
def clamp(number, minimum, maximum):
```

Return `minimum` if too small, `maximum` if too large, otherwise return
the number.

### 27. List Cleaner

Create:

``` python
def remove_zeroes(numbers):
```

Return a new list with all `0` values removed.

### 28. Username Validator

Create:

``` python
def valid_username(username):
```

Return `True` if the username has at least 5 characters and contains no
spaces. Otherwise return `False`.

------------------------------------------------------------------------

# File Handling (29--31)

### 29. Write to a File

Ask the user for their name and write it into `student.txt`.

### 30. Read from a File

Open `student.txt` and print its contents.

### 31. Save Scores

Given:

``` python
scores = [70, 82, 65, 91]
```

Write every score to `scores.txt`, with each score on a new line.

------------------------------------------------------------------------

# Problem-Solving Challenges (32--35)

### 32. ATM Withdrawal

Start with:

``` python
balance = 500
```

Ask how much to withdraw. The user cannot withdraw more than the balance
or withdraw `0`/a negative number. Otherwise subtract it and print the
remaining balance.

### 33. Shopping Basket

Given:

``` python
prices = [2.50, 1.20, 3.75, 4.00]
```

Calculate the total. If it is more than £10, apply a 10% discount. Print
the original total, discount, and final total.

### 34. Simple Voting System

Ask 5 users to vote for `A` or `B`. Count the votes and print the
winner. If equal, print `Draw`.

### 35. Mini Game Scoreboard

Given:

``` python
players = [
    ["Alex", 120],
    ["Sam", 95],
    ["Amy", 150]
]
```

Print every player's name and score, the highest-scoring player, and the
average score.

**Challenge:** Find the highest score without using `max()`.
