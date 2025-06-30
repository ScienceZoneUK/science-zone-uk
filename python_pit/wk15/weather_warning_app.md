 
# 🌞 Sun Smart System — Python Coding Workshop

**Ages**: 12–14  
**Length**: 1 hour 15 minutes  
**Focus**: Computational Thinking • Python • Real-World Problem Solving • Visual Outputs

---

## 🏖️ Context

It’s the middle of summer, the sun’s blazing, and it’s getting *hot*! Living near the coast, we’re no strangers to sunshine — but how can we use code to help ourselves and others stay safe in the sun?

In this creative and hands-on workshop, we’ll learn how to **turn real-world problems into computer programs** using **computational thinking** and Python. Then we’ll make it visual with **Turtle graphics** — drawing over a sunny image to share a summer heat warning.

---

## 🧠 What We’ll Learn

- How to think like a computer (inputs → process → outputs)
- Use of **functions**, **if/elif/else**, **loops**, and **dictionaries**
- How to **visualise safety messages** using Turtle graphics
- Stretch challenge with **creative coding** and optional GUI/sensors

---

## 🔍 Workshop Outline

### 1. Introduction (10 min)
- Talk about summer heat and UV Index.
- Discuss sun safety and how we can help others.
- Introduce the idea of **building a sun safety alert system**.

### 2. Plan the System (10 min)
- Use a flowchart to map the logic.
- Identify inputs (temperature/UV), process (if/else), and outputs (warnings).

### 3. Code the Logic (20 min)
Create a function that takes two inputs
```python
def example_func(input1, input2):
  #do something input1
  #do something input2
```
We can use condiitons to check our inputs.    
One or more conditions can be checked.

```python
def sun_warning(temp, uv_index):
    if temp > 35 or uv_index > 8:
        return "🌡️ Extreme Heat/UV! Stay indoors and hydrate!"
    elif temp > 30 or uv_index > 6:
        return "☀️ Be cautious! Use sunscreen, wear a hat."
    else:
        return "😎 All clear. Enjoy the sun safely!"

print(sun_warning(33, 7))
```
- Let kids edit inputs, add messages, take user input with `input()`.

### 4. Looping Through Data (15 min)
```python
forecast = [
    {"day": "Monday", "temp": 34, "uv": 7},
    {"day": "Tuesday", "temp": 37, "uv": 9},
    {"day": "Wednesday", "temp": 28, "uv": 5},
]

for day in forecast:
    print(day["day"] + ": " + sun_warning(day["temp"], day["uv"]))
```
- Kids can add new days, change conditions, or sort alerts by severity.

---

## 🎨 Creative Stretch — Turtle Graphics (15 min)

### 🐢 Visualise a Safety Alert

1. Convert your favourite summer image to `.gif` and save it as `beach.gif`.
2. Use the Turtle module to overlay your warning message!

```python
import turtle

screen = turtle.Screen()
screen.title("Sun Safety Alert")
screen.setup(width=800, height=600)
screen.bgpic("beach.gif")  # Use your own beach.gif

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 200)

def display_message(message):
    pen.clear()
    pen.color("red")
    pen.write(message, align="center", font=("Arial", 24, "bold"))

# Example usage
display_message("🔥 EXTREME ALERT! Stay indoors & hydrate!")
screen.mainloop()
```

---

## ✅ Learning Outcomes

By the end of this workshop, students will:
- Understand how computers handle decision-making
- Be able to design a program from real-life needs
- See how code can be both **practical** and **artistic**
- Feel empowered to build their own safety or utility apps

---

## 💡 Next Steps (Optional)
- Use `tkinter` to make a GUI sun safety app.
- Hook up a micro:bit or Raspberry Pi with real sensors.
- Get data from a weather API and automate the system.

---

Happy summer coding! 🌊😎☀️
