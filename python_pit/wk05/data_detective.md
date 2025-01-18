
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
    # Additional countries here...
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

### **Exploring the Data**
- **Find countries with an ocean**:
```python
countries_with_ocean = [country for country, details in countries_data.items() if details["has_ocean"]]
print(countries_with_ocean)
```

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

Build an app that allows users to explore country data interactively.

### **Code Example**
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

## **8. Conclusion**

This workshop covered:
1. Working with nested dictionaries in Python.
2. Using underscores for readability in large numbers.
3. Sorting data with the `sorted()` function.
4. Building an interactive app for data exploration.

This knowledge sets the foundation for working with real-world datasets in Python! 🎉

---

Feel free to customize or expand the app for further exploration!
