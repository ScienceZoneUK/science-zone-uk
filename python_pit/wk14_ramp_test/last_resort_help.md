# 🐍 Python Power-Up Tower – Starter Code

This starter file includes code templates for each challenge. Fill in the blanks to complete the tasks!

---

## 🧱 Level 0: WARM-UP – Say Hello

```python
# Ask the user for their name and greet them
name = input("What is your name? ")
print("Hello, " + ________)
```

---

## 🧱 Level 0.5: MATHS MAGIC

```python
# Ask for two numbers and print their total
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
total = _________
print("The total is", total)
```

---

## ✂️ Level 1: STRING MAGIC

```python
# Ask for favorite animal and do string tasks
animal = input("What is your favorite animal? ")
print(animal.________())
print("It has", ________, "letters.")
print("First letter is", animal[__])
```

---

## 🌟 Level 2: STAR POWER

```python
# Print stars using a loop
count = int(input("How many stars? "))
for i in range(________):
    print("*")
```

---

## 🧩 Level 3: BOX BUILDER

```python
# Build a box with nested loops
width = int(input("Width? "))
height = int(input("Height? "))

for i in range(height):
    for j in range(width):
        print("#", end="")
    print()
```

---

## 🧠 Level 4: SAY HELLO FUNCTION

```python
# Create a function to greet
def greet():
    print("Hello, brave coder!")

greet()
```

---

## 🧠 Level 5: MATH FUNCTION

```python
# Multiply two numbers using a function
def multiply(a, b):
    return _________

result = multiply(3, 4)
print("The result is", result)
```

---

## 🍕 Level 6: YUM LIST

```python
# List of favorite foods
foods = ["pizza", "burger", "sushi"]
for food in _________:
    print("Yum! I love", food)

foods.append("tacos")

for food in foods:
    print("Yum! I love", food)
```

---

## 🧠 Level 7: PET PROFILE

```python
# Create and update a dictionary
pet = {"name": "Luna", "type": "Dog", "age": 3}
print("My pet", pet["name"], "is a", pet["age"], "year-old", pet["type"])

new_age = int(input("Enter a new age: "))
pet["age"] = ________
print("Now", pet["name"], "is", pet["age"], "years old.")
```

---

## 🎓 FINAL CHALLENGE

```python
# Ask for games and print them using a function
games = []
for i in range(3):
    game = input("What's your favorite game? ")
    games.append(game)

def shout_game(name):
    print("Cool choice:", name)

for g in games:
    shout_game(g)
```
