# GCSE Python Exercises --- Set 2

## Input, Output & Calculations (1--6)

### 1. Name and Age

Ask the user for their name and age.

Print:

``` text
Hello Alex, you are 15 years old.
```

### 2. Rectangle Area

Ask the user for the width and height of a rectangle.

Calculate and print its area.

Example:

``` text
Width: 5
Height: 4
Area: 20
```

### 3. Seconds Converter

Ask the user to enter a number of minutes and convert it into seconds.

### 4. Average of Three Numbers

Ask the user for three numbers and calculate their average.

### 5. Total Price

Ask the user for: - Price of an item - Quantity

Calculate the total price.

### 6. Celsius Converter

Ask the user for a temperature in Celsius and convert it to Fahrenheit.

``` text
F = (C × 9 / 5) + 32
```

------------------------------------------------------------------------

# Selection --- `if`, `elif`, `else` (7--13)

### 7. Positive or Negative

Ask the user for a number. Print whether it is `Positive`, `Negative`,
or `Zero`.

### 8. Even or Odd

Ask the user for an integer. Print `"Even"` if it is even and `"Odd"`
otherwise.

### 9. Password Checker

``` python
password = "python123"
```

Ask the user to enter a password. Print `"Access Granted"` or
`"Access Denied"`.

### 10. Largest Number

Ask the user for two numbers and print the larger number.

### 11. Age Checker

Ask the user for their age.

-   `"Child"` if under 13
-   `"Teenager"` if 13--17
-   `"Adult"` if 18 or older

### 12. Grade Calculator

Ask the user for a mark between 0 and 100.

``` text
70+ → Grade A
60–69 → Grade B
50–59 → Grade C
40–49 → Grade D
Below 40 → Fail
```

### 13. Login System

``` python
correct_username = "student"
correct_password = "python123"
```

Ask for both username and password. Only print `"Login successful"` if
both are correct.

------------------------------------------------------------------------

# `for` Loops (14--19)

### 14. Count to 10

Use a `for` loop to print the numbers 1 to 10.

### 15. Even Numbers

Use a loop to print all even numbers from 2 to 20.

### 16. Times Table

Ask the user for a number and print its multiplication table from 1 to
10.

Example for `5`:

``` text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

### 17. Total Numbers

``` python
numbers = [5, 8, 2, 10, 7]
```

Use a loop to calculate the total **without using `sum()`**.

### 18. Count the Letter

``` python
word = "mississippi"
```

Use a loop to count how many times `"s"` appears. Do not use `.count()`.

### 19. Find the Largest

``` python
numbers = [12, 5, 27, 8, 19]
```

Use a loop to find the largest number. Do not use `max()`.

------------------------------------------------------------------------

# `while` Loops & Validation (20--24)

### 20. Count Down

Use a `while` loop to print:

``` text
10
9
8
...
1
GO!
```

### 21. Keep Asking

Keep asking the user to type `"yes"`. The program should only stop when
they enter `"yes"`.

### 22. Valid Age

Ask the user for an age. It must be between `0` and `120`. If invalid,
ask again.

### 23. PIN Checker

``` python
correct_pin = "1234"
```

Keep asking for the PIN until the correct PIN is entered. Then print
`"Access Granted"`.

### 24. Three Attempts

``` python
password = "computer"
```

Give the user three attempts to enter the correct password.

If correct:

``` text
Access Granted
```

If all attempts are incorrect:

``` text
Account Locked
```

------------------------------------------------------------------------

# Lists & Algorithms (25--30)

### 25. Search a List

``` python
names = ["Alex", "Sam", "John", "Amy", "David"]
```

Ask the user for a name and print whether it exists in the list.

### 26. Count Passes

``` python
scores = [65, 32, 78, 49, 21, 90, 55]
```

A score of `40` or higher is a pass. Count how many students passed.

### 27. Highest and Lowest

``` python
temperatures = [15, 18, 12, 21, 17, 14]
```

Find the highest and lowest temperatures.

**Challenge:** Do it without using `max()` or `min()`.

### 28. Linear Search

``` python
numbers = [4, 7, 12, 3, 9, 15]
```

Ask the user for a number and use a loop to search the list.

Print `"Found"` or `"Not Found"`.

### 29. Count Occurrences

``` python
numbers = [1, 3, 2, 3, 5, 3, 7, 3]
```

Ask the user for a number and count how many times it occurs. Do not use
`.count()`.

### 30. Number Statistics

``` python
numbers = [12, 7, 5, 18, 21, 4, 10]
```

Calculate:

-   Total
-   Average
-   Largest number
-   Smallest number
-   Number of even values
-   Number of odd values

**Challenge:** Calculate everything using loops rather than `sum()`,
`max()` and `min()`.
