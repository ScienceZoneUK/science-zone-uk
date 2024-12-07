
# Python Workshop: Lists and Loops for 12-Year-Olds

## What You’ll Learn Today:
- How to create and use lists.
- How to loop through lists to access their items.
- Cool challenges like finding the highest score and building a password generator!

---

## Step 1: What Are Lists?

A list is a collection of items, like a shopping list or a list of your friends’ names. You can store numbers, words, or a mix of both in a list.

To create a list in Python, place elements inside square brackets. Each item is separated by commas. An empty list is simply a pair of empty brackets.

Computer languages deal with numbers. When you want to use words, you’ll need to create a list of strings. Strings are a collection of characters. To make a list composed of strings, you place each of them inside quotation marks.

In Python, a string of characters is encoded. This conversion process happens with the use of Python Unicode, which covers every character found in languages around the world!

A list can contain any object or even another list (called a sublist). Lists that contain sublists are known as nested lists. Elements in a list are numbered 0 (first element) to -1 (last item).

### Example:
```python
# A list of numbers
scores = [100, 200, 300]

# A list of names
friends = ["Alice", "Bob", "Charlie"]

# A mixed list
mixed = [42, "banana", 3.14]
```

---

## Step 2: Using Loops to Access Lists

Loops let you go through each item in a list, one by one. This is called **iterating**.

### Example:
```python
# A list of animals
animals = ["cat", "dog", "rabbit"]

for animal in animals:
    print(f"I have a {animal}.")
```

**Output:**
```
I have a cat.
I have a dog.
I have a rabbit.
```

### Using Loops with Indexes

Sometimes, you need to know the position of items in a list. Use a combination of `range()` and `len()` to loop through lists with their indexes.

### Example:
```python
# A list of colors
colors = ["red", "blue", "green"]

for i in range(len(colors)):
    print(f"Color at index {i} is {colors[i]}.")
```

**Output:**
```
Color at index 0 is red.
Color at index 1 is blue.
Color at index 2 is green.
```

---

## Step 3: Challenges

### Challenge 1: Find the Highest Score
You have a list of student scores. Your job is to find the highest one!

#### Setup Code:
```python
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
```

#### What To Do:
1. Start with a variable called `high_score` and set it to `0`.
2. Loop through the `student_scores` list.
3. If a score is higher than `high_score`, update `high_score`.
4. Print the highest score after the loop finishes.

#### Pseudocode:
```python
# 1. Create a variable `high_score` and set it to 0.
# 2. Loop through `student_scores`.
# 3. If the score is greater than `high_score`, update `high_score`.
# 4. Print `high_score` after the loop ends.
```

---

### Challenge 2: Count Long Names
Count how many names in the list have more than 4 letters.

#### Setup Code:
```python
names = ["Liam", "Olivia", "Emma", "Sophia", "Ava"]
```

#### What To Do:
1. Create a variable `count` and set it to `0`.
2. Loop through the `names` list.
3. If the name has more than 4 letters, increase the `count`.
4. Print the total count after the loop.

#### Pseudocode:
```python
# 1. Create a variable `count` and set it to 0.
# 2. Loop through `names`.
# 3. If the length of the name is greater than 4, increase `count`.
# 4. Print `count` at the end.
```

---

### Challenge 3: Password Generator

Let’s build something fun—a **password generator**! We’ll create random passwords using letters, numbers, and symbols.

#### Setup Code:
```python
from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?
"))
nr_symbols = int(input("How many symbols would you like?
"))
nr_numbers = int(input("How many numbers would you like?
"))
```

#### What To Do:
1. Start with an empty string called `password`.
2. Use a loop to add random letters, symbols, and numbers to `password`.
3. Shuffle the characters to mix them up.
4. Print the final password.

#### Pseudocode:
```python
# 1. Create an empty string `password`.
# 2. Use a loop to add random letters, numbers, and symbols to `password`.
# 3. Convert `password` to a list and shuffle it.
# 4. Convert the list back to a string and print it.
```

---

## Recap of What We Learned:
1. **Lists:**
   - Store multiple items in one variable.
   - Use indexes to access items.

2. **Loops:**
   - Use `for` loops to go through lists.
   - Combine loops with `range()` and `len()` to access items by index.

3. **Challenges:**
   - Finding the highest score.
   - Counting long names.
   - Generating random passwords.

---

## Keep Practicing!
Try experimenting with other list challenges:
- Sort a list of numbers.
- Find the smallest number in a list.
- Create a program that removes duplicates from a list.

**Happy Coding! 🎉**
