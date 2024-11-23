
# Let's Learn Python: Lists and Loops! 🐍

Hi everyone! 🎉 Welcome to your Python programming lesson. Today, we’ll learn about **lists** and **loops** while creating a fun game called "Simon Says." Follow these steps, practice the concepts, and by the end, you’ll have written your own program!

---

## Tips Before You Start 💡

- You can use **[w3schools](https://www.w3schools.com/python/)** to look up Python topics if you get stuck.
- Save **each program separately** in a folder on your computer. For example, you can name the files `activity1.py`, `activity2.py`, and so on.
- At the end of each activity, remember to **save your work** before moving on to the next one.

---

## What You'll Learn 🧠

By the end of this lesson, you’ll be able to:
1. Create and use **lists** in Python.
2. Understand how to repeat actions using **loops**.
3. Write your own Python programs with lists and loops.
4. Make a fun game called **Simon Says!**

---

## Step 1: Practice the Basics 🖥️

Before we make the game, let’s practice some basics. Follow these steps, try the code, and see what happens!

### **1.1 Create a List**
A **list** is a way to store many items in one place.

#### Code:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Prints the entire list
print(fruits[0])  # Prints the first item
print(fruits[2])  # Prints the third item
```

---

### **1.2 Add Items to a List**
We can use `.append()` to add new items to a list.

#### Code:
```python
fruits.append("grape")
print(fruits)
```

---

### **1.3 Randomly Pick Items**
We can use `random.choice()` to pick a random item from a list.

#### Code:
```python
from random import choice
print(choice(fruits))  # Picks a random fruit
```

---

## Step 2: Build Simon Says 🎲

Now that we’ve practiced the basics, let’s create a fun game step by step!

---

### Start the Game
```python
simon_says = ["Hands on head", "Right hand up"]
from random import choice
print(f"Simon says {choice(simon_says)}")
```

---

Save after each section! Enjoy coding! 🎉

