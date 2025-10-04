# Simon Says
## 🎯 Learning Objectives (Bloom’s Taxonomy)

By the end of this lesson, pupils will be able to:

* 🔵 **Remembering**: Define what a sequence is.
* 🟢 **Understanding**: Describe how the Micro:bit can combine sound and lights.
* 🟡 **Applying**: Use Micro:bit buttons to repeat a sequence of sounds.
* 🟠 **Analysing**: Compare strategies for remembering sequences.
* 🔴 **Evaluating**: Justify which features make memory games fun or too challenging.
* 🟣 **Creating**: Design their own memory sequence game (e.g., faster speed, longer rounds, different tones).

---

## 🕒 Lesson Flow

---

### 1️⃣ Introduction (10 mins)

💬 **Discussion Questions**

* Have you ever played **Simon Says** or a memory game?
* What skills do you need to win?
* Where do we use memory in real life?

  * Learning songs 🎵
  * Remembering instructions 📝
  * Playing sports (remembering moves) ⚽

📌 **Highlight**:
This game trains **focus, listening, and pattern recognition**.

---

### 2️⃣ Problem Introduction (5–10 mins)

🌟 **Music Memory Problem**
We need to create a game where:

* Micro:bit plays a sequence of **lights + sounds**.
* The player copies the sequence using **button A** and **button B**.
* If the player is correct → sequence gets longer.
* If the player is wrong → ❌ Game Over.

💬 **Discussion Prompt**

* How can we make the game harder or easier?
* Should we add scoring?
* What should happen if you lose?

---

### 3️⃣ Coding the Solution (20–25 mins)

✅ **Step 1: Play a Single Note**

```python
from microbit import *
import music

music.play(['C4'])
display.show(Image.HEART)
```

👉 Flash it: Hear a note + see a light.

---

✅ **Step 2: Play a Random Sequence**

```python
import random

sequence = []
sequence.append(random.choice(['A', 'B']))
```

👉 Micro:bit chooses button A or B as the “note.”

---

✅ **Step 3: Show the Sequence**

```python
for move in sequence:
    if move == 'A':
        display.show(Image.ARROW_W)
        music.play(['C4'])
    else:
        display.show(Image.ARROW_E)
        music.play(['E4'])
    sleep(500)
    display.clear()
    sleep(200)
```

👉 Sequence shows as **arrows + notes**.

---

✅ **Step 4: Player Input**

```python
for move in sequence:
    correct = False
    while not correct:
        if button_a.was_pressed() and move == 'A':
            music.play(['C4'])
            correct = True
        elif button_b.was_pressed() and move == 'B':
            music.play(['E4'])
            correct = True
        elif button_a.was_pressed() or button_b.was_pressed():
            display.show(Image.SAD)
            music.play(['C3'])
            game_over = True
            break
```

👉 Player presses the right button for each note.

---

✅ **Step 5: Add Levels & Scoring**

```python
score = 0
game_over = False

while not game_over:
    # Add new move
    sequence.append(random.choice(['A', 'B']))
    
    # Show sequence
    for move in sequence:
        if move == 'A':
            display.show(Image.ARROW_W)
            music.play(['C4'])
        else:
            display.show(Image.ARROW_E)
            music.play(['E4'])
        sleep(500)
        display.clear()
        sleep(200)
    
    # Player turn
    for move in sequence:
        correct = False
        while not correct:
            if button_a.was_pressed() and move == 'A':
                music.play(['C4'])
                correct = True
            elif button_b.was_pressed() and move == 'B':
                music.play(['E4'])
                correct = True
            elif button_a.was_pressed() or button_b.was_pressed():
                display.show(Image.SAD)
                music.play(['C3'])
                game_over = True
                break
    
    # Update score
    if not game_over:
        score += 1

display.scroll("Score: " + str(score))
```

---

### 4️⃣ Testing & Reflection (10–15 mins)

💬 Ask Students:

* How many notes can you remember?
* What makes it difficult?
* Did you develop a memory strategy (e.g., humming, grouping)?

---

### 5️⃣ Extensions / Challenges

✨ Encourage students to:

* Add **more buttons** (gestures, shake = extra note).
* Speed up the sequence as levels increase.
* Add **LED patterns** instead of arrows.
* Add **bonus rounds** or special effects.
* Create a **high score tracker**.

---

## 📌 Wrap-Up

By the end of this lesson, pupils have:

* Learned how to combine **sound + visuals** on Micro:bit.
* Practised coding **loops and lists**.
* Tested their **memory skills**.
* Extended the game by designing new challenges.

---

👉 Would you like me to also make a **Student Handout version** (fill-in-the-blanks, simplified steps, space for their own sequences) for the Music Memory Game, like we did for Tilt Maze and Balance Game?


# Full Code
```python
from microbit import *
import music
import random

# Start variables
sequence = []
score = 0
game_over = False

while not game_over:
    # Add a new random move (A or B) to the sequence
    sequence.append(random.choice(['A', 'B']))

    # Show the sequence to the player
    for move in sequence:
        if move == 'A':
            display.show(Image.ARROW_W)  # Show arrow left for button A
            music.play(['C4'])           # Play note C4
        else:
            display.show(Image.ARROW_E)  # Show arrow right for button B
            music.play(['E4'])           # Play note E4
        sleep(500)
        display.clear()
        sleep(200)

    # Player repeats the sequence
    for move in sequence:
        correct = False
        while not correct:
            if button_a.was_pressed():  # Player presses A
                if move == 'A':
                    music.play(['C4'])
                    correct = True
                else:
                    display.show(Image.SAD)
                    music.play(['C3'])
                    game_over = True
                    break

            if button_b.was_pressed():  # Player presses B
                if move == 'B':
                    music.play(['E4'])
                    correct = True
                else:
                    display.show(Image.SAD)
                    music.play(['C3'])
                    game_over = True
                    break

        if game_over:  # If player made a mistake, stop checking further
            break

    # If player survived this round, increase score
    if not game_over:
        score += 1

# Show final score
display.scroll("Score: " + str(score))

   
```
