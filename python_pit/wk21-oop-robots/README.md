# 📝 1.5-Hour Python Workshop — OOP + Arrays + Functions (Ages 10–12)

**IDE:** Thonny • **Length:** 1.5 hours (90 minutes)
**Theme / Project:** **Robot Team Manager** — create `Robot` objects, store them in a list, and use functions to manage and interact with the team.

---

# 1. Why this topic is important (10 minutes — discussion)

Start with a short conversation so students see the point.

Ask/Prompt:

* “Imagine a game with lots of characters (pets, robots, players). Would you write separate code for each one?”
* “How would you keep everything tidy if you want many similar things that can act on their own?”

Key teacher points:

* **Classes** let us create a blueprint (a recipe) for many similar things.
* **Objects** are the actual things made from that blueprint.
* **Lists (arrays)** let us hold many objects together so we can do things to all of them.
* **Functions** let us make reusable actions that work on objects or lists of objects.
* Together, these help build games and apps that are organized, easier to change, and less buggy.

Learning goals (student-friendly):

* I can explain what a **class** and an **object** are and how they differ.
* I can **instantiate** (make) objects from a class.
* I can show why it's good to keep data inside a class (**encapsulation**).
* I can use **lists** to store many objects and write **functions** to work with them.

---

# 2. Coding concepts we will cover

* Classes & objects (`class`, `__init__`)
* Attributes and methods (`self`, `self.attribute`, `def method(self, ...)`)
* Instantiation (`robot = Robot("R1")`)
* Encapsulation (keeping data & behavior together)
* Lists (arrays) of objects: `robots = [robot1, robot2]`
* Functions that operate on lists and objects (`def add_robot(robots, ...)`)
* Loops (`for`) to handle many objects
* Simple I/O with `input()` and `print()` for interaction
* (Optional) `sorted()` and `key=` to show finding the strongest robot

---

# 3. Project introduction & requirements

**Project:** Robot Team Manager — students build a small text program to:

1. Define a `Robot` class with name, power, and battery (or health) attributes.
2. Add methods like `attack()`, `recharge()` and `status()` inside the class.
3. Instantiate multiple robots and store them in a list.
4. Write functions to add a robot, remove a robot, list robots, and make all robots do an action.
5. Run a short loop so the user can choose actions from a menu.

**Must-haves:**

* A `Robot` class with at least two attributes and two methods.
* A list to hold the robots.
* At least two functions that manipulate the list (e.g., `add_robot`, `remove_robot`, `team_attack`).
* Demonstration of encapsulation: robot data should be changed via methods, not by external code directly (show both and discuss).

---

# 4. Workshop timeline & step-by-step activities (90 minutes total)

Times are suggestions — adapt to class pace.

### Activity 0 — Setup (5 minutes)

* Make sure Thonny is open.
* New file: `robot_manager.py`
* Save early and often.

---

### Activity 1 — Simple class + instantiate (15 minutes)

**Goal:** Understand class, object, instantiation, attributes.

```python
# robot_basic.py
class Robot:
    def __init__(self, name):
        self.name = name     # attribute
        self.power = 10      # starting power

# Create two robot objects (instantiation)
r1 = Robot("Bolt")
r2 = Robot("Spark")

print(r1.name, "power:", r1.power)
print(r2.name, "power:", r2.power)
```

Test: Run — students should see both robot names and power printed.
Talk: Class = blueprint; each `Robot(...)` call makes a new object with its own data.

---

### Activity 2 — Add methods & encapsulation (15 minutes)

**Goal:** Learn methods and why to change attributes via methods.

```python
# robot_methods.py
class Robot:
    def __init__(self, name):
        self.name = name
        self.power = 10

    def attack(self):
        # robot uses power to attack
        if self.power >= 2:
            self.power -= 2
            print(self.name, "attacks! Power is now", self.power)
        else:
            print(self.name, "is too weak to attack!")

    def recharge(self, amount=5):
        self.power += amount
        print(self.name, "recharges by", amount, "-> power:", self.power)

# Test
r = Robot("Nova")
r.attack()
r.attack()
r.recharge()
```

Test: Run; students should call `attack()` until `power` gets low, then recharge.
Discuss: Why not change `r.power` directly? (Use method to control behavior and prevent invalid states.)

---

### Activity 3 — Store objects in a list (arrays) (10 minutes)

**Goal:** Use a list to keep many robots and loop over them.

```python
# robot_list.py
class Robot:
    def __init__(self, name):
        self.name = name
        self.power = 10

    def status(self):
        print(self.name, "power:", self.power)

# Create list of robots
robots = [Robot("Bolt"), Robot("Spark"), Robot("Nova")]

# Loop through the list
for bot in robots:
    bot.status()
```

Test: Run and see each robot's status printed.
Talk: Lists let us hold lots of objects and do the same action to each.

---

### Activity 4 — Functions that operate on the list (15 minutes)

