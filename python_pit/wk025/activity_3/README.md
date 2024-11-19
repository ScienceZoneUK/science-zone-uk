
# Python Workshop: Understanding Functions! 🐍

Hello, young coder! Today we’re going to learn about **functions**. Functions are like mini-programs that you can create to do specific jobs in your code. Once you’ve created a function, you can use it again and again without rewriting the code. Let’s dive in and learn what functions are, why they’re useful, and how to create them!

## What You’ll Learn
- **What a function is** and why functions are useful.
- **How to define a function** in Python.
- **Calling a function** to make it do its job.
- **Practice** with simple examples and Reeborg's World!

## Need Help?
If you’re ever curious or need more help, check out [W3Schools Functions](https://www.w3schools.com/python/python_functions.asp) for more details!

---

### Step 1: What is a Function?

- A **function** is a piece of code that does a specific task. 
- Think of a function as a **recipe** that you follow to make a dish. Once you have the recipe, you can make the dish anytime!
- In Python, functions help you organize your code by putting some actions together.

---

### Step 2: Defining (Creating) a Function

1. To create a function in Python, we use the `def` keyword, which means “define.”
2. After `def`, we write the name of the function, like `greet`, and then `()` and a `:`.

   Here’s a simple function that says “Hello!”:

   ```python
   def greet():
       print("Hello, world!")
   ```

3. **Run it!** Nothing will happen yet because we haven’t asked Python to “call” or “use” the function.

---

### Step 3: Calling (Using) a Function

1. To make a function do its job, we need to **call** it by its name and add `()`.
   
   ```python
   greet()  # This will make the function say "Hello, world!"
   ```

2. When you run this, it will display "Hello, world!" because you called the `greet()` function.

---

### Step 4: Adding Information (Parameters) to a Function

1. We can make functions even more useful by giving them **parameters** (extra information). This lets us customize what the function does.
   
   For example, let’s make a function that says hello to someone by name:
   ```python
   def greet(name):
       print("Hello, " + name + "!")
   ```
2. Now, when you call `greet("Alice")`, it will print “Hello, Alice!”.
3. Try calling it with different names, like `greet("Bob")` or `greet("Charlie")`.

---

### Step 5: Repeating Actions with Functions

1. **Challenge:** Let’s create a function that repeats something fun!

   ```python
   def cheer():
       print("Hooray!")
       print("Hooray!")
       print("Hooray!")
   ```
2. Now, each time you call `cheer()`, it will cheer three times. Try it out!

---

### Step 6: Practicing with Reeborg’s World 🐍

- **Reeborg’s World** is a fun way to practice functions by giving Reeborg (a virtual robot) instructions.
- Visit [Reeborg’s World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)
- **Challenge:** Write a function in Reeborg’s World to help him move forward or turn left.

   ```python
   def turn_right():
       turn_left()
       turn_left()
       turn_left()
   ```
- You can then use `turn_right()` to make Reeborg turn right whenever you need!

---

### Final Challenge: Making Your Own Functions

1. Create a function that asks for your favorite food and prints a message about it.
   ```python
   def favorite_food():
       food = input("What’s your favorite food? ")
       print("Yum! I love " + food + " too!")
   ```

2. Call `favorite_food()` and try it out!

---

Congratulations! You’ve learned the basics of functions. Keep practicing and using them, and soon you’ll be a pro at writing and calling functions in Python.

