
# Week 2: Conditional Statements and Logic

## Objectives:
- Learn how to use conditional statements to make decisions in Python.
- Apply logic to solve problems using `if`, `elif`, and `else`.

## Key Concepts:
1. **Conditional Statements**: These allow your program to make decisions based on certain conditions.
   - **if statement**: Checks if a condition is true and runs a block of code if it is.
     ```python
     if age >= 18:
         print("You can vote!")
     ```
   - **elif statement**: Checks another condition if the previous condition is false.
   - **else statement**: Runs if none of the previous conditions are true.
2. **Comparison Operators**: Used to compare values in conditions. Common operators:
   - `==`: Equals
   - `!=`: Not equals
   - `>`: Greater than
   - `<`: Less than
   - `>=`: Greater than or equal to
   - `<=`: Less than or equal to
3. **Boolean Logic**: Python expressions that evaluate to either `True` or `False`. Often used with conditionals.

## Tasks:
1. **Sudo Code for Activity 1:**
   - Prompt the user to enter the weather condition.
   - Use `if` statements to recommend an activity based on the user's input.
   ```python
   # Pseudo code
   # Ask the user about the weather (raining or sunny).
   # If raining, suggest an indoor activity.
   # If sunny, suggest an outdoor activity.
   ```

2. **Sudo Code for Activity 2:**
   - Ask for the user's age and recommend a movie rating based on their age.
   ```python
   # Pseudo code
   # Get user's age.
   # If the user is younger than 13, recommend a PG movie.
   # If between 13 and 17, recommend a PG-13 movie.
   # If 18 or older, recommend an R-rated movie.
   ```

# Python Workshop

This workshop covers Python programming fundamentals, including user input, arithmetic calculations, string formatting with f-strings, and rounding numbers. Participants will also create a **Tip Calculator** and a **Leap Year Calculator** as practical applications.

## Objective

By the end of this workshop, you will:
- Understand how to get user input.
- Learn how to perform arithmetic calculations.
- Discover how to round numbers and format strings using f-strings.
- Create a simple tip calculator application.

## Topics Covered

### 1. F-strings in Python
F-strings allow embedding expressions inside string literals. They are preceded by an `f` or `F` before the opening quote.

#### Example:
```python
name = "John"
color = "blue"
age = 25
print(f"My name is {name}, my favorite color is {color}, and I am {age} years old.")
```

#### Sudo Code for Activity:
- Create your own f-string that includes variables such as name, favorite color, and favorite number.
- Use rounding in your f-string to format a decimal number.
```python
# Pseudo code
# Create variables for name, favorite color, and favorite number.
# Use f-strings to print a sentence including these variables.
```

### 2. Rounding Numbers
The `round()` function allows rounding a number to a specified number of decimal places.

#### Syntax:
```python
round(number, decimal_places)
```

#### Example:
```python
rounded_number = round(3.14159, 2)  # Output: 3.14
```

#### Sudo Code for Activity:
- Try rounding different numbers using the `round()` function.
```python
# Pseudo code
# Create a float number.
# Use round() to round it to 2 decimal places.
# Print the rounded number.
```

## Projects

### Tip Calculator

This application calculates the total tip and splits the bill among friends.

#### Steps:
1. **Welcome Message**: Start by welcoming the user.
2. **User Inputs**: 
   - Total bill amount.
   - Tip percentage (10%, 12%, or 15%).
   - Number of people splitting the bill.
3. **Calculations**: 
   - Calculate the total tip and total bill.
   - Divide the total bill by the number of people to find out how much each person owes.
4. **Rounding & Formatting**:
   - Use `round()` to round the amount to two decimal places.
   - Format the output using f-strings.
  
#### Sudo Code for Challenge:
- Tip Calculator
```python
# Pseudo code for Tip Calculator

# 1. Display a welcome message for the user.

# 2. Ask the user to input the total bill amount.

# 3. Ask the user to input the tip percentage they want to give (options: 10%, 12%, or 15%).

# 4. Ask the user to input the number of people splitting the bill.

# 5. Calculate the tip as a percentage of the total bill.

# 6. Calculate the total tip amount.

# 7. Add the total tip amount to the original bill to get the total bill.

# 8. Divide the total bill by the number of people to find how much each person should pay.

# 9. Round the result to 2 decimal places.

# 10. Display the final amount each person needs to pay.

```

#### Example:
```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
```

#### Sudo Code for Challenge:
- Add more tip percentage options (e.g., 18%).
```python
# Pseudo code
# Add an option for a new tip percentage (e.g., 18%).
# Perform the same calculations to get the final amount per person.
```

- Create an option to split the bill unevenly by entering different amounts for each person.
```python
# Pseudo code
# Ask each person how much they want to contribute.
# Calculate each person's individual share, including tip.
```

### Leap Year Calculator

This program checks whether a given year is a leap year or not.

#### Steps:
1. Prompt the user to enter a year.
2. Check if the year is divisible by 4.
3. If divisible by 4, check if it's divisible by 100.
4. If divisible by 100, check if it's divisible by 400.
5. Print the result ("Leap year" or "Not a leap year").

#### Example:
```python
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
```

#### Sudo Code for Activity:
- Prompt the user for a year and check whether it is a leap year.
```python
# Pseudo code
# Ask the user for a year.
# Check if the year is divisible by 4.
# If it is, check if it's divisible by 100 and 400.
# Print "Leap year" or "Not a leap year" based on the checks.
```

## Additional Resources
- [How to Print a Float with Two Decimal Places in Python](https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python)

## License
This workshop is for educational purposes. Feel free to use and modify the content as needed.
