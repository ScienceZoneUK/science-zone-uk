# Functions, Dictionaries, and Activities

## Introduction
This README provides step-by-step instructions and examples for learning about functions that return values, as well as activities involving dictionaries and nested data structures. By the end of this guide, you will understand the importance of functions, how to use them effectively, and how to work with real-world problems like grading systems and auctions.

---

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
```python
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2024))  # True
```

#### Example 3: Check Prime Numbers
```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

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
# Grading function
def get_grade(score):
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "Exceeds Expectations"
    elif score >= 71:
        return "Acceptable"
    else:
        return "Fail"

# Input data
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Initialize student grades dictionary
student_grades = {}

# Assign grades using a loop
for student, score in student_scores.items():
    student_grades[student] = get_grade(score)

# Output
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
def get_highest_bidder(bidders):
    highest_bidder = max(bidders, key=lambda x: x['Bid'])
    return highest_bidder

# Input logic
bidders = []
bidding_active = True

while bidding_active:
    name = input("Enter the bidder's name: ")
    bid = int(input("Enter the bid amount: "))
    bidders.append({"Name": name, "Bid": bid})

    more_bids = input("Are there more bidders? Type 'yes' or 'no': ").lower()
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

