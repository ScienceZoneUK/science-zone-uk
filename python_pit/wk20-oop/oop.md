# 📝 Python Workshop: **"Build Your Own Virtual Pet – Learning Object-Oriented Programming!"**

**Target Age:** 10–12 years
**Length:** 1.5 hours
**IDE:** Thonny
**Theme:** Understanding OOP through a Pet Simulator
**Final Project:** Students create a virtual pet using a class, instantiate multiple pets, and interact with them through simple methods.

---

## 1️⃣ Why This Topic Is Important (10 minutes – Discussion)

**Teacher prompts:**

* “How does a video game know what your character looks like, how much health it has, or what it can do?”
* “Why do games like Minecraft or Pokémon have many different creatures or players — but all work in similar ways?”

**Explain simply:**
In programming, we often create **many versions** of something similar — characters, cars, enemies, pets, etc.
Instead of writing separate code for each one, we use **Object-Oriented Programming (OOP)**.
OOP helps us make **blueprints** (called **classes**) to create many **objects** that behave the same way.

**Key Takeaway:**
Classes are **blueprints**.
Objects are the **things built from those blueprints**.
OOP helps us keep code organized, reusable, and easy to manage — this is called **encapsulation**.

---

## 2️⃣ Coding Concepts for This Workshop

Students will learn:

* **Classes** – blueprints for creating objects.
* **Objects** – things created from classes.
* **Attributes** – characteristics (like `name`, `age`, `health`).
* **Methods** – actions an object can do.
* **Instantiation** – creating an object from a class.
* **Encapsulation** – keeping data and functions together inside a class.
* **Using dot notation** – `my_pet.name` or `my_pet.feed()`.

---

## 3️⃣ Project Introduction: **Virtual Pet Simulator 🐕**

**Scenario:**
You’re designing a simple game where you can create and care for your own virtual pets.
Each pet has:

* A **name** and a **hunger level**.
* The ability to **eat** and **play**.
* The hunger level changes based on what happens.

**Requirements:**

1. Create a `Pet` class with attributes (`name`, `hunger`).
2. Add methods for `eat()` and `play()`.
3. Instantiate multiple pets.
4. Interact with pets using their methods.
5. Demonstrate encapsulation (keeping data inside the class).

---

## 4️⃣ Step-by-Step Activities with Testable Code

---

### **Activity 1: Creating a Class and an Object** (10 minutes)

**Introduce:**
A class is like a *blueprint*.
An object is like a *house built from that blueprint*.

```python
# Step 1: Create a simple class
class Pet:
    pass

# Step 2: Create (instantiate) an object from the class
my_pet = Pet()

print(type(my_pet))
```

✅ **Test:** Students should see output similar to `<class '__main__.Pet'>`.
💬 Discuss: “The class is the plan; the object is the actual pet.”

---

### **Activity 2: Adding Attributes** (10 minutes)

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # 0 = full, 10 = starving

my_pet = Pet("Fluffy")

print("Your pet's name is", my_pet.name)
print("Hunger level:", my_pet.hunger)
```

✅ **Test:** Students create their own pets with different names.
💬 Ask: “What happens if you make another pet?” (They’ll see each pet has its own data — that’s encapsulation!)

---

### **Activity 3: Adding Methods (Actions)** (10 minutes)

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5

    def eat(self):
        self.hunger -= 1
        print(self.name, "eats some food. Hunger level:", self.hunger)

    def play(self):
        self.hunger += 1
        print(self.name, "plays happily! Hunger level:", self.hunger)

my_pet = Pet("Fluffy")

my_pet.eat()
my_pet.play()
```

✅ **Test:** Run it and see the hunger level change.
💬 Ask: “What’s happening inside the pet?” (We’re changing the data stored in that object.)

---

### **Activity 4: Multiple Objects (Instantiation)** (10 minutes)

```python
pet1 = Pet("Fluffy")
pet2 = Pet("Spike")

pet1.eat()
pet2.play()

print(pet1.name, "hunger:", pet1.hunger)
print(pet2.name, "hunger:", pet2.hunger)
```

✅ **Test:** Run and compare pets — they have independent data!
💬 Discuss: “Each pet is an object created from the same class — that’s **instantiation**.”

---

### **Activity 5: Encapsulation in Action** (10 minutes)

Explain that **encapsulation** means keeping data and actions together — the pet takes care of itself!

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5

    def feed(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0
        print(self.name, "was fed. Hunger level:", self.hunger)

    def get_status(self):
        if self.hunger < 3:
            print(self.name, "is happy and full!")
        else:
            print(self.name, "is getting hungry...")
```

✅ **Test:**

```python
pet1 = Pet("Luna")
pet1.feed(2)
pet1.get_status()
```

💬 Ask: “Why don’t we just change `pet1.hunger` directly?”
🧠 Answer: Because we want the **class** to control how hunger changes — that’s safer and cleaner (encapsulation).

---

### **Activity 6: Build the Full Virtual Pet Game!** (20 minutes)

Bring it all together into a mini interactive program:

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5

    def feed(self):
        self.hunger -= 1
        if self.hunger < 0:
            self.hunger = 0
        print(self.name, "has eaten! Hunger level:", self.hunger)

    def play(self):
        self.hunger += 1
        print(self.name, "had fun! Hunger level:", self.hunger)

    def check_status(self):
        if self.hunger < 3:
            print(self.name, "is happy and full! 😊")
        elif self.hunger < 7:
            print(self.name, "is doing okay 😐")
        else:
            print(self.name, "is starving! 😱")

# --- Game Loop ---
name = input("What is your pet's name? ")
my_pet = Pet(name)

while True:
    print("\n1. Feed your pet")
    print("2. Play with your pet")
    print("3. Check status")
    print("4. Quit")

    choice = input("Choose an action: ")

    if choice == "1":
        my_pet.feed()
    elif choice == "2":
        my_pet.play()
    elif choice == "3":
        my_pet.check_status()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Not a valid option.")
```

✅ **Test:** Run and play! Feed, play, and check on your pet.
💬 Ask: “Why does each pet remember its own hunger level?” (Encapsulation!)

---

## 5️⃣ Wrap-Up & Reflection (10 minutes)

**Discussion Prompts:**

* “What’s a class? What’s an object?”
* “What is instantiation?”
* “How does encapsulation make coding easier?”
* “How could you extend this program?” (Add happiness, tiredness, or multiple pets.)

**Mini-Challenge (if time allows):**
Add a new method, `sleep()`, that lowers hunger and prints a message.

---

## 6️⃣ Materials Needed

* Thonny installed.
* Whiteboard or slides for simple OOP diagrams.
* Optional: worksheet with key definitions:

  * Class = Blueprint
  * Object = Thing made from the blueprint
  * Instantiation = Making an object
  * Encapsulation = Keeping data & methods together

---

## ✅ Learning Outcomes Recap

By the end of the workshop, students should be able to:

* ✅ Explain the difference between a **class** and an **object**.
* ✅ Understand and demonstrate **instantiation**.
* ✅ Explain the benefits of **encapsulation**.
* ✅ Write a simple OOP-based Python program in Thonny.
