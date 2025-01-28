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

# Big Project

## Easy solution
```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


encrypt(original_text=text, shift_amount=shift)

```

## Hard solution
```python
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")



```