**Goal:** Write reusable functions to manage the robot team.

```python
# robot_functions.py
class Robot:
    def __init__(self, name):
        self.name = name
        self.power = 10

    def status(self):
        print(self.name, "power:", self.power)

    def attack(self):
        if self.power >= 2:
            self.power -= 2
            print(self.name, "attacks! power:", self.power)
        else:
            print(self.name, "can't attack.")

def add_robot(team, name):
    team.append(Robot(name))
    print(name, "added to the team.")

def remove_robot(team, name):
    for bot in team:
        if bot.name == name:
            team.remove(bot)
            print(name, "removed from team.")
            return
    print(name, "not found.")

def team_status(team):
    print("Team status:")
    for bot in team:
        bot.status()

# Test the functions
team = []
add_robot(team, "Bolt")
add_robot(team, "Spark")
team_status(team)
remove_robot(team, "Bolt")
team_status(team)
```

Test: Run — confirm add/remove/status work.
Discuss: Functions let us reuse logic and keep the main program tidy.

---

### Activity 5 — Build interactive menu combining all pieces (20 minutes)

**Goal:** Put class, list, and functions into an interactive program.

```python
# robot_manager.py
class Robot:
    def __init__(self, name):
        self.name = name
        self.power = 10

    def status(self):
        print(self.name, "power:", self.power)

    def attack(self):
        if self.power >= 2:
            self.power -= 2
            print(self.name, "attacks! power:", self.power)
        else:
            print(self.name, "is too weak to attack!")

    def recharge(self, amount=5):
        self.power += amount
        print(self.name, "recharges by", amount, "-> power:", self.power)

def add_robot(team, name):
    team.append(Robot(name))
    print(name, "added.")

def remove_robot(team, name):
    for bot in team:
        if bot.name == name:
            team.remove(bot)
            print(name, "removed.")
            return
    print(name, "not found.")

def team_attack(team):
    print("Team attacks!")
    for bot in team:
        bot.attack()

def show_team(team):
    for i, bot in enumerate(team, start=1):
        print(i, "-", bot.name, "power:", bot.power)

# --- main program ---
def main():
    team = []
    while True:
        print("\nRobot Team Manager")
        print("1) Add robot")
        print("2) Remove robot")
        print("3) Show team")
        print("4) Team attack")
        print("5) Recharge all")
        print("6) Quit")
        choice = input("Choose (1-6): ")

        if choice == "1":
            name = input("Robot name: ")
            add_robot(team, name)

        elif choice == "2":
            name = input("Robot name to remove: ")
            remove_robot(team, name)

        elif choice == "3":
            show_team(team)

        elif choice == "4":
            team_attack(team)

        elif choice == "5":
            for bot in team:
                bot.recharge()
            print("All recharged.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
```

Test: Run in Thonny, add a few robots, show team, make team attack, recharge, remove, quit.
Tip for teacher: Demonstrate a “bug” scenario (e.g., attempt team attack when team is empty) and show how to guard against it in code (e.g., `if not team: print("No robots!")`).

---

### Activity 6 — Extend / Challenge (10 minutes)

Options depending on class speed:

1. **Find the strongest robot** — add function:

```python
def strongest_robot(team):
    if not team:
        print("No robots.")
        return
    best = max(team, key=lambda b: b.power)
    print("Strongest:", best.name, "power:", best.power)
```

2. **Sort robots by power** and display.
3. **Save / load** simple text file of team (bonus: file I/O).
4. **Add more attributes** (e.g., `armor`) and methods using them.

Students pick one small extension, implement, and demo.

---

# 5. Teaching notes & common misconceptions

* **Misconception:** “Class is the same as object.” Reinforce: class = blueprint, object = thing built from it.
* **Pitfall:** Changing one object’s attribute doesn't change others — show with two robots to prove independence.
* **Good practice:** Use methods to change attributes (encapsulation) so you can check rules (e.g., `power` can’t go negative).
* **Debug tip:** Use `print()` inside methods to see when they run and what they change.

---

# 6. Materials & setup

* Computers with Thonny installed.
* Python 3 (Thonny default).
* Project starter file optionally pre-created with basic `Robot` class.
* Whiteboard or slide with quick class/object diagram.

---

# 7. Wrap-up & assessment (5–10 minutes)

Quick checks (oral / mini-quiz):

* “What is instantiation?” (Answer: making an object from a class.)
* “Why use a method instead of changing `robot.power` directly?” (Answer: control & safety — encapsulation.)
* Ask a volunteer to demonstrate: add a robot, team attack, recharge.

Optional small homework:

* Add a `heal()` method or a `level` attribute and a function that levels up the whole team.
* Write a short paragraph: “When would a list of objects be better than single variables?”

---

# 8. Ready-to-run files (quick summary)

You can copy the `robot_manager.py` program above into Thonny and run it as the full classroom exercise. Break the class into the activities above, have students type/modify code, then run and test.
