# 📝 Python Workshop: **"Saving Your Game – An Introduction to File Handling"**

**Target Age:** 10–12 years

**Length:** 1.5 hours

**IDE:** Thonny

**Theme:** Writing and reading from text files in Python.

**Final Outcome:** Students create a program that saves and loads a high score list from a text file.

---

## 1️⃣ Why This Topic is Important (10 minutes – Discussion)

**Starter questions:**

* "What happens to your progress when you play a game and then close it? How does it know where you left off?"
* "How does your phone remember your contacts, notes, or playlists?"
* "Where do websites store your login details so you don’t have to type them every time?"

**Key point:**
File handling is how programs **store information permanently** so it’s still there the next time you run the program.
Without files, all data disappears when the program stops.

---

## 2️⃣ Coding Concepts for This Workshop

Students will learn:

* **When to use file handling** – saving progress, storing scores, keeping lists.
* **Creating a text file** in Python.
* **Writing to a file** – using `open(filename, "w")` and `.write()`.
* **Appending to a file** – using `"a"`.
* **Reading from a file** – using `open(filename, "r")` and `.read()` / `.readlines()`.
* **Closing files** – `.close()` or using `with open(...)`.
* **Basic string formatting** for file output.
* Recognising **permanent vs. temporary data**.

---

## 3️⃣ Project Introduction: **High Score Saver** 🎯

**Scenario:**
We are going to make a program that:

1. Lets the player enter their name and score.
2. Saves the score to a file called `scores.txt`.
3. Can read and display all saved scores.

**Why this project?**

* Relates to games (engaging).
* Demonstrates writing and reading in one program.
* Gives a tangible file students can open in a text editor to see their data.

---

## 4️⃣ Step-by-Step Activities with Testable Code

---

### **Activity 1: Writing to a File** (10 minutes)

```python
# Writing to a file
file = open("scores.txt", "w")  # 'w' means write (overwrites existing file)
file.write("Alice: 100\n")
file.write("Bob: 200\n")
file.close()
print("Scores saved!")
```

✅ Test: Run the program, then open `scores.txt` in a text editor to see if it worked.

---

### **Activity 2: Appending to a File** (10 minutes)

```python
# Appending to a file
file = open("scores.txt", "a")  # 'a' means append (adds to file)
file.write("Charlie: 150\n")
file.close()
print("New score added!")
```

✅ Test: Run multiple times, check that new lines keep adding instead of replacing.

---

### **Activity 3: Reading from a File** (10 minutes)

```python
# Reading from a file
file = open("scores.txt", "r")  # 'r' means read
contents = file.read()
file.close()
print("Current scores:\n", contents)
```

✅ Test: Students see the full list printed.

---

### **Activity 4: Using `with open(...)`** (5 minutes)

Explain that this automatically closes the file:

```python
with open("scores.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes \n
```

---

### **Activity 5: Building the High Score Program – Step 1** (10 minutes)

Let’s add a new score and then read all scores:

```python
name = input("Enter your name: ")
score = input("Enter your score: ")

with open("scores.txt", "a") as file:
    file.write(name + ": " + score + "\n")

print("\nAll Scores:")
with open("scores.txt", "r") as file:
    for line in file:
        print(line.strip())
```

✅ Test: Students run it, add names, and see updated scoreboard.

---

### **Activity 6: Recognising When to Use File Handling** (10 minutes)

Class brainstorm:

* Saving high scores.
* Storing player inventories.
* Keeping lists (shopping, tasks).
* Logging events.
* Remembering settings/preferences.

---

### **Activity 7: Bonus Challenge – Sorting Scores** (Optional – 15 minutes)

Have them modify the reading section to sort scores highest to lowest.

---

## 5️⃣ Wrap-Up (10 minutes)

* Review objectives:

  * What file modes do we know? (`"w"`, `"a"`, `"r"`)
  * What is the syntax for writing and reading?
  * When do we use file handling?
* Quick challenge: Write a program that saves 3 favorite foods to `foods.txt` and then reads them back.

---

## Materials Needed

* Thonny installed.
* Access to the file system so students can open `.txt` files.
* Whiteboard for brainstorming.
