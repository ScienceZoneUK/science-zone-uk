# 🍬 Python Workshop: Sweet Vending Machine

## 🎯 Target Age
12–13 years old

## 🧠 Learning Goals
- Understand what subroutines are
- Practice creating **procedures** (no return) and **functions** (with return)
- Use a dictionary to store and look up data
- Build a basic vending machine simulator
- Follow the PRIMM learning structure

---

## 🧩 PRIMM Framework

### ✅ 1. Predict + Run: Simple Procedure

```python
sweets = {
    "Mars": 1.20,
    "Skittles": 0.95,
    "Haribo": 0.85
}

def welcome_message():
    print("Welcome to the Sweet Vending Machine!")
    print("Choose from the following sweets.")
```

**Prediction Prompt:**  
What do you think will happen when we run `welcome_message()`?

```python
welcome_message()
```

---

### 🔍 2. Investigate: Trace the Code

Use **Thonny's Debugger** to trace this code line by line:

1. Add a **breakpoint** on the line calling `welcome_message()`
2. Click **debug** or press `Ctrl+F5`
3. **Step through** the code using the step buttons
4. Watch how Python **enters the function**, executes the print statements, then **returns back**

---

### ✏️ 3. Modify: Procedure With Parameter

```python
def show_price(sweet_name):
    if sweet_name in sweets:
        print(sweet_name + " costs £" + str(sweets[sweet_name]))
    else:
        print("That sweet is not available.")
```

Try:
```python
show_price("Mars")
show_price("Twix")
```

---

### ➕ 4. Modify: Function With Return

```python
def get_price(sweet_name):
    if sweet_name in sweets:
        return sweets[sweet_name]
    else:
        return 0
```

Try:
```python
price = get_price("Haribo")
print("You need £" + str(price))
```

---

### 🧠 5. Make: Your Own Vending Machine Program

```python
def vend(sweet, money):
    if sweet in sweets:
        price = sweets[sweet]
        if money >= price:
            change = money - price
            print("Here is your " + sweet)
            print("Your change is £" + str(round(change, 2)))
        else:
            print("Not enough money.")
    else:
        print("That sweet is not in the machine.")
```

Try:
```python
name = input("What sweet would you like? ")
money = float(input("How much money do you have? "))
vend(name, money)
```

---

## 🌈 Extension Challenges
- Add more sweets to the dictionary
- Track how many sweets have been sold
- Let the user buy multiple items
- Add a stock counter for each sweet

---

## 🐞 Tip: Always use **Trace (Debug)** in Thonny to step through your code if something doesn’t work as expected!
