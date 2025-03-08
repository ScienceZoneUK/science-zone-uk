# Let's Learn Python: Lists and Loops! 🐍

Hi everyone! 🎉 Welcome to your Python programming lesson. Today, we’ll learn about **lists** and **loops** while creating a fun game called "Simon Says." 
Follow these steps, practice the concepts, and by the end, you’ll have written your own program!

---

## What You'll Learn 🧠

By the end of this lesson, you’ll be able to:
1. Create and use **lists** in Python.
2. Understand how to repeat actions using **loops**.
3. Write your own Python programs with lists and loops.
4. Make a fun game called **Simon Says!**

---

## Key Words to Remember 📝

Here are some important programming words we’ll use today:
- **List**: A way to store lots of items (like words or numbers) in one place.
- **Index**: The position of an item in a list. For example, the first item is at position `0`.
- **Append**: Add a new item to a list.
- **Loop**: A way to repeat actions in your program.

---

## Step 1: Practice the Basics 🖥️

Before we make the game, let’s practice some basics. Follow these steps, try the code, and see what happens! 
Remember to **save your program** after every step so you don’t lose your work. If you need extra help, 
you can look up examples on [W3Schools](https://www.w3schools.com/).

---

### **1.1 Create a List**
A **list** is a way to store many items in one place.

#### Code:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Prints the entire list
print(fruits[0])  # Prints the first item
print(fruits[2])  # Prints the third item
```
What to Do:
	1	Copy the code into your editor.
	2	Run it and see what happens.
	3	Change the items in the list to your favourite foods!
Don't forget to save your program!

1.2 Add Items to a List
We can use .append() to add new items to a list.
Code:
```python
fruits = ["apple", "banana"]
fruits.append("cherry")  # Add a new item
print(fruits)
```
What to Do:
	1	Add more fruits to the list.
	2	Print the list to see how it grows.
Don't forget to save your program!

1.3 Remove Items from a List
We can use .remove() to delete an item from a list.
Code:
```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")  # Remove an item
print(fruits)
```
What to Do:
	1	Try removing different items from the list.
	2	What happens if you try to remove something that’s not in the list?
Don't forget to save your program!

1.4 Use Random Numbers
We can use the random module to pick random numbers. This is great for games!
Code:
```python
from random import randint
random_number = randint(1, 10)  # Pick a random number between 1 and 10
print(random_number)
```
What to Do:
	1	Run the code a few times to see different random numbers.
	2	Try changing the range (e.g., 1 to 100).
Don't forget to save your program!

1.5 Access Items in a List Randomly
Let’s use a random number to pick an item from a list.
Code:
```python
from random import randint

fruits = ["apple", "banana", "cherry", "grape"]
index = randint(0, len(fruits) - 1)  # Pick a random index
print(fruits[index])
```
What to Do:
	1	Run the code and see which fruit gets picked.
	2	Add more items to the list and run it again.
Don't forget to save your program!

1.6 Repeat Actions with Loops
A loop repeats the same code multiple times.
Code:
```python
for number in range(5):  # Repeat 5 times
    print("Hello!")
```
What to Do:
	1	Run the code and count how many times it prints "Hello!"
	2	Change the 5 to 10 and run it again.
Don't forget to save your program!

1.7 Loop Through a List
You can use a loop to go through all the items in a list.
Code:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Print each fruit
```
What to Do:
	1	Run the code to see each item in the list printed one by one.
	2	Add more items to the list and run it again.
Don't forget to save your program!

1.8 Add Pauses with time.sleep()
You can make your program wait between actions using time.sleep().
Code:
```python
from time import sleep

print("Ready...")
sleep(2)  # Wait 2 seconds
print("Set...")
sleep(2)  # Wait another 2 seconds
print("Go!")
```
What to Do:
	1	Run the code to see the pauses.
	2	Change the number of seconds and see what happens.
Don't forget to save your program!

Step 2: Build the "Simon Says" Game 🎲
Now that we’ve practiced the basics, let’s create a fun game step by step!

Step 2.1: Start with a Simple Version
We’ll use a list to store the instructions for "Simon Says."
Code:
```python
simon_says = ["Hands on head", "Hands on ears", "Right hand up", "Left hand up"]
print("Pick a number between 0 and 3:")
index = int(input())  # Ask the player for a number
print(f"Simon says... {simon_says[index]}")  # Show the instruction
```
What to Do:
	1	Copy this code into your editor.
	2	Run it and enter different numbers (0, 1, 2, 3) to see what happens.
Don't forget to save your program!

Step 2.2: Add Randomisation
Let’s make "Simon Says" choose instructions randomly.
Code:
```python
from random import choice

simon_says = ["Hands on head", "Hands on ears", "Right hand up", "Left hand up"]
instruction = choice(simon_says)  # Pick a random instruction
print(f"Simon says... {instruction}")
```
What to Do:
	1	Copy this code and run it.
	2	Watch how the instructions change each time!
Don't forget to save your program!

Step 2.3: Repeat Instructions with Loops
Now we’ll make the game repeat 10 times.
Code:
```python
from time import sleep
from random import choice

simon_says = ["Hands on head", "Hands on ears", "Right hand up", "Left hand up"]

for _ in range(10):  # Repeat 10 times
    instruction = choice(simon_says)  # Pick a random instruction
    print(f"Simon says... {instruction}")
    sleep(2)  # Pause for 2 seconds
```
What to Do:
	1	Copy this code and run it.
	2	Watch as "Simon Says" gives 10 random instructions!
Don't forget to save your program!

Step 2.4: Add a Challenge
Sometimes "Simon Says" won’t say "Simon says..."! The player has to figure out when to follow the instructions.
Code:
```python
from random import choice
from time import sleep

simon_says = ["Hands on head", "Hands on ears", "Right hand up", "Left hand up"]
intros = ["Simon says...", ""]  # Sometimes leave it blank

for _ in range(10):
    intro = choice(intros)  # Randomly pick an intro
    instruction = choice(simon_says)  # Randomly pick an instruction
    print(f"{intro} {instruction}")
    sleep(2)
```
What to Do:
	1	Copy this code and run it.
	2	Watch how "Simon Says" sometimes doesn’t say "Simon says...!"
Don't forget to save your program!

Summary of What You Learned 🎓
	1	Lists: How to create, add, remove, and access items.
	2	Loops: How to repeat actions in your program.
	3	Randomisation: How to make your program pick random items.
	4	Game Logic: How to combine everything into a fun game.

Challenge Yourself! 🚀
Can you:
	1	Add more instructions to "Simon Says"?
	2	Keep score of how many correct actions the player does?
	3	End the game if the player messes up?
