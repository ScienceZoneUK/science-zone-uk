# Functions in Python

Welcome to this step-by-step GitHub tutorial on **functions** in Python. This tutorial is designed to guide you through the basics of creating and using functions, with examples and challenges to help you practice.

---

## 1. What is a Function?
A **function** is a reusable block of code that performs a specific task. Functions help make your code more organized and efficient.

### Example: A Simple Function
```python
# Simple Function that packages code into a named block
def greet():
    print("Hello Deadpool")
    print("How do you do T-Ray?")
    print("Isn't the weather nice?")

# Call the function
greet()
```
### Output:
```
Hello Deadpool
How do you do T-Ray?
Isn't the weather nice?
```

---

## 2. Functions with Inputs
Functions can accept **inputs** (called parameters) to make them more flexible.

### Example: Function with One Parameter
```python
# Function that allows for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

# Call the function
greet_with_name("Billie")
```
### Output:
```
Hello Billie
How do you do Billie?
```

---

## 3. Parameters vs. Arguments
- **Parameter**: The variable name in the function definition (e.g., `name` in `greet_with_name(name)`).
- **Argument**: The actual value you pass when calling the function (e.g., "Billie").

---

## 4. Challenge: Life in Weeks
I was reading an article by Tim Urban called "Your Life in Weeks," and it made me realize how little time we actually have. Let’s write a function to calculate how much time is left if we live until 90 years old.

### Task:
Create a function called `life_in_weeks()` that:
1. Takes your current age as an input.
2. Calculates the number of weeks you have left until age 90.
3. Prints the result using an f-string.

### Pseudo Code:
1. Define a function called `life_in_weeks`.
2. Accept an input parameter `current_age`.
3. Calculate the number of years left by subtracting `current_age` from 90.
4. Convert the years left into weeks by multiplying by 52.
5. Use an f-string to print the result in the format: "You have x weeks left."

### Test It Out:
Input: `25`

### Expected Output:
```
You have 3380 weeks left.
```

---

## 5. Summary
Functions make your code:
- **Reusable**: Write once, use many times.
- **Readable**: Name your functions clearly to make your code self-explanatory.
- **Organized**: Break your program into smaller, manageable pieces.

---

## 6. Next Steps
1. Modify the `life_in_weeks` function to include days and months.
2. Create a function that calculates time left based on a custom lifespan.
3. Experiment with functions that take multiple inputs.

Keep practicing and experimenting with functions to become a Python pro!

---

**Happy Coding!**
