
# 🧠 Python Try-Except Workshop (Age 14+)

## 📚 Overview

This is a 1-hour beginner-friendly Python workshop that teaches students how to use `try-except` to catch and handle errors. It includes step-by-step examples, clear explanations, and a final activity where students build a password checker using a dictionary.

---

## 🛠️ What You’ll Learn

- What Python errors (exceptions) are
- How to stop your code from crashing
- How to use `try-except` to handle different error types
- How to raise your own custom errors
- How to build a simple login system with usernames and passwords

---

## 🧩 Common Python Errors

| Error | What it Means |
|-------|----------------|
| `ValueError` | You tried to use the wrong type (e.g., "hello" instead of a number) |
| `ZeroDivisionError` | You tried to divide by zero |
| `TypeError` | You used mismatched types (e.g., adding string + number) |
| `IndexError` | You asked for a list item that doesn't exist |

---

## 🔍 Activity 1: Crash it on Purpose

```python
age = int(input("Enter your age: "))
print("You will be", age + 1, "next year!")
```

Try typing a word like `"hello"` — Python crashes with a `ValueError`.

---

## 🛡️ Activity 2: Catch That Error

```python
try:
    age = int(input("Enter your age: "))
    print("You will be", age + 1, "next year!")
except ValueError:
    print("Oops! That’s not a number!")
```

🎨 Modify the message to something fun!

---

## ➗ Activity 3: Catch More Errors

```python
try:
    num = int(input("Enter a number: "))
    print("10 divided by", num, "is", 10 / num)
except ValueError:
    print("⚠️ That’s not a number!")
except ZeroDivisionError:
    print("🚫 You can’t divide by zero!")
except Exception as e:
    print("Something else went wrong:", e)
```

---

## 🔁 Activity 4: Ask Until It Works

```python
while True:
    try:
        number = int(input("Pick a number: "))
        print("Thanks! Your number is", number)
        break
    except ValueError:
        print("That’s not a number. Try again!")
```

---

## 💥 Activity 5: Raise Your Own Error

```python
try:
    name = input("What’s your name? ")
    if name == "":
        raise ValueError("No empty names allowed!")
except ValueError as error:
    print("Error:", error)
else:
    print("Hello,", name)
finally:
    print("This message always runs.")
```

---

## 🧪 Final Challenge: Build a Password Checker

### ✅ Goal:
- Store usernames and passwords in a dictionary
- Ask the user to log in
- Catch incorrect usernames or passwords with `try-except`
- Use `raise` to create custom errors

### 🔧 Scaffolded Starter Code

```python
users = {
    "alice": "1234",
    "bob": "qwerty",
    "admin": "admin123"
}

try:
    # Ask the user to enter a username
    username = input("Enter your username: ")

    # Check if username is in dictionary
    # If not, raise ValueError("User not found")

    # Ask for password
    # Check if password matches
    # If not, raise ValueError("Wrong password")

    # Print "Access granted" if everything is OK

except ValueError as e:
    # Print error message
    print("Login failed:", e)

finally:
    print("Login system finished running.")
```

---

## ✅ Complete Example (for reference)

```python
users = {
    "alice": "1234",
    "bob": "qwerty",
    "admin": "admin123"
}

try:
    username = input("Enter your username: ")

    if username not in users:
        raise ValueError("User not found!")

    password = input("Enter your password: ")

    if users[username] != password:
        raise ValueError("Wrong password!")

    print("✅ Access granted! Welcome,", username)

except ValueError as e:
    print("Login failed:", e)

finally:
    print("🔒 Login system finished running.")
```

---

## 🧠 Quiz

1. What does `try` do?
2. What does `except ValueError` catch?
3. What happens when you divide by 0?
4. How can you catch *any* kind of error?
5. How do you **make your own** error happen?

---

## 🎉 Great Job!

Now you know how to:
- Catch errors
- Prevent crashes
- Make your programs safer and friendlier

Ready to build your own games and apps? You're off to a great start! 🚀
