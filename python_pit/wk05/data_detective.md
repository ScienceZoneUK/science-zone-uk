
# **Exploring the World with Python Dictionaries**

Welcome to this hands-on Python workshop! In this guide, we will explore the powerful capabilities of dictionaries, learn to access and manipulate nested data, and build an interactive app to investigate information about countries.

---

## **Table of Contents**
1. [Introduction to Dictionaries](#1-introduction-to-dictionaries)
2. [Understanding Large Numbers with Underscores](#2-understanding-large-numbers-with-underscores)
3. [The Countries Dictionary](#3-the-countries-dictionary)
4. [Accessing the Dictionary](#4-accessing-the-dictionary)
5. [Being a Data Detective](#5-being-a-data-detective)
6. [Sorting Data with the `sorted()` Function](#6-sorting-data-with-the-sorted-function)
7. [Creating an Interactive App](#7-creating-an-interactive-app)
8. [Conclusion](#8-conclusion)

---

## **1. Introduction to Dictionaries**

A dictionary in Python is a collection of key-value pairs. It allows you to map keys (like a country name) to values (like its population, continent, etc.).

### **Syntax**
```python
# Example dictionary
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
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
population = 1_420_000_000  # India's population
```

Python treats these numbers as normal:
```python
print(1_420_000_000 + 1)  # Output: 1420000001
```

---

## **3. The Countries Dictionary**

Our main data structure is a dictionary of 10 countries. Each country is a key, and its value is another dictionary containing details.

```python
countries_data = {
    "USA": {
        "continent": "North America",
        "population": 331_000_000,
        "pollution_co2": "15.52 metric tons per capita",
        "languages": ["English"],
        "currency": "USD",
        "has_ocean": True
    },
    "India": {
        "continent": "Asia",
        "population": 1_420_000_000,
        "pollution_co2": "1.91 metric tons per capita",
        "languages": ["Hindi", "English"],
        "currency": "INR",
        "has_ocean": True
    },
    "Germany": {
        "continent": "Europe",
        "population": 83_000_000,
        "pollution_co2": "8.04 metric tons per capita",
        "languages": ["German"],
        "currency": "EUR",
        "has_ocean": False
    },
    "Brazil": {
        "continent": "South America",
        "population": 214_000_000,
        "pollution_co2": "2.17 metric tons per capita",
        "languages": ["Portuguese"],
        "currency": "BRL",
        "has_ocean": True
    },
    "Australia": {
        "continent": "Oceania",
        "population": 26_000_000,
        "pollution_co2": "16.96 metric tons per capita",
        "languages": ["English"],
        "currency": "AUD",
        "has_ocean": True
    },
    "China": {
        "continent": "Asia",
        "population": 1_400_000_000,
        "pollution_co2": "7.41 metric tons per capita",
        "languages": ["Mandarin"],
        "currency": "CNY",
        "has_ocean": True
    },
    "Egypt": {
        "continent": "Africa",
        "population": 109_000_000,
        "pollution_co2": "2.39 metric tons per capita",
        "languages": ["Arabic"],
        "currency": "EGP",
        "has_ocean": True
    },
    "South Africa": {
        "continent": "Africa",
        "population": 60_000_000,
        "pollution_co2": "7.56 metric tons per capita",
        "languages": ["Zulu", "Xhosa", "Afrikaans", "English"],
        "currency": "ZAR",
        "has_ocean": True
    },
    "Japan": {
        "continent": "Asia",
        "population": 125_000_000,
        "pollution_co2": "9.31 metric tons per capita",
        "languages": ["Japanese"],
        "currency": "JPY",
        "has_ocean": True
    },
    "Mexico": {
        "continent": "North America",
        "population": 126_000_000,
        "pollution_co2": "3.93 metric tons per capita",
        "languages": ["Spanish"],
        "currency": "MXN",
        "has_ocean": True
    }
}
```

---

## **4. Accessing the Dictionary**

### **Access Nested Values**
Access details about a specific country:
```python
print(countries_data["India"]["population"])  # Output: 1420000000
```

---

## **5. Being a Data Detective**

Imagine you’re a detective solving mysteries in a giant database of countries. Your job is to sift through the data to find specific pieces of information, like which countries are in Asia, which have oceans, or the population of the USA. Python makes this investigation easy by letting us "ask questions" to the dictionary using its tools.

---

### **Task 1: Find Specific Details**

We’ll use Python code to explore the dictionary (`countries_data`) and answer these questions:

1. **Which countries are in Asia?**
2. **Which countries have an ocean?**
3. **What is the population of the USA?**

---

### **Step 1: Understand the Dictionary**

The `countries_data` dictionary is a collection of data about countries. Each key is the name of a country (like "USA" or "India"), and its value is another dictionary containing details about that country, like:
- Its continent (`"continent"`).
- Whether it has an ocean (`"has_ocean"`).
- Its population (`"population"`).

Here’s an example:
```python
countries_data = {
    "USA": {
        "continent": "North America",
        "population": 331_000_000,
        "has_ocean": True
    },
    "India": {
        "continent": "Asia",
        "population": 1_420_000_000,
        "has_ocean": True
    },
    # More countries...
}
```

---

### **Question 1: Which countries are in Asia?**

We’re looking for countries where the `"continent"` value is `"Asia"`. Python allows us to search through the dictionary and extract these countries.

**How It Works:**
- We use a **list comprehension**, which is a way to create a new list by filtering and processing data.
- The code:
  ```python
  asian_countries = [country for country, details in countries_data.items() if details["continent"] == "Asia"]
  ```
  - **`countries_data.items()`**: Breaks the dictionary into pairs of `country` (name) and `details` (data).
  - **`if details["continent"] == "Asia"`**: Filters for countries where the `"continent"` is `"Asia"`.
  - The filtered country names are added to a new list called `asian_countries`.

**Output:**
```python
print(asian_countries)
# Example Output: ['India', 'China', 'Japan']
```

---

### **Question 2: Which countries have an ocean?**

Now, we want to find countries where the `"has_ocean"` value is `True`.

**How It Works:**
- The code:
  ```python
  countries_with_ocean = [country for country, details in countries_data.items() if details["has_ocean"]]
  ```
  - Similar to the first question, this checks each country’s details.
  - **`if details["has_ocean"]`**: Only adds countries where `"has_ocean"` is `True`.

**Output:**
```python
print(countries_with_ocean)
# Example Output: ['USA', 'India', 'Brazil', 'Japan']
```

---

### **Question 3: What is the population of the USA?**

To answer this, we can directly access the `"population"` value for the `"USA"` key in the dictionary.

**How It Works:**
```python
print(countries_data["USA"]["population"])
# Output: 331000000
```

Here:
- **`countries_data["USA"]`**: Gets the details of the USA.
- **`["population"]`**: Extracts the population from those details.

---

### **Summary of Results**

After running the above code:
1. The list of countries in Asia is printed: `['India', 'China', 'Japan']`.
2. The list of countries with an ocean is printed: `['USA', 'India', 'Brazil', 'Japan']`.
3. The population of the USA is printed: `331000000`.

---

### **Breaking Down the Tools Used**

1. **`countries_data.items()`**:
   - Converts the dictionary into pairs of country names and their details.

2. **List Comprehension**:
   - A compact way to filter data:
     ```python
     [country for country, details in countries_data.items() if condition]
     ```

3. **Direct Access**:
   - Use keys (`["USA"]["population"]`) to pinpoint specific data.

By combining these tools, you can easily "detect" patterns and answers in complex data! 🕵️‍♂️


---

## **6. Sorting Data with the `sorted()` Function**

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

## **7. Creating an Interactive App**

# **Build Your Own Country Explorer App**
 In this project, you'll build a simple app that lets users explore data about countries. We'll guide you step-by-step, so follow along and add each part of the code as you go.

---

## **Overview**
The Country Explorer App will:
1. Ask the user for input.
2. Let the user explore country data.
3. Show a list of available countries.
4. Exit when the user wants to quit.

By the end, you'll have a fully functional app that you built from scratch!

---

## **Step 1: Start the Function and Loop**
To begin, we need a function that runs continuously until the user chooses to stop. In Python, we use a `while True` loop for this.

### **What to Do**
1. Create a new function called `explore_country_data`.
2. Inside the function, add a `while True` loop.

### **Code to Add**
```python
def explore_country_data():
    while True:
        # This loop will run continuously until we break out of it
        pass  # Replace this with your logic later
```

---

## **Step 2: Add a Welcome Message**
Let's make the app user-friendly by displaying a title and instructions.

### **What to Do**
1. Inside the loop, print a title for the app.
2. Add instructions for the user.

### **Code to Add**
```python
print("\nCountry Explorer App")
print("Type the name of a country to learn more, 'list' to see all countries, or 'exit' to quit.")
```

---

## **Step 3: Get User Input**
Next, we need to ask the user for their choice. We'll use `input()` to get input and `.strip()` to clean up any extra spaces.

### **What to Do**
1. Ask the user to type their choice.
2. Store the input in a variable and clean it up with `.strip()`.

### **Code to Add**
```python
user_input = input("Enter your choice: ").strip()
```

---

## **Step 4: Handle the "Exit" Command**
What happens if the user types `"exit"`? We want the program to say goodbye and stop running. Use `if` and `break` to handle this.

### **What to Do**
1. Check if the input is `"exit"`.
2. If yes, print "Goodbye!" and break out of the loop.

### **Code to Add**
```python
if user_input.lower() == "exit":
    print("Goodbye!")
    break
```

---

## **Step 5: Handle the "List" Command**
What if the user wants to see all the available countries? Use `countries_data.keys()` to access all the country names.

### **What to Do**
1. Check if the input is `"list"`.
2. Print all the country names in a nice format.

### **Code to Add**
```python
elif user_input.lower() == "list":
    print("Available countries:", ", ".join(countries_data.keys()))
```

---

## **Step 6: Handle a Valid Country Name**
Now we’ll handle situations where the user types a valid country name. If the country exists in the dictionary, we’ll display its details.

### **What to Do**
1. Check if the input matches a country in the dictionary.
2. If yes, loop through the details and print each one.

### **Code to Add**
```python
elif user_input in countries_data:
    country_details = countries_data[user_input]
    for key, value in country_details.items():
        print(f"{key.capitalize()}: {value}")
```

---

## **Step 7: Handle Invalid Input**
What happens if the user types something we don’t recognize? Let’s print an error message for invalid inputs.

### **What to Do**
1. Use an `else` statement for inputs that don’t match any conditions.
2. Print "Invalid choice. Try again!"

### **Code to Add**
```python
else:
    print("Invalid choice. Try again!")
```

---

## **Bringing It All Together**
After completing all the steps, your function should look like this when it’s fully built:

```python
def explore_country_data():
    while True:
        print("\nCountry Explorer App")
        print("Type the name of a country to learn more, 'list' to see all countries, or 'exit' to quit.")
        
        user_input = input("Enter your choice: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "list":
            print("Available countries:", ", ".join(countries_data.keys()))
        elif user_input in countries_data:
            country_details = countries_data[user_input]
            for key, value in country_details.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Invalid choice. Try again!")
```

---

## **Key Takeaways**
- Use a `while True` loop for programs that run continuously.
- Use `.strip()` to clean user input.
- Use `if`, `elif`, and `else` to handle different commands.
- Access data from dictionaries using keys and `.items()`.

Great work! You’ve built a real program that explores data interactively! 🎉


---

## **8. Conclusion**

This workshop covered:
1. Working with nested dictionaries in Python.
2. Using underscores for readability in large numbers.
3. Sorting data with the `sorted()` function.
4. Building an interactive app for data exploration.

This knowledge sets the foundation for working with real-world datasets in Python! 🎉

---

Feel free to customize or expand the app for further exploration!
