
# 🎅 Secret Santa Python Program

Welcome to the **Secret Santa Python Program**! This is a fun project where you will learn how to make a program that assigns Secret Santa gifts randomly. 🎁

## 🧑‍💻 What You’ll Learn
- How to use **lists** to store names.
- How to use the **random** module to shuffle names.
- How to create loops to make the program work.
- How to make sure everyone gets a Secret Santa!

---

## 🚀 Steps to Follow

### 1. Import the `random` Module
The `random` module will help us shuffle the names.

```python
import random
```

### 2. Create a List of Names
Make a list of people who are playing Secret Santa.

```python
participants = ["Alice", "Bob", "Charlie", "Daisy", "Eve"]
```

### 3. Shuffle the List
Randomly mix up the list of names.

```python
random.shuffle(participants)
print("Shuffled participants:", participants)
```

### 4. Assign Secret Santas
Loop through the list and assign each person someone to give a gift to.

```python
for i in range(len(participants)):
    giver = participants[i]
    receiver = participants[(i + 1) % len(participants)]
    print(f"{giver} gives a gift to {receiver}")
```

### How modulo % works 
```python
receiver = participants[(i + 1) % len(participants)]
```
Here’s what it does:

   - ```i + 1```:
        We're moving to the next person in the list.
        For example, if i is 0, i + 1 will be 1 (the next participant).

   - ```% len(participants)```:
        Ensures the index wraps around to the beginning of the list when it reaches the end.
        len(participants) gives the total number of participants.
        When ```i + 1 equals len(participants)```, the modulo operator makes the index wrap back to 0.

Example:
        If ```len(participants) = 5``` and ```i + 1 = 5```, ```5 % 5 = 0``` (the index goes back to the first person).

Result:
        This ensures that the last person (i = len(participants) - 1) is paired with the first person (i = 0), creating a circular assignment.

### 5. Make It Interactive (Optional)
Let people type in their names!

```python
participants = []

while True:
    name = input("Enter a participant's name (or press Enter to stop): ")
    if name == "":
        break
    participants.append(name)

random.shuffle(participants)

for i in range(len(participants)):
    giver = participants[i]
    receiver = participants[(i + 1) % len(participants)]
    print(f"{giver} gives a gift to {receiver}")
```

---

## 🎉 Example Output

If the names are:

```
Alice, Bob, Charlie, Daisy, Eve
```

The program might print:

```
Alice gives a gift to Bob
Bob gives a gift to Charlie
Charlie gives a gift to Daisy
Daisy gives a gift to Eve
Eve gives a gift to Alice
```

---

## 💡 Things to Try
1. Add more names to the list and run the program again.
2. Change the program so nobody gets assigned to themselves. Can you figure it out?
3. Save the results to a text file!

---

## 🧑‍🏫 What Did You Learn?
- How to use lists to store data.
- How to shuffle items randomly with `random.shuffle()`.
- How to use loops to go through a list.
- How the modulo operator `%` works!

---

## 🌟 Ready to Code?

Copy the code and try it yourself! Have fun and happy Secret Santa coding! 🎄✨
