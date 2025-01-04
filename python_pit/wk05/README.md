
# Python Workshop: Follow-Along Guide to Dictionaries

## **Workshop Title:** Mastering Python Dictionaries with Planets
**Duration:** 1 Hour  
**Objective:** Learn Python dictionaries step-by-step and visualize data using Turtle.

---


# 1. Introduction to Dictionaries

## What is a Dictionary?

Imagine you are 100yrs 👵 , you hear someone use the word "Riz" and you're not sure what it means. You might look it up online 💻. Before the internet 💾, people used dictionariese📚books 🥱 that matched words (keys) to their meanings (values). Python dictionaries are:

- **Ordered** (since Python 3.7): The order in which you add items is remembered.
- **Mutable**: You can add, remove, or change items after creating the dictionary.
- **Unique**: Each key must be unique, but values can repeat.

### Python also has other data structures you’ll use:
- **List**: A collection of items in order (e.g., `["apple", "banana"]`).
- **Tuple**: Similar to lists, but you can’t change them after creating (e.g., `("apple", "banana")`).
- **Set**: Unordered collection of unique items (e.g., `{ "apple", "banana" }`).

### Activity 1: Write this code to create a simple dictionary.
```python
example = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}
print(example)
```

---

## **2. Creating a Dictionary**

### Activity 2: Create a Dictionary for Mercury
Write a dictionary for Mercury with these keys and values:

- `name`: Mercury  
- `colour`: "Red"
- `size`:  3,032 # miles diameter
- `orbit`: 88 # Days to orbit sun
- `info`: The smallest and fastest planet.

Here’s how it should look:
```python
mercury = {
    "name": "Mercury",
    "colour": "Red",
    "size": 3,032,
    "orbit": 88,
    "info": "The smallest and fastest planet."
}
```
---
### Questions 

The data in a dictionary is known as ```Key : Value``` pairs. Eg: ``` "name" : "Chris"``` ``` "age" : 100``` 

- What data type is the key?
- What data type is the value?

## **3. Accessing Dictionary Data**

- Resources: [W3Schools](https://www.w3schools.com/python/python_dictionaries_access.asp)


There are many ways we can access items of a Python dictionary. Python has built-in methods to interact with dictionaries. The easiest way is by referring to its key inside the square brackets.

The bracket notation is best used when we want to access a single item in the dictionary. For example, to get the type of pencil, we can code as follows:

```print(mercury["name"])  # Output: Mercury```

Get(): Another way to access an item is the get method. Similar to the bracket notation the get function fetches the value based on the key passed.

```x = mercury.get(“name”)```

Keys(): The keys method can be used to retrieve all the keys of the collection. Running this code, the dictionary will return all the keys within it.
```python
x=mercury.keys()
print(x)
```

Values(): This method is similar to the keys function. The difference is that the values method would return the current values in the dictionary instead of keys. This can be useful if want to see just the values to locate particular values to be modified.
```python
x=mercury.values()
print(x)
```

Items(): The items method of python returns the full dictionary as key-value pair.
```python
x=mercury.items()
print(x)
```

### Activity 3: Retrieve Data from Mercury
Look at the resources for some examples of printing data.
Write some code to access data from your Mercury dictionary (Use different python dictionary methods and store in varaiables):

```python
print(f"Write a short paragraph \n using the planet data \n that can be used for other planets") #Write a short paragraph using fstrings
```


---

## **4. Expanding a Dictionary**

### Activity 4: Add a New Planet
Add this dictionary for Venus to your code:
```python
venus = {
    "name": "Venus",
    "colour": "????",
    "size": "????",
    "orbit": "????",
    "info": "The hottest planet in our solar system."
}
```
Run your program to ensure there are no errors.

---

## **5. Updating a Dictionary**

### Activity 5: Modify Mercury’s Data
Update Mercury’s `info` key and add a new key for temperature:
```python
mercury["info"] = "Mercury is closest to the Sun."
mercury["temperature"] = "hot"
print(mercury)
```

---

## **6. Looping Through Dictionary Data**

### Activity 6: Loop Through Mercury’s Data
Add this loop to print all keys and values for Mercury:
```python
for key, value in mercury.items():
    print(f"{key}: {value}")
```

---

## **7. Using Turtle to Draw Single Dictionary Data**

### Activity 7: Draw Mercury Using Turtle
Write this program to visualize Mercury using Turtle:

```python
import turtle

planet = {
    "name": "Mercury",
    "colour": "brown",
    "size": 15,
    "position": (100, 100)
}

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Planet Visualization")

planet_turtle = turtle.Turtle()
planet_turtle.shape("circle")

# Use the dictionary data to set the turtle's attributes.
planet_turtle.color(planet["colour"])
planet_turtle.penup()
planet_turtle.goto(planet["position"])
planet_turtle.begin_fill()
planet_turtle.circle(planet["size"])
planet_turtle.end_fill()

turtle.done()
```

---

## **8. Introduction to Nested Dictionaries**

- Resources [W3Schools](https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp)

### Activity 8: Create a Nested Dictionary
Combine multiple planets into one dictionary:

```python
planets = {
    "Mercury": {
        "colour": "brown",
        "size": 15,
        "position": (100, 100)
    },
    "Venus": {
        "colour": "yellow",
        "size": 20,
        "position": (200, 150)
    },
    "Earth": {
        "colour": "blue",
        "size": 25,
        "position": (-100, -100)
    }
}
```

---

## **9. Using Turtle to Draw Multiple Planets**

### Activity 9: Draw All Planets Using Nested Dictionaries
Write this code to loop through the `planets` dictionary and draw all planets:

```python
import turtle

#Add the planets dictionary

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Visualization")

planet_turtle = turtle.Turtle()
planet_turtle.shape("circle")

for planet_name, planet_data in planets.items():
    planet_turtle.color(planet_data["colour"])
    planet_turtle.penup()
    planet_turtle.goto(planet_data["position"])
    planet_turtle.begin_fill()
    planet_turtle.circle(planet_data["size"])
    planet_turtle.end_fill()

turtle.done()
```

---

## **10. Wrap-Up**

### Key Points:

1. Dictionaries store key-value pairs.

2. Nested dictionaries help organize complex data.

3. Turtle allows you to visualize dictionary data.

### Challenge:

Create a solar system with at least five planets and visualize it using Turtle.
