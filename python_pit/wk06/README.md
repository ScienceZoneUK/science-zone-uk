# Functions, Dictionaries, and Activities

## Introduction
This README provides step-by-step instructions and examples for learning about functions that return values, as well as activities involving dictionaries and nested data structures. By the end of this guide, you will understand the importance of functions, how to use them effectively, and how to work with real-world problems like grading systems and auctions.

---

## Table of Contents
1. [Functions That Return Values](#functions-that-return-values)
   - What are Functions that Return Values?
   - Examples and Explanations
   - Practice Activities

2. [Grading Program Using Dictionaries](#grading-program-using-dictionaries)
   - Problem Breakdown
   - Solution and Code
   - Activity

3. [Blind Auction Using Nested Dictionaries](#blind-auction-using-nested-dictionaries)
   - Problem Breakdown
   - Solution and Code
   - Activity

4. [Homework and Extensions](#homework-and-extensions)

---

## Functions That Return Values

### What Are Functions That Return Values?
The Python return statement marks the end of a function and specifies the value or values to pass back from the function. Return statements can return data of any type, including integers, floats, strings, lists, dictionaries, and even other functions.
[W3Schools](https://www.w3schools.com/python/gloss_python_function_return_value.asp)

**Syntax:**
```python
def function_name(parameters):
    # Perform some operation
    return value
```

### Examples and Explanations
#### Example 1: Simple Addition
```python
def add_numbers(a, b):
    result = a + b
    return result

output = add_numbers(3, 4)  # Call the function
print(output)  # Prints: 7
```

#### Example 2: Is Leap Year?
Determine whether a year is a leap year.
- See if the number is evenly divisible by 4. Dividing the year by 4 will result in a whole number with no remainder if the number is evenly divisible. The number must be evenly divisible by 4! Otherwise, it is not a leap year
- Confirm the number isn't evenly divisible by 100. If a year is evenly divisible by 4, but it is not evenly divisible 100, then it is a leap year. If a year is divisible by both 4 and 100, then it might not be a leap year, and you will have to perform 1 more calculation to check
- Check if the number is evenly divisible by 400 to confirm a leap year. If a year is divisible by 100, but not 400, then it is not a leap year. If a year is divisible by both 100 and 400, then it is a leap year.


Use modulo to check if the year is divisible by a value example: divisible by 4 ```  print(year % 4 == 0) ```
Use nested if statements that return a boolean:
```python
 if ___:
        if ___:
            if ___:
                return ___
            else:
                return ___
        else:
            return ___
    else:
        return ___
```
```python
def is_leap_year(year):
   ___
   ___

#Answers
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2024))  # True
```

#### Example 3: Check Prime Numbers
Use modulo again to check is a number is divisible by a value.
Copy the code into your file.
```python
def is_prime(num):
   #Use a conditional to check number is < or == 1
   #Return ???
   #Loop to check a range
   #range(2, int(num ** 0.5) + 1)
   #conditional to check if the number is divisiable by i in the for loop, return false
   #Otherwise the function returns true

#Answers
print(is_prime(11))  # True
print(is_prime(25))  # False
print(is_prime(2))   # True
```

### Practice Activity
- Write a function that calculates the factorial of a number.
- Write a function that checks if a string is a palindrome.

---

## Grading Program Using Dictionaries

### Problem Breakdown
You have a dictionary of student scores. Write a program to assign grades based on the following criteria:
- **91 - 100:** Outstanding
- **81 - 90:** Exceeds Expectations
- **71 - 80:** Acceptable
- **70 or below:** Fail

### Solution and Code
```python
# Input data
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Initialize student grades dictionary


# Grading function that checks a score against the grading criteria
def get_grade(score):
   #add code
   #add code
   #add code




# Get grade function returns a grade then assign grades using a loop, put the student grades into a dictionary
for ???, ??? in ???.items():
    student_grades[???] = get_grade(???)

# Output the dictionary
print(student_grades)
```

### Activity
- Modify the program to include an additional grade category for scores between 50 and 60.

---

## Blind Auction Using Nested Dictionaries

### Problem Breakdown
1. Collect bidder names and their bid amounts.
2. Store each entry in a dictionary.
3. Determine the highest bidder.

### Solution and Code
```python
# A function that takes a dictionary, sorts it and returns the highest bidder. Use the '.max(key=lambda x: x['???'])' method on the dictionary
def get_highest_bidder(bidders):
    highest_bidder = ???
    return ????

# Input logic
bidders = []
bidding_active = True

while bidding_active:
    name = input("????")
    bid = int(input("???"))
   #Append a list of bidders and their bid in a dictionary structure
   ???.append({????})

    more_bids = input("???").lower()
    if more_bids == 'no':
        bidding_active = False

# Determine winner
winner = get_highest_bidder(bidders)
print(f"The winner is {winner['Name']} with a bid of ${winner['Bid']}")
```

### Activity
- Add functionality to validate that bids are positive integers.
- Extend the program to handle ties by restarting the auction.

---

## Homework and Extensions

1. **Modify the Grading Program**
   - Add a new grade category for scores below 50.
   - Allow users to input their own grading criteria.

2. **Extend the Blind Auction**
   - Add an option for users to view all bids before deciding to add more.
   - Implement a feature to remove a bid.

3. **Practice Functions**
   - Write a function that reverses a string.
   - Write a function that calculates the nth Fibonacci number.

---

## Final Notes
Understanding functions, dictionaries, and loops is essential for solving real-world problems. These activities build foundational skills that can be extended to more complex tasks in programming.

