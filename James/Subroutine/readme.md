# Introduction to subroutines 
Sometimes when writing code there may be some alogrithms or sequences that repeat themselves in other to
avoid retyping those algorithms programmers use this thing we call subroutines otherwise know as functions.
This helps the code to be more easy to read quicker to type and neater etc. Here is how you define a function in 
python 

## How to define a subroutine 
```python

def my_sub():
  print("Hello World)

```
## How to call a subroutine
Before you can use a subroutine you'll have to call it to call it you will use the name of the subroutine then the 

```python
my_sub()
```

## Task 1
* Call a subroutine that prints “Hello, world”
* Call the same subroutine three times
* Predict the output of a program that calls multiple subroutines
* Change the order of subroutine calls and observe what changes


## Task2 

```python

balance = 1000  # Starting balance

def show_menu():
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance():
    global balance
    print("Your current balance is:", balance)

def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful!")

def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
    else:
        print("Insufficient funds!")

# Main program
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Try again.")


```


