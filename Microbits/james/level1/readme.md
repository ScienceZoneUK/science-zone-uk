## Warm Up

### Loops

1. **Count to 100**

   * Print the numbers from 1 to 100.
   * Then modify it to only print even numbers.

2. **Countdown**

   * Ask the user for a starting number.
   * Count down to 0.
   * Print `"Blast off!"` at the end.

3. **Sum of Numbers**

   * Ask the user for 5 numbers.
   * Add them together and output the total.
   * Challenge: use a loop rather than writing five separate inputs.

4. **Guess the Number**

   * Store a secret number.
   * Keep asking the user to guess until they get it right.
   * Tell them `"Too high"` or `"Too low"`.

5. **Number Validation**

* Ask the user to enter a number between 1 and 10.
* Keep asking until they enter a valid number.
* Concepts: `while`, `if/else`.

---

### Arrays / Lists

1. **Shopping List**

* Create a list containing 5 items.
* Use a loop to print each item.

2. **Find the Largest**

* Create a list of numbers.
* Find and print the largest number **without using `max()`**.

3. **Count Even Numbers**

* Given a list of numbers, count how many are even.

4. **Search a List**

* Create a list of names.
* Ask the user for a name.
* Tell them whether the name is in the list.
* Challenge: do it using a loop instead of `in`.

5. **Average Calculator**

* Store several test scores in a list.
* Calculate and output the average.
* Then output `"Pass"` or `"Fail"` depending on the average.

---

### GCSE-style challenges

1. **Student Score System**

Store 10 scores in a list.

Your program should:

* calculate the total
* calculate the average
* find the highest score
* find the lowest score
* count how many students passed
* output a grade for each student

This combines **lists + loops + selection + arithmetic**.

2. **ATM Simulator**

Start with a balance of £500.

Display:

```text
1. Check balance
2. Deposit
3. Withdraw
4. Exit
```

Keep displaying the menu until the user chooses Exit.

Make sure:

* they cannot withdraw more than their balance
* they cannot deposit a negative amount
* invalid menu choices are rejected

This is excellent practice for `while` loops and `if/elif/else`.

3. **Quiz Game**

Store several questions and answers.

The program should:

* ask each question
* check the answer
* keep track of the score
* display the final score
* give a message based on the score

Example:

```text
Score: 8/10
Excellent!
```

4. **Number Analysis**

Ask the user to enter 10 numbers and store them in a list.

Then output:

```text
Largest:
Smallest:
Total:
Average:
Even numbers:
Odd numbers:
```

**Challenge:** Don't use `max()`, `min()` or `sum()`.

5. **Cinema Ticket System**

Ask for the customer's age and calculate their ticket price.

For example:

```text
Under 5       £0
5–15          £6
16–64         £10
65+           £7
```

Then add:

* number of tickets
* discounts
* input validation
* a running total

This gives you practice with nested `if` statements and loops.

### ⭐ A really good GCSE challenge order

I'd recommend doing them in this order:

**if/else → loops → lists → combining them**
