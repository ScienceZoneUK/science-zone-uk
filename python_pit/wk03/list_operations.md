
# Basic Functions and Operations on Python Lists

Python lists are incredibly versatile and come with built-in functions and operations that make working with them easier. Here’s a quick guide to some of the most common list functions and operations.

---

## 🔍 Accessing Elements in a List

You can access elements of a list using their **index** (starting at 0).

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
```

---

## ➕ Adding Elements

### 1. **`append()`**  
Adds a single item to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

### 2. **`extend()`**  
Adds multiple elements to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
```

### 3. **`insert()`**  
Adds an item at a specific index.

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

---

## ➖ Removing Elements

### 1. **`remove()`**  
Removes the first occurrence of a specific value.

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']
```

### 2. **`pop()`**  
Removes and returns the item at a specific index (default is the last item).

```python
fruits = ["apple", "banana", "cherry"]
last_item = fruits.pop()
print(last_item)  # Output: cherry
print(fruits)  # Output: ['apple', 'banana']
```

### 3. **`clear()`**  
Removes all items from the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []
```

---

## 🔄 Modifying Lists

### **Replace Elements**

You can directly modify elements by accessing them using their index.

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

---

## 🔢 Sorting and Reversing

### 1. **`sort()`**  
Sorts the list in ascending order (can also sort in descending order).

```python
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]
```

### 2. **`reverse()`**  
Reverses the order of the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']
```

---

## 🔢 Aggregation Functions

### 1. **`len()`**  
Returns the number of items in the list.

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3
```

### 2. **`sum()`**  
Returns the sum of numeric elements in the list.

```python
numbers = [1, 2, 3]
print(sum(numbers))  # Output: 6
```

### 3. **`min()` / `max()`**  
Finds the smallest and largest elements in the list.

```python
numbers = [3, 1, 4, 2]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 4
```

---

## 🔍 Searching in Lists

### 1. **`in` Operator**  
Checks if an item exists in the list.

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
```

### 2. **`index()`**  
Finds the index of the first occurrence of an item.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1
```

---

## 📜 Copying Lists

### 1. **`copy()`**  
Creates a copy of the list.

```python
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)  # Output: ['apple', 'banana', 'cherry']
```

### 2. Using Slice Notation
```python
fruits = ["apple", "banana", "cherry"]
new_list = fruits[:]
print(new_list)  # Output: ['apple', 'banana', 'cherry']
```

---

## 🚀 Advanced Operations

### 1. **List Comprehensions**  
A concise way to create lists.

```python
numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16]
```

### 2. **`enumerate()`**  
Iterates through the list with an index.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

With these functions and operations, you can unlock the full potential of Python lists. Practice each concept with examples to master them!

---
