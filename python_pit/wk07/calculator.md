# Calculator Challenge

## Introduction
Welcome to the **Calculator Challenge!** In this challenge, you will create a Python program that can perform basic mathematical calculations using functions stored in a dictionary. This activity will help you understand how functions can be stored as variables and used dynamically in a program.

## Learning Objectives
- Learn how to store functions as variable values.
- Use a dictionary to map mathematical operations to functions.
- Implement user input handling in Python.
- Use loops to allow continued calculations.

---

## Getting Started

### Storing Functions as Variables
In Python, you can store a function in a variable just like any other value. For example:

```python
def add(n1, n2):
    return n1 + n2
    
my_favourite_calculation = add
print(my_favourite_calculation(3, 5))  # Outputs: 8
```

In your starting file, you'll find a dictionary that references different mathematical calculations that your calculator can perform. Try it out and ensure that it works for addition, subtraction, multiplication, and division.

```python
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,  # Use "*" to match the input prompt
}
```

---

## Step-by-Step Instructions

### 1
**TODO:** Write out the other three functions:
- `subtract(n1, n2)` should return `n1 - n2`.
- `multiply(n1, n2)` should return `n1 * n2`.
- `divide(n1, n2)` should return `n1 / n2`.

### 2
**TODO:** Create a dictionary to store your functions. The dictionary should look like this:

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

### 3
**TODO:** Use the dictionary to perform a calculation.
Multiply `4 * 8` using the dictionary like this:

```python
result = operations["*"](4, 8)
print(result)  # Should print 32
```

---

## Functionality of the Calculator
1. The program asks the user to type the first number.
2. The program asks the user to type a mathematical operator (`+`, `-`, `*`, or `/`).
3. The program asks the user to type the second number.
4. The program calculates the result based on the chosen operation.
5. The program asks if the user wants to continue working with the previous result:
   - If **yes**, the previous result is used as the first number, and the calculation process repeats.
   - If **no**, the program resets and asks for a new first number.

---

## Additional Features
- Add a **logo** from `art.py` at the start of your program.
- Implement **error handling** for division by zero.
- Allow the user to **exit** the program at any time.

---

## Hints

### Hint 1
Try sketching out a **flowchart** to plan your program before you start coding.

### Hint 2
To call multiplication from the `operations` dictionary, use:

```python
result = operations["*"](n1=5, n2=3)
print(result)  # Outputs: 15
```

Good luck and have fun coding your calculator!
