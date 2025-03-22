# Learning to read Psuedo-Code
Pseudo-code is a simple way of describing a set of instructions in a manner that resembles a programming language. In an algorithm, most processes fall into three main categories:
* inputs
* processes
* outputs

* For example, if a person was writing a program where a number is input and the program calculates and outputs the times table up to ten, they could write a statement like this:
```
The user INPUTS a number which is saved as num
FOR each number from 1 to 10, OUTPUT num*number
```
This could be improved by writing the pseudocode:
```
num ← USERINPUT
FOR number ← 1 TO 10
  OUTPUT number * num
ENDFOR
```
The ← symbol in pseudo-code means assignment.
Most programming languages use = instead of ←. In the example above, num ← USERINPUT means that the user input is being put into, or assigned to,  
the variable called num ```num = input("What's your name?")```.

Outputs use the word OUTPUT before the data to be sent to the user. In the example above, the line OUTPUT number * num in Python might look like ```print(number * num)```.

Processing refers to any operation the computer system is performing on data, for example doing a calculation or searching for 
something. In OUTPUT number * num, the program is actually performing a calculation within the output, so it is possible to see statements which combine one or more of these.


## Functions in Pseudocode

Functions are fundamental components in programming that allow you to group related instructions together, make your code more modular, and promote reusability. In pseudocode, functions are used to structure algorithms and simplify complex tasks by breaking them down into smaller, more manageable pieces.
Function Syntax

The basic syntax for defining a function in pseudocode is:
```
FUNCTION function_name (parameters)
    statements
    RETURN value
END FUNCTION
```

Here, "function_name" is the name of the function, "parameters" are the inputs that the function takes, "statements" are the actions the function performs, and "value" is what the function returns.
Example of a Simple Function



```
FUNCTION calculate_sum (a, b)
    sum = a + b
    RETURN sum
END FUNCTION

INPUT x, y
result = calculate_sum(x, y)
OUTPUT result
```


## The vending machine

* Can you predict what the program will do?

The psuedo-code is one complete procedure, this is not good practice.



```
// Coffee Machine Pseudocode Skeleton
// Diagram: [INPUTS] → [PROCESSES] → [OUTPUTS]

START

// OUTPUT: Display welcome message and coffee menu
OUTPUT "Welcome to the Coffee Machine!"
OUTPUT "Please select your coffee:"
OUTPUT "1: Espresso - £1.50"
OUTPUT "2: Latte    - £2.00"
OUTPUT "3: Cappuccino - £2.50"

// INPUT: User selects a coffee option (coffee_choice)
coffee_choice ← USERINPUT

// PROCESS: Determine coffee selection and set price
IF coffee_choice = "1" THEN
    coffee_name ← "Espresso"
    price ← 1.50
ELSE IF coffee_choice = "2" THEN
    coffee_name ← "Latte"
    price ← 2.00
ELSE IF coffee_choice = "3" THEN
    coffee_name ← "Cappuccino"
    price ← 2.50
ELSE
    OUTPUT "Invalid selection. Please restart the program."
    STOP
ENDIF

// OUTPUT: Confirm the selected coffee and its price
OUTPUT "You selected " + coffee_name + " which costs £" + price

// PROCESS: Convert the price from pounds to pence for easier calculation
price_pence ← price * 100

// PROCESS: Initialize total money inserted to zero
total_inserted ← 0

// OUTPUT: Inform the user of the accepted coins
OUTPUT "Accepted coins: 1p, 2p, 5p, 20p, 50p, £1, £2"

// LOOP: Continue accepting coins until the inserted total meets or exceeds the price
WHILE total_inserted < price_pence DO
    // INPUT: User inserts a coin (coin_input)
    OUTPUT "Insert a coin (e.g., 1p, 2p, 5p, 20p, 50p, £1, £2):"
    coin_input ← USERINPUT

    // PROCESS: Convert coin_input to a numeric value in pence
    // For example: "1p" → 1, "£1" → 100, "£2" → 200, etc.
    // (Students need to implement this conversion logic)
    coin_value ← CONVERT_COIN(coin_input)
    
    // PROCESS: Validate the coin is accepted (valid values: 1, 2, 5, 20, 50, 100, 200)
    IF coin_value is in {1, 2, 5, 20, 50, 100, 200} THEN
        total_inserted ← total_inserted + coin_value
        // OUTPUT: Show current total inserted
        OUTPUT "Total inserted: " + total_inserted + " pence"
    ELSE
        OUTPUT "Invalid coin. Please try again."
    ENDIF
ENDWHILE

// PROCESS: Calculate change if any
IF total_inserted > price_pence THEN
    change ← total_inserted - price_pence
    // OUTPUT: Dispense coffee and return change
    OUTPUT "Dispensing " + coffee_name + ". Your change is " + change + " pence."
ELSE
    // OUTPUT: Dispense coffee with exact amount
    OUTPUT "Dispensing " + coffee_name
ENDIF

STOP

```


