# True Love Generator Workshop

**Objective:** In this workshop, you’ll create a program that calculates a "Love Score" based on the names of two people. This project will teach you about conditionals, string manipulation, and counting in Python.

---

💪 This is a difficult challenge! 💪

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs.

    Then check for the number of times the letters in the word LOVE occurs.

    Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is *z*."

### Workshop Outline:

- **Step 1:** Take user input.
- **Step 2:** Convert the input to lowercase to make counting case-insensitive.
- **Step 3:** Count occurrences of letters in "TRUE" from both names.
- **Step 4:** Count occurrences of letters in "LOVE" from both names.
- **Step 5:** Combine the counts to create a two-digit Love Score.
- **Step 6:** Use conditional statements to display a message based on the score.

---

## Step-by-Step Guide

### Step 1: Take Input

**Task**: Prompt the user to enter two names.

```python
# Step 1: Get user input for two names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
```

### Step 2: Convert letters case
**Task**: Convert both names to lowercase to make counting letters case-insensitive.
```python
# Step 2: Convert both names to lowercase
name1 = name1.lower()
name2 = name2.lower()
```
**Explanation**: Using the lower() function ensures that A and a are treated as the same character. This makes it easier to count letters accurately.

### Step 3: Count Occurrences of "TRUE"

**Task**: Count how many times each letter in "TRUE" appears in both names combined.
```python
# Step 3: Count occurrences of letters in "TRUE"
true_count = (
    name1.count('t') + name2.count('t') +
    name1.count('r') + name2.count('r') +
    name1.count('u') + name2.count('u') +
    name1.count('e') + name2.count('e')
)
```
**Explanation**: We use the count() function to find the occurrences of each letter in TRUE across both names, then add them together. The total true_count will be used in the final calculation.

### Step 4: Count Occurrences of "LOVE"

**Task**: Count how many times each letter in "LOVE" appears in both names combined.
```python
# Step 4: Count occurrences of letters in "LOVE"
love_count = (
    name1.count('l') + name2.count('l') +
    name1.count('o') + name2.count('o') +
    name1.count('v') + name2.count('v') +
    name1.count('e') + name2.count('e')
)
```
**Explanation**: Similar to Step 3, we count each letter in "LOVE" and sum these values to get the total love_count.

### Step 5: Calculate the Love Score

**Task**: Combine true_count and love_count into a two-digit number representing the "Love Score."

```python
# Step 5: Combine true_count and love_count into a two-digit number
love_score = int(str(true_count) + str(love_count))
```
**Explanation**: By converting true_count and love_count to strings and joining them, we create a two-digit number. Converting this result back to an integer gives us the final love_score.








