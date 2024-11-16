
# Python Workshop: Learn Coding Step by Step! 🎉

Welcome, young coder! In this workshop, we’ll explore Python basics and build your coding skills step by step. By the end, you’ll create a fun project: a **Band Name Generator**!

## What You’ll Learn
1. **Print statements** to display messages and create recipes.
2. **String manipulation** using concatenation and `\n`.
3. Using **`input()`** and storing inputs in variables.
4. Naming variables properly and debugging name errors.
5. Understanding **data types**: strings, integers, floats, and booleans.
6. **Type casting** and avoiding type errors.

---

## Saving Your Work

Each time you create a new program, **save it with a new file name**. For example:
- After Step 1, save it as `recipe.py`.
- After Step 5, save it as `band_name_generator.py`.

By the end, you’ll have **10+ Python programs**!

---

## Step 1: Print Statements - Write a Recipe

**What is `print()`?**
- The `print()` function is used to display messages on the screen.
- It can show words, numbers, or even the result of calculations!

**Example: Write a Recipe**
```python
print("Pancake Recipe:")
print("1. Mix flour, eggs, and milk.")
print("2. Pour into a pan and cook until golden brown.")
print("3. Serve with syrup!")
```

**Challenge:** Add line breaks using `\n` for readability.

---

## Step 2: String Concatenation and `\n`

**What is String Concatenation?**
- It’s a way to combine multiple strings into one.

**Using `\n`**
- `\n` adds a new line in your message.

**Examples**
```python
print("Hello, " + "world!")
print("Welcome to Python!\n
Let’s learn coding step by step.\n
Have fun!")
```

---

## Step 3: Using `input()`

**What is `input()`?**
- The `input()` function lets the user type something in. Your program can then use this input.

**Example**
```python
name = input("What’s your name? ")
print("Hello, " + name + "!")
```

**Challenge:** Ask for two inputs and combine them in a sentence.

---

## Step 4: Storing Input in Variables

**What are Variables?**
- Variables are like boxes where you store information. You can use the information later.

**Example**
```python
city = input("What city do you live in? ")
print("Wow! " + city + " sounds like a great place!")
```

**Challenge:** Ask for a favorite food and color, then create a message using both.

---

## Step 5: Naming Variables and Debugging Errors

**How to Name Variables**
- Use meaningful names.
- No spaces—use underscores `_` instead.
- Don’t use Python keywords (e.g., `print`, `input`).

**Example**
```python
user_name = input("What’s your name? ")
favorite_color = input("What’s your favorite color? ")
```

**Quiz:** Spot the error:
```python
1name = "Alice"
print(1name)
```

---

## Step 6: Name Error Quiz

**Why Do Name Errors Happen?**
- You might misspell a variable or use one before defining it.

**Example Quiz**
```python
Name = "Charlie"
print(name)  # What’s wrong here?
```

---

## Step 7: Project - Band Name Generator 🎸

**What Will You Create?**
- A fun program that generates a band name based on user inputs.

**Steps**
1. Create a greeting:
   ```python
   print("Welcome to the Band Name Generator!")
   ```

2. Ask for inputs:
   ```python
   city = input("What’s the name of the city you grew up in?")
   pet_name = input("What’s your pet’s name?")
   ```

3. Combine inputs:
   ```python
   print("Your band name could be " + city + " " + pet_name)
   ```

4. Add a blank line for clean output:
   ```python
   print(" ")
   ```

---

## Step 8: Understanding Data Types

**What are Data Types?**
- Data types define what kind of information a variable holds.

**Common Data Types**
1. **String**: Text, like `"Hello"`.
   ```python
   print("Hello"[0])  # Outputs: H
   ```

2. **Integer**: Whole numbers, like `123`.
   ```python
   print(123 + 345)  # Outputs: 468
   ```

3. **Float**: Decimal numbers, like `3.145`.
   ```python
   print(3.145)
   ```

4. **Boolean**: True/False values.
   ```python
   is_hungry = True
   print(is_hungry)
   ```

**Quiz**
What gets printed?
```python
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
```

---

## Step 9: Type Errors and Casting

**What are Type Errors?**
- A type error happens when you try to combine incompatible data types.

**Example**
```python
print("Angela has " + 7 + " characters")  # This causes an error!
```

**Using `type()`**
- Check a variable’s data type:
   ```python
   num_char = len("Angela")
   print(type(num_char))
   ```

**Type Casting**
- Change a variable’s type to avoid errors:
   ```python
   print("Angela has " + str(7) + " characters")
   ```

**Challenge**
Add up the digits of a number:
```python
two_digit_number = input("Type a two-digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))
```

---

Congratulations! You’ve completed the workshop. Keep practicing and building amazing Python programs!
