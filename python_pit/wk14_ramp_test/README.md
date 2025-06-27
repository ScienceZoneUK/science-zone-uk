# 🐍 Python Power-Up Tower!  
## 🎮 How far can you climb?

### ⏱️ Time: 1 hour 15 mins  
👧🏽 For: Young Coders  
🧠 Goal: Practice input, strings, loops, lists, functions & more!  
💡 Need help? Use **[w3schools.com/python](https://www.w3schools.com/python)** – it's super helpful!
☠️ Completely stuck? go here!!

---

## 🧾 PYTHON CHEAT SHEET

```python
# INPUT & PRINT
name = input("What’s your name?")
print("Hello", name)

# NUMBERS & MATH
x = int(input("Enter a number: "))
y = int(input("Another: "))
print("Sum:", x + y)

#Print tricks
print("#", end="") # removes the line break /n
print("#", end="")
print("#", end="")
print("#")
print("#")
print("#")


# STRINGS
text = "hello"
print(text.upper())     # HELLO
print(text[0])          # h
print(len(text))        # 5

# FOR LOOP
for i in range(5):
    print(i)

# NESTED LOOP
for i in range(2):
    for j in range(3):
        print(i, j)

# FUNCTION (print)
def greet():
    print("Hello there!")

# FUNCTION (return)
def add(x, y):
    return x + y

# LIST
foods = ["pizza", "burger"]
foods.append("sushi")
print(foods[0])

# DICTIONARY
person = {"name": "Sam", "age": 11}
print(person["name"])
```

---

# 🧱 Level 0: WARM-UP – Say Hello (5 mins)
🧪 **Task:** Ask for the user’s name and say hello.  
✍️ **Pseudocode:**
```
Ask for name
Print greeting using their name
```

---

# 🧱 Level 0.5: MATHS MAGIC (5 mins)
🧪 **Task:** Ask for two numbers and print their total.  
✍️ **Pseudocode:**
```
Ask for two numbers
Turn them into integers
Add and print the result
```

---

# ✂️ Level 1: STRING MAGIC (10 mins)
🧪 **Task:** Ask for your favorite animal. Print:
- All uppercase
- How many letters
- First letter

✍️ **Pseudocode:**
```
Ask for animal
Print upper version
Print length
Print first letter
```

---

# 🌟 Level 2: STAR POWER (10 mins)
🧪 **Task:** Ask for a number. Print that many `*` stars using a loop.  
💥 **Bonus:** Make a triangle using nested loops.

✍️ **Pseudocode:**
```
Ask for number
Repeat that many times
    Print a star
```

---

# 🧩 Level 3: BOX BUILDER (10 mins)
🧪 **Task:** Ask for width and height. Print a box of `#` characters.  
✍️ **Pseudocode:**
```
Ask for width and height
Outer loop = height
Inner loop = width
    Print '#' without new line *hint- look at cheat sheet
Print new line after each row
```

---

# 🧠 Level 4: SAY HELLO FUNCTION (5 mins)
🧪 **Task:** Create a function `greet()` that prints “Hello, brave coder!”

✍️ **Pseudocode:**
```
Define greet()
Inside it, print message
Call greet()
```

---

# 🧠 Level 5: MATH FUNCTION (10 mins)
🧪 **Task:** Make a function that takes two numbers and returns the product.  
✍️ **Pseudocode:**
```
Define function with two parameters
Return their product
Call function with inputs
Print the result
```

---

# 🍕 Level 6: YUM LIST (10 mins)
🧪 **Task:** Make a list of 3 favorite foods.  
- Print each with: “Yum! I love [food]!”
- Add another food using `.append()`

✍️ **Pseudocode:**
```
Create list
Loop through list
    Print custom message
Add one more
Loop again
```

---

# 🧠 Level 7: PET PROFILE (10 mins)
🧪 **Task:** Create a dictionary like this:
```python
pet = {"name": "Luna", "type": "Dog", "age": 3}
```
Print:  
> “My pet Luna is a 3-year-old Dog.”

**Bonus:** Ask for a new age and update it.

✍️ **Pseudocode:**
```
Make dictionary
Print message using keys
Ask for new age
Update and print again
```

---

# 🎓 FINAL CHALLENGE! (Last 5 mins)
🧪 **Task:** Ask 3 friends for their favorite game. Store in a list. Use a function to print:  
> “Cool choice: [game]!”

✍️ **Pseudocode:**
```
Create empty list
Repeat 3 times:
    Ask for game
    Add to list
Define function to print message
Loop through list, call function
```
