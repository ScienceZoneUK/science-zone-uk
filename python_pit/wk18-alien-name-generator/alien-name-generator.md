# Python Alien Name Generator

## Getting Started

### 1. Recommended Tools
- Install **[Thonny](https://thonny.org/)**: A beginner-friendly Python IDE to write and run your Python code.
- **[W3Schools Python Tutorial](https://www.w3schools.com/python/)**: Use this as an additional resource to learn and explore Python concepts.

### 2. Preparing to Code
1. Open **Thonny**.
2. Create or open a folder named after yourself (e.g., `alex_python_workshop`).
3. Save **all your programs** in this folder:
   - File names should be in **lowercase**.
   - No **spaces** in file names. Use underscores (`_`) if needed.
   - File names should be **meaningful** (e.g., `greet_function.py`, not `file1.py`).

---

## Learning Objectives
- By the end of this activity, you will:
  1. Understand the concepts of random number generation, modifying strings.
  2. Write code to practice using libraries and manipulating strings.
  3. Apply the learned concepts to solve challenges.

---

## Concept Explanation

### What are random numbers?
**Random numbers** are numbers generated unpredictably. You cannot predict what the next number will be even if you know all of the previous numbers.
### What are strings?
**Strings** are text. They are made up of a collection of individual letters, numbers or punctuation marks called characters. Characters under the hood are simply numbers from 0-255 (8-bit). Each number represents a different character. See the ASCII table for the exact code for each character.

---

## Guided Activity

### Example Code
Save this code as `random-strings.py` in your folder:
```python
import random

length = random.randint(2,10)
for character in range(0, length, 1):
  print(char(random.randint(97, 123)), end="")
# 97-122 are a-z in ASCII, so we choose a random number between 97 and 122 inclusive.
```

### Steps to Follow
1. Open **Thonny** and create a new file.
2. Copy and paste the code above into your file.
3. Save the file in your folder as `random-strings.py`.
4. Run the program to see the output.
5. Modify the program and experiment by changing parts of the code.

---

## Practice Activities

### Activity 1: [Activity Name]
Save this as `vowels-consonants.py`.

- Modify the string to make the first letter capitalised, we're generating names!
- Make the characters alternate between vowels and consonants to make the names more pronouncable.

### Activity 2: [Activity Name]
Save this as `sentences.py`.

- Generate a random number between 1 and 10 to be the number of words in your sentence
- Generate this number of words and print them out, with spaces in-between.

---

## DIY Challenge

### Challenge 1: [Challenge Name]
Save this as `punctuation.py`.

- Modify your sentence generator to add punctuation after each word.

### Advanced Challenge (Optional)
Save this as `paragraphs.py`.

- Modify your sentence generator to generate a random number of sentences and print a whole paragraph to the screen!

---

## Summary
- **What did you learn?**
  - How to generate random numbers
  - ASCII and the relationship between random numbers and random letters.
- **What’s next?**
  - Much more complex versions of this system are used to generate readable English. This is how AI chatbots such as ChatGPT work!

---

## Resources
- 🐍 [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- 🐍 [Official Python Documentation](https://docs.python.org/3/)
- 💡 [Fun Python Practice Problems](https://www.hackerrank.com/domains/tutorials/10-days-of-python)
