
# Workshop: Using Python Dictionaries to Collect User Data

## Overview

In this workshop, you will learn:
1. How to create a Python dictionary to store structured data.
2. How to use `input()` to collect user information.
3. How to store and display data for multiple users using a list of dictionaries.

---

## Materials Needed
1. Python IDE ([Thonny](https://thonny.org/) )or online coding platform.
2. Access to a computer.

---

## Learning Objectives
1. Build a dictionary structure for data.
2. Use `input()` to gather user details.
3. Collect and display multiple dictionaries in a list.

---

## Resources
[W3 Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

---

## Recap
Briefly recap what dictionaries are:

- Key-value pairs.
- Keys are unique identifiers, and values store data.
Example:
    
```python 
person = {
    "name": "John",
    "age": 25,
    "gender": "male"
}
```

## Workshop Plan

### Step 1: Create an Empty Dictionary Structure (5 minutes)

**Task:**  
Start by creating an empty dictionary for a single person.

```python
# Create an empty dictionary to store one person's information
person = {
    "name": "",
    "age": 0,
    "gender": "",
    "favorite_food": "",
    "birth_place": ""
}

# Print the dictionary to see its structure
print(person)
```

**Discussion:**  
- Why do we use keys like `"name"` and `"age"`?  
(Answer: To organize and label data clearly.)

---

### Step 2: Fill the Dictionary with Sample Data (5 minutes)

**Task:**  
Manually add sample data to the dictionary and print it.

```python
# Fill in the dictionary with sample data
person["name"] = "Alice"
person["age"] = 12
person["gender"] = "female"
person["favorite_food"] = "pizza"
person["birth_place"] = "New York"

# Print the filled dictionary
print(person)
```

**Discussion:**  
- How do we access or update a value in a dictionary?  
(Answer: Using the key, e.g., `person["name"]`.)

---

### Step 3: Use `input()` to Gather Data Dynamically (10 minutes)

**Task:**  
Replace hardcoded values with user input.

```python
# Ask the user for their details
person["name"] = input("What is your name? ")
person["age"] = int(input("How old are you? "))
person["gender"] = input("What is your gender? ")
person["favorite_food"] = input("What is your favorite food? ")
person["birth_place"] = input("Where were you born? ")

# Print the dictionary with user data
print("\nHere is the information you provided:")
print(person)
```

**Discussion:**  
- Why do we use `int()` for age?  
(Answer: To convert the input from a string to a number.)  
- Encourage students to try entering their own details.

---

### Step 4: Collect Data for Multiple People Using a List (10 minutes)

**Task:**  
Store multiple dictionaries in a list.

```python
# Create an empty list to store multiple people's data
people = []

# Add a single dictionary (the 'person' dictionary) to the list
people.append(person)

# Print the list
print("\nData collected about people:")
print(people)
```

**Discussion:**  
- Why do we use a list to store multiple dictionaries?  
(Answer: To group data for multiple people in one place.)

---

### Step 5: Add a Loop to Collect Multiple Records (10 minutes)

**Task:**  
Use a `while` loop to collect multiple people's data dynamically.

```python
# Create an empty list to store multiple people's data
people = []

# Loop to gather data for multiple people
while True:
    # Create a new dictionary for each person
    person = {
        "name": input("What is your name? "),
        "age": int(input("How old are you? ")),
        "gender": input("What is your gender? "),
        "favorite_food": input("What is your favorite food? "),
        "birth_place": input("Where were you born? ")
    }
    
    # Add the dictionary to the list
    people.append(person)

    # Ask if the user wants to add another person
    add_another = input("Do you want to add another person? (yes/no): ").lower()
    if add_another != "yes":
        break

# Print the collected data
print("\nData collected about people:")
print(people)
```

**Discussion:**  
- What happens if we skip the `break` statement?  
(Answer: The loop will run forever!)  
- Emphasize saving data at each iteration.

---

### Step 6: Display Data Nicely (10 minutes)

**Task:**  
Format the output to display each person’s details in a clean format.

```python
# Display each person's information
print("\nData collected about people:")
for p in people:
    print(f"Name: {p['name']}")
    print(f"Age: {p['age']}")
    print(f"Gender: {p['gender']}")
    print(f"Favorite Food: {p['favorite_food']}")
    print(f"Birth Place: {p['birth_place']}")
    print("------")
```

**Challenge:**  
- Add another field to the dictionary (e.g., hobby) and include it in the output.

---

## Wrap-Up and Extension Ideas

**Summary:**  
1. Use dictionaries to structure data.  
2. Use `input()` to gather user input.  
3. Use loops to handle multiple entries.

**Extension Challenge:**  
- Write the data to a text file.  
- Add error handling for invalid inputs (e.g., non-numeric age).
