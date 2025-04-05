
# 🔁 Loop It, Sort It, Search It!

A 1.5-hour Python workshop for 13-year-olds using the **PRIMM** framework and **semantic wave theory** to explore `for` loops, data structures, and basic algorithms like searching and sorting.

---

## 🧠 Learning Goals
- Understand and apply `for` loops using `range()`, list iteration, and `enumerate()`
- Use debugging to improve code reading skills
- Implement Linear Search, Binary Search, and Bubble Sort

---


### 0. Setup (5 mins)
- Open your Python environment (e.g. Replit or Thonny)
- Create a new file: `search_sort_loops.py`

---

## Standard search algorithms

Since computers were created, users have devised programs, many of which have needed to do the same thing. 
As a result, common algorithms have evolved and been adopted in many programs.

Two algorithms often used are searches and sorts:

  - searches allow a set of data to be examined and for a specific item to be found
  - sorts allow a data set to be sorted into order

**Methods of searching include:**
  - linear search
  - binary search

**Methods of sorting include:**
  - bubble sort
  - merge sort
  - insertion sort

Examples to test [click here](https://www.w3schools.com/dsa/dsa_data_arrays.php)

---

### 1. Predict (15 mins)

#### Activity 1.1 – Predict What Happens
```python
numbers = [4, 8, 15, 16, 23, 42]
target = 15
for num in numbers:
    if num == target:
        print("Found it!")
```
- What do you think this code will print?
- Add your guess as a comment before running.

---

### 2. Run (15 mins)
Create one program, one loop at a time create a custom function and run it. Print a message in each function  
explaining the loop. At the end you will have 4 functions running a loop and a print statement.
Example:
```python
def my_func():
  print("something will happen")

print(my_func())
```
#### Activity 2.1 – Count from 0 to 4
```python
for i in range(5):
    print(i)
```

#### Activity 2.2 – Loop through a list
```python
animals = ["cat", "dog", "elephant"]
for pet in animals:
    print(pet)
```

#### Activity 2.3 – Use `enumerate()`
```python
for index, pet in enumerate(animals):
    print(index, pet)
```

#### Mini Challenge
- Change the list to your favourite snacks, games, or Pokémon.

---

### 3. Investigate (20 mins)
**linear search**
A linear search algorithm simply moves up the list and checks each item,  
the data in the list does not need to be in order. However, as the list gets longer   
the algorithm takes longer to run, making it inefficient for large lists.  

In pseudo-code, this may look like:
```
find <-- 1
found <-- False
length <-- length(list)
counter <-- 0

WHILE found = False AND counter <= length
     IF list[counter] = find THEN
          found <-- True
          OUTPUT 'Found at position', counter
        ELSE
          counter <-- counter + 1
        ENDIF
ENDWHILE
IF found = False THEN
   OUTPUT 'Item not found'
ENDIF
```

#### Activity 3.1 – Linear Search
```python
def linear_search(data, target):
    for item in data:
        if item == target:
            return "Found!"
    return "Not Found"

print(linear_search([5, 3, 7, 1, 8], 7))
```
- Try searching for different numbers.
- What happens if the target isn't in the list?

---

#### Activity: 🐞 Debug the Loop!

##### Bug 1:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
print(fruit)
```

##### Bug 2:
```python
animals = ["dog", "cat", "fox"]
for i in range(4):
    print(animals[i])
```

##### Bug 3:
```python
numbers = [1, 2, 3]
for number in numbers:
    print(num)
```

##### Bug 4:
```python
pets = ["hamster", "parrot", "lizard"]
for pet in pets:
    if pet == "dog":
        print("Found it!")
```

✅ Fix the bugs and explain what was wrong in each!

---

### 4. Modify (20 mins)
---


> 🚨 **Learn**  
> 
> In Python, // is the floor division operator.

🔢 What it does:
It divides two numbers and rounds the result down to the nearest whole number (also called integer division or floor division).
✅ Examples:
```python
print(7 // 2)     # Output: 3
print(8 // 2)     # Output: 4
print(9 // 4)     # Output: 2
```
Even though 7 / 2 is 3.5, 7 // 2 gives 3 because it drops the decimal.


---


#### Activity 4.1 – Binary Search


# 🔍 Binary Search

Binary search is another example of a **searching algorithm**, and it's more efficient than linear search — **but it only works if the list is sorted**.

---

## ⚙️ How Binary Search Works

With **each loop**, binary search removes **half of the data** from the search space. It does this using **indexes**, which represent the positions of items in a list.

To find the **midpoint**, it adds the **lowest index** to the **highest index** and divides by 2:

> Midpoint = (Low + High) // 2

It uses **floor division (`//`)**, which rounds down to the nearest whole number.

---

## 🧠 Example Calculation

If the highest index is `8` and the lowest is `0`:
```
Mid = (0 + 8) // 2 = 4
```

You can round up or down, but you must stay consistent throughout the search.

---

## 🔄 Binary Search Algorithm Steps

1. Set your pointer to the **middle item**.
2. If it matches the search item — 🎯 done!
3. If the search item is **greater**, ignore the **lower half**.
4. If the search item is **less**, ignore the **upper half**.
5. Repeat with the new half until found, or list is empty.

---

## 🧪 Example: Searching for 7 in this list:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### 🔍 Trace Table

| Search Term | Start | End | Mid | Found | List Searched      |
|-------------|-------|-----|-----|-------|---------------------|
| 7           | 1     | 10  | 5   | False | [1–10]              |
|             | 6     | 10  | 8   | False | [6–10]              |
|             | 6     | 7   | 6   | False | [6, 7]              |
|             | 7     | 7   | 7   | True  | [7]                 |

---

## 🧠 Pseudo-code for Binary Search

```text
Find <-- 7
Found <-- False
Start <-- 0
End <-- length(list)

WHILE Found = False AND Start <= End
     Mid <-- (Start + End) DIV 2

     IF list[Mid] = Find THEN
        OUTPUT 'Found at' +  Mid
        Found <-- True
     ELSE
        IF list[Mid] > Find THEN
           End <-- Mid - 1
        ELSE
           Start <-- Mid + 1
        ENDIF
     ENDIF
ENDWHILE

IF Found = False THEN
     OUTPUT 'Not found'
ENDIF
```

---

✏️ **Remember:** Binary search is fast **because it halves the search space** each time — that’s much quicker than checking each item one-by-one like linear search!





```python
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if data[mid] == target:
            return f"Found at index {mid} in {steps} steps"
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"

print(binary_search([1, 3, 5, 7, 9, 11, 13], 9))
```
Challenge:
  - Try changing the target.
  - Try a bigger list (copy + paste extra numbers).
  - What happens if the list isn’t sorted?



#### Activity 4.2 – Bubble Sort


# 🫧 Bubble Sort

Bubble sort is a **simple sorting algorithm** that repeatedly steps through the list, compares pairs of items, and **swaps them** if they are in the wrong order.

It gets its name because the largest unsorted values "bubble up" to the top (end) of the list.

---

## 🔄 How Bubble Sort Works

1. Start at the beginning of the list.
2. Compare each pair of adjacent items.
3. If the first is greater than the second, swap them.
4. Continue until you reach the end of the list.
5. Repeat the entire process until the list is sorted.

---

## 📊 Visual Example

Unsorted list:
```
[5, 3, 8, 1]
```

Step-by-step passes:

**Pass 1:**
- Compare 5 and 3 → swap → [3, 5, 8, 1]
- Compare 5 and 8 → no swap → [3, 5, 8, 1]
- Compare 8 and 1 → swap → [3, 5, 1, 8]

**Pass 2:**
- Compare 3 and 5 → no swap → [3, 5, 1, 8]
- Compare 5 and 1 → swap → [3, 1, 5, 8]
- Compare 5 and 8 → no swap → [3, 1, 5, 8]

**Pass 3:**
- Compare 3 and 1 → swap → [1, 3, 5, 8]
- Compare 3 and 5 → no swap
- Compare 5 and 8 → no swap

Sorted! 🎉

---

## 

## 📋 Pseudo-code & 💻 Python Code

```text
REPEAT for each item in the list
    FOR each pair of adjacent items
        IF the first item > second item THEN
            SWAP them
        ENDIF
    ENDFOR
ENDREPEAT
```

```python
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([5, 3, 8, 1]))
```

---


## 🧠 Key Concepts

- Bubble sort is easy to understand but **not very efficient** for large lists.
- It compares **pairs** and **swaps** if needed.
- The biggest numbers move to the end each round.

---

✏️ **Try It Yourself:**  
Use bubble sort to sort your list of favourite numbers, scores, or Pokémon stats!


```python
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([9, 3, 1, 5, 13, 12]))
```

---

### 5. Make (15 mins)

#### Activity 5.1 – Your Own Search Game
```python
def my_search(my_list, target):
    for i, item in enumerate(my_list):
        if item == target:
            return f"Found at position {i}"
    return "Not found"

print(my_search(["pizza", "tacos", "sushi", "noodles"], "sushi"))
```

🧠 Try using `input()` to let a friend type in the target!

---

## 🧠 Wrap-Up (5 mins)

### Questions to Ask:
- What’s the difference between linear and binary search?
- What kind of loop does a bubble sort use?
- Where could you use this in your own games or tools?

---

## 🧠 Semantic Wave Summary

| Concept Level | Activity       | Description                                  |
|---------------|----------------|----------------------------------------------|
| Everyday      | Predict         | Real-world examples, guessing code output    |
| Abstract      | Investigate     | Dive into logic, syntax, and loop structure  |
| Concrete      | Make            | Apply knowledge to build something personal  |
