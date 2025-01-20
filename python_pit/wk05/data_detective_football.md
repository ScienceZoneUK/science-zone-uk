
# **Exploring Football Players with Python Dictionaries**

Welcome to this hands-on Python workshop! In this guide, we will explore the powerful capabilities of dictionaries, learn to access and manipulate nested data, and build an interactive app to investigate information about football players.

---

## **Table of Contents**
1. [Introduction to Dictionaries](#1-introduction-to-dictionaries)
2. [Understanding Large Numbers with Underscores](#2-understanding-large-numbers-with-underscores)
3. [The Football Players Dictionary](#3-the-football-players-dictionary)
4. [Accessing the Dictionary](#4-accessing-the-dictionary)
5. [Being a Data Detective](#5-being-a-data-detective)
6. [Sorting Data with the sorted() Function](#6-sorting-data-with-the-sorted-function)
7. [Creating an Interactive App](#7-creating-an-interactive-app)
8. [Conclusion](#8-conclusion)

---

## **1. Introduction to Dictionaries**

A dictionary in Python is a collection of key-value pairs. It allows you to map keys (like a player's name) to values (like their goals, assists, market value, etc.).

### **Syntax**
```python
# Example dictionary
player_dict = {
    "player1": "value1",
    "player2": "value2",
    "player3": "value3"
}
```

### **Key Features**
- Keys must be unique.
- Values can be of any data type (strings, numbers, lists, even other dictionaries).

---

## **2. Understanding Large Numbers with Underscores**

Python allows underscores in numbers to make large values easier to read. This feature improves clarity without affecting the number's value.

### **Example**
```python
market_value = 150_000_000  # Market value in euros
```

Python treats these numbers as normal:
```python
print(150_000_000 + 1)  # Output: 150000001
```

---

## **3. The Football Players Dictionary**

Our main data structure is a dictionary of 10 football players. Each player's name is a key, and its value is another dictionary containing details.

```python
football_players = {
    "Lionel Messi": {
        "team": "Inter Miami",
        "position": "Forward",
        "goals_scored": 804,
        "assists": 365,
        "market_value": 50_000_000,
        "country": "Argentina"
    },
    "Cristiano Ronaldo": {
        "team": "Al-Nassr",
        "position": "Forward",
        "goals_scored": 850,
        "assists": 229,
        "market_value": 20_000_000,
        "country": "Portugal"
    },
    "Kylian Mbappé": {
        "team": "Paris Saint-Germain",
        "position": "Forward",
        "goals_scored": 253,
        "assists": 116,
        "market_value": 180_000_000,
        "country": "France"
    },
    "Kevin De Bruyne": {
        "team": "Manchester City",
        "position": "Midfielder",
        "goals_scored": 95,
        "assists": 250,
        "market_value": 85_000_000,
        "country": "Belgium"
    },
    "Erling Haaland": {
        "team": "Manchester City",
        "position": "Forward",
        "goals_scored": 204,
        "assists": 65,
        "market_value": 170_000_000,
        "country": "Norway"
    },
    "Neymar Jr.": {
        "team": "Al-Hilal",
        "position": "Forward",
        "goals_scored": 430,
        "assists": 210,
        "market_value": 60_000_000,
        "country": "Brazil"
    },
    "Robert Lewandowski": {
        "team": "Barcelona",
        "position": "Forward",
        "goals_scored": 552,
        "assists": 157,
        "market_value": 30_000_000,
        "country": "Poland"
    },
    "Luka Modrić": {
        "team": "Real Madrid",
        "position": "Midfielder",
        "goals_scored": 50,
        "assists": 123,
        "market_value": 10_000_000,
        "country": "Croatia"
    },
    "Mohamed Salah": {
        "team": "Liverpool",
        "position": "Forward",
        "goals_scored": 303,
        "assists": 129,
        "market_value": 90_000_000,
        "country": "Egypt"
    },
    "Harry Kane": {
        "team": "Bayern Munich",
        "position": "Forward",
        "goals_scored": 321,
        "assists": 94,
        "market_value": 100_000_000,
        "country": "England"
    }
}
```

---

## **4. Accessing the Dictionary**

### **Access Nested Values**
Access details about a specific player:
```python
print(football_players["Lionel Messi"]["goals_scored"])  # Output: 804
```

---

## **5. Being a Data Detective**

Imagine you’re a detective investigating football players' performance. Your job is to sift through the data to find specific pieces of information, like top scorers, most valuable players, or the total assists. Python makes this investigation easy by letting us "ask questions" to the dictionary.

---

### **Task 1: Find Specific Details**

We’ll use Python code to explore the dictionary (`football_players`) and answer these questions:

1. **Who are the forwards?**
2. **Who has the highest market value?**
3. **Which player has scored the most goals?**

---

### **Step 1: Understand the Dictionary**

The `football_players` dictionary is a collection of data about players. Each key is the name of a player (like "Lionel Messi" or "Cristiano Ronaldo"), and its value is another dictionary containing details about that player.

---

### **Sorting Data with the sorted() Function**

The `sorted()` function is a powerful tool in Python for organizing data. Let’s explore it in detail.

### **What is `sorted()`?**
The `sorted()` function arranges items in a list or other iterable object in a specific order. By default, it sorts in **ascending order**.

### **Syntax**
```python
sorted(iterable, key=None, reverse=False)
```

### **Parameters**
1. **`iterable`**:
   - The data structure to sort. It can be a list, tuple, dictionary keys, or items.
   - Example: A list of country names or a list of key-value pairs.

2. **`key`** (optional):
   - A function that specifies a custom sort order.
   - Example: Sort countries by population using `key=lambda x: x[1]["population"]`.

3. **`reverse`** (optional):
   - A boolean (`True` or `False`).
   - Default is `False` (ascending order). Set to `True` for descending order.

---

### **Examples**

#### **1. Sorting a List**
Sort a simple list of numbers in ascending order:
```python
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 7, 9]
```

#### **2. Sorting in Descending Order**
Use the `reverse=True` parameter:
```python
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # Output: [9, 7, 5, 2, 1]
```

#### **3. Sorting a Dictionary by Keys**
Sort country names alphabetically:
```python
sorted_countries = sorted(countries_data.keys())
print(sorted_countries)
# Output: ['Brazil', 'Germany', 'India', 'USA', ...]
```

---

### **Sorting Nested Data**

#### **4. Sorting by Population**
Sort countries by their population in descending order:
```python
sorted_by_population = sorted(countries_data.items(), key=lambda x: x[1]["population"], reverse=True)

for country, details in sorted_by_population:
    print(f"{country}: {details['population']} people")
```

#### **5. Sorting by CO2 Pollution**
Sort countries based on their CO2 pollution:
```python
sorted_by_pollution = sorted(countries_data.items(), key=lambda x: float(x[1]["pollution_co2"].split()[0]))

for country, details in sorted_by_pollution:
    print(f"{country}: {details['pollution_co2']}")
```

---

### **Key Takeaways**
1. The `sorted()` function can sort lists, dictionaries, and tuples.
2. Use the `key` parameter for custom sorting logic.
3. Use `reverse=True` for descending order.

---

#### **Sorting by Goals Scored**
```python
sorted_by_goals = sorted(football_players.items(), key=lambda x: x[1]["goals_scored"], reverse=True)
for player, details in sorted_by_goals:
    print(f"{player}: {details['goals_scored']} goals")
```


---

## **7. Creating an Interactive App**

Here's a basic Football Explorer App you can build:

```python
def explore_players():
    while True:
        print("\nFootball Player Explorer")
        print("Type a player's name to learn more, 'list' to see all players, or 'exit' to quit.")
        user_input = input("Enter your choice: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "list":
            print("Available players:", ", ".join(football_players.keys()))
        elif user_input in football_players:
            player_details = football_players[user_input]
            for key, value in player_details.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Invalid choice. Try again!")
```

---

## **8. Conclusion**

This workshop covered:
1. Working with nested dictionaries in Python.
2. Using underscores for readability in large numbers.
3. Sorting data with the `sorted()` function.
4. Building an interactive app for data exploration.

This knowledge sets the foundation for working with real-world datasets in Python! 🎉
