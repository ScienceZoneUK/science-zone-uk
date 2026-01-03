## 1) Imports (what we’re using and why)

```python
import tkinter as tk
from tkinter import messagebox
import json
import random
from pathlib import Path
```

* **tkinter**: builds the GUI (window, buttons, labels, etc.)
* **messagebox**: popup dialogs (score/results)
* **json**: lets you load questions from a `questions.json` file
* **random**: shuffle questions for variety
* **Path**: easier file handling (`questions.json`)

---

## 2) Question bank (your quiz content)

The code includes built-in questions:

```python
DEFAULT_QUESTIONS = [
    {
        "question": "In Tkinter, which widget is best for single-line text input?",
        "choices": ["Entry", "Text", "Label", "Canvas"],
        "answer": 0,
    },
    {
        "question": "Which geometry manager uses rows and columns?",
        "choices": ["grid", "pack", "place", "after"],
        "answer": 0,
    },
    {
        "question": "What does mainloop() do?",
        "choices": [
            "Runs the event loop and keeps the GUI responsive",
            "Creates the main window",
            "Loads images",
            "Closes the app",
        ],
        "answer": 0,
    },
    {
        "question": "How do you run a function when a Button is clicked?",
        "choices": [
            "Use the button's command option",
            "Call it inside mainloop()",
            "Put it in the window title",
            "Use pack(command=...)",
        ],
        "answer": 0,
    },
    {
        "question": "Which widget is commonly used for a scrollable multi-line editor?",
        "choices": ["Text", "Entry", "Radiobutton", "Spinbox"],
        "answer": 0,
    },
    {
        "question": "What does after(ms, callback) do?",
        "choices": [
            "Schedules callback to run after ms milliseconds",
            "Blocks the UI for ms milliseconds",
            "Closes the app after ms milliseconds",
            "Runs callback immediately in a loop",
        ],
        "answer": 0,
    },
]

```

Each question is a dictionary with:

* `"question"`: the question text
* `"choices"`: list of choices (2 to 4)
* `"answer"`: index of the correct choice (0-based)

Example:

* `"answer": 0` means choice A is correct.

---

## 3) Optional: Load from `questions.json`

```python
QUESTIONS_JSON = Path("questions.json")
```

Then:

```python
def load_questions():
    if QUESTIONS_JSON.exists():
        try:
            data = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
            # Basic validation
            cleaned = []
            for q in data:
                if (
                    isinstance(q, dict)
                    and isinstance(q.get("question"), str)
                    and isinstance(q.get("choices"), list)
                    and isinstance(q.get("answer"), int)
                    and 2 <= len(q["choices"]) <= 4
                    and 0 <= q["answer"] < len(q["choices"])
                ):
                    cleaned.append(q)
            if cleaned:
                return cleaned
        except Exception:
            pass
    return DEFAULT_QUESTIONS
```

What this does:

* If `questions.json` exists, it tries to load questions from it.
* It **validates** the format (question is text, choices is a list, answer is a valid index).
* If file loading fails, it falls back to `DEFAULT_QUESTIONS`.

So you can expand the quiz **without editing code**.

---

## 4) The main app class (the whole GUI lives here)

```python
class QuizApp(tk.Tk):
    def __init__(self, questions, shuffle=True):
        super().__init__()
```

* `QuizApp` is your app window.
* `tk.Tk` is the Tkinter “main window” object.
* `super().__init__()` actually creates the window.

Then:

```python
self.questions = questions[:]
if shuffle:
    random.shuffle(self.questions)
```

* Makes a copy of questions
* Shuffles them if you want random order

---

## 5) Tracking state (important variables)

These store what’s happening in the quiz:

```python
self.index = 0                  # current question number
self.score = 0                  # computed at submit time
self.user_answers = [None] * len(self.questions)  # remembers answers
self.selected = tk.IntVar(value=-1)               # current selected option
```

Key idea:

* `IntVar` is a special Tkinter variable that connects to Radiobuttons.
* `value=-1` means “nothing selected”.

---

## 6) Building the UI (labels, buttons, radiobuttons)

### Title + progress

```python
self.header = tk.Label(self, text="Quiz", font=("Arial", 18, "bold"))
self.header.pack(pady=(14, 8))

self.progress = tk.Label(self, text="", font=("Arial", 11))
self.progress.pack()
```

* Header shows app title
* Progress shows “Question 3 of 10”

### Question text

```python
self.question_label = tk.Label(..., wraplength=580, justify="left")
```

* `wraplength` keeps long questions from going off-screen.

### Choices (Radiobuttons)

```python
self.radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(
        self.choices_frame,
        variable=self.selected,
        value=i,
        command=self.on_select
    )
```

Important:

* All Radiobuttons share `variable=self.selected`
* Each has a different `value=i`
* When clicked, `self.selected` becomes that `i`
* `command=self.on_select` runs when user picks an option

---

## 7) Navigation buttons (Previous / Next / Submit / Reset)

```python
self.prev_btn = tk.Button(..., command=self.prev_question)
self.next_btn = tk.Button(..., command=self.next_question)
self.submit_btn = tk.Button(..., command=self.submit)
self.reset_btn = tk.Button(..., command=self.reset)
```

Each button calls a function that updates state and redraws the UI.

---

## 8) Render function (the “display this question” function)

This is the core of the app:

```python
def render(self):
    q = self.questions[self.index]
    self.question_label.config(text=q["question"])
```

Then it updates choice text:

```python
choices = q["choices"]
for i, rb in enumerate(self.radio_buttons):
    if i < len(choices):
        rb.config(text=choices[i], state="normal")
    else:
        rb.pack_forget()
```

Why this exists:

* Some questions might only have 2 or 3 options.
* It hides extra buttons cleanly.

It also restores the previous answer:

```python
prev = self.user_answers[self.index]
self.selected.set(prev if prev is not None else -1)
```

So when you go back to a question, your selection is still there.

---

## 9) Saving the user’s selection

When user clicks a choice:

```python
def on_select(self):
    self.user_answers[self.index] = self.selected.get()
```

* `self.selected.get()` returns 0/1/2/3
* It stores that answer in the list at the current question index.

---

## 10) Next / Previous logic

### Next

```python
def next_question(self):
    if self.index == len(self.questions) - 1:
        self.submit()
        return
    self.index += 1
    self.render()
```

If on last question → finish submits.
Otherwise → go forward and re-render.

### Previous

```python
def prev_question(self):
    if self.index > 0:
        self.index -= 1
        self.render()
```

Go back and re-render.

---

## 11) Submit = scoring + results popup

```python
def submit(self):
    score = 0
    for i, q in enumerate(self.questions):
        if self.user_answers[i] == q["answer"]:
            score += 1
```

* It compares user answers vs correct answer index
* Calculates total

Then shows results:

```python
messagebox.showinfo("Result", f"Score: {score}/{total} ...")
```

It also builds a small “review” list (your answer vs correct).

---

## 12) Reset button

```python
def reset(self):
    self.index = 0
    self.user_answers = [None] * len(self.questions)
    self.selected.set(-1)
    self.render()
```

Starts everything over.

---

## 13) Starting the app

```python
if __name__ == "__main__":
    questions = load_questions()
    app = QuizApp(questions, shuffle=True)
    app.mainloop()
```

* Load questions (json if available, else defaults)
* Create the window
* `mainloop()` keeps the GUI alive and listening for clicks

---

If you want, I can rewrite it into **3 tiny files** (`app.py`, `quiz_engine.py`, `questions.json`) so it’s even easier to follow and edit.

