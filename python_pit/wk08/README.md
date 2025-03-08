# Coffee Machine Program

## Overview
This program simulates a coffee machine that allows users to order drinks such as espresso, latte, or cappuccino. It manages resources, processes coin payments, provides change, and prints reports on resource usage—all using British currency.

## Features

1. **User Prompt**
   - The program repeatedly prompts the user with:
     ```
     What would you like? (espresso/latte/cappuccino):
     ```
   - It processes the user's input to determine the next action.
   - The prompt is displayed after every action, allowing for continuous service.

2. **Turn Off the Coffee Machine**
   - The machine can be turned off by entering `"off"`.
   - This serves as a secret command for maintainers to safely shut down the machine, ending the program's execution.

3. **Print Report**
   - When the user enters `"report"`, the program displays the current resource levels.
   - Example output:
     ```
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: £2.50
     ```

4. **Resource Check**
   - Before making a drink, the program checks whether there are enough resources available.
   - If a resource (e.g., water, milk, or coffee) is insufficient, the program outputs a message like:
     ```
     Sorry there is not enough water.
     ```

5. **Process Coins**
   - If there are sufficient resources, the program asks the user to insert coins.
   - Coin values:
     - pound: £1.0
     - fifty: £0.5
     - twenty: £0.2
     - ten: £0.10
     - five: £0.05
     - Pennies: £0.01
   - The program calculates the total monetary value of the inserted coins.
   - For example, inserting 1 quarter, 2 dimes, 1 nickel, and 2 pennies calculates as:  
     `£0.25 + (2 x £0.10) + £0.05 + (2 x £0.01) = £0.52`

6. **Transaction Check**
   - The program verifies whether the inserted money covers the cost of the selected drink.
     - If insufficient, it outputs:
       ```
       Sorry that's not enough money. Money refunded.
       ```
     - If sufficient, the cost is added to the machine's profit.
   - If the inserted amount exceeds the drink's cost, the program calculates and returns the correct change (rounded to 2 decimal places).
     - For example:  
       ```
       Here is £2.45 in change.
       ```

7. **Make Coffee**
   - Upon a successful transaction and if there are enough resources, the program deducts the necessary ingredients from the machine's resources.
   - Example resource update:
     - **Before purchasing a latte:**
       ```
       Water: 300ml
       Milk: 200ml
       Coffee: 100g
       Money: £0.00
       ```
     - **After purchasing a latte:**
       ```
       Water: 100ml
       Milk: 50ml
       Coffee: 76g
       Money: £2.50
       ```
   - Finally, it outputs:
     ```
     Here is your latte. Enjoy!
     ```
     (or the corresponding message for the drink selected).

## How to Use

1. **Run the Program:**
   - Start the Coffee Machine program in your preferred environment.

2. **Input Commands:**
   - At the prompt, type the drink you would like (espresso, latte, or cappuccino).
   - Enter `"report"` to view the current resource levels.
   - Enter `"off"` to shut down the machine (for maintainers).

3. **Follow Prompts:**
   - If your selection requires a coin transaction, follow the prompts to insert coins.
   - Once the transaction is successful, the drink will be prepared and dispensed.

## Conclusion
This Coffee Machine program offers an interactive simulation of a real-life coffee machine. It demonstrates effective resource management, coin processing, transaction validation, and user feedback—all designed to enhance user experience and maintain operational efficiency using British currency.
