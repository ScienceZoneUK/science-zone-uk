

## 🔢 What it does

* ➕ Increment
* ➖ Decrement
* 🔄 Reset
* 🎨 Color changes based on value

---

# Step 1 
Go to VS Code or any coding editor of your choice and create the following files: "index.html", "style.css" and "script.js"


# Step 2 
The following "html" and "css" code to their respective files


## 🧱 HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Counter App</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <div class="container">
    <h1>Counter</h1>
    <span id="value">0</span>

    <div class="buttons">
      <button id="decrease">Decrease</button>
      <button id="reset">Reset</button>
      <button id="increase">Increase</button>
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

---

## 🎨 CSS

```css
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: Arial, sans-serif;
  background: #f4f4f4;
}

.container {
  text-align: center;
  background: white;
  padding: 30px;
  border-radius: 10px;
  width: 300px;
}

#value {
  font-size: 4rem;
  display: block;
  margin: 20px 0;
}

.buttons button {
  padding: 10px 15px;
  margin: 5px;
  cursor: pointer;
}
```

---

## ⚙️ JavaScript (DOM)

```javascript
let count = 0;

const value = document.getElementById("value");
const increaseBtn = document.getElementById("increase");
const decreaseBtn = document.getElementById("decrease");
const resetBtn = document.getElementById("reset");

increaseBtn.addEventListener("click", () => {
  count++;
  updateCounter();
});

decreaseBtn.addEventListener("click", () => {
  count--;
  updateCounter();
});

resetBtn.addEventListener("click", () => {
  count = 0;
  updateCounter();
});

function updateCounter() {
  value.textContent = count;

  if (count > 0) {
    value.style.color = "green";
  } else if (count < 0) {
    value.style.color = "red";
  } else {
    value.style.color = "black";
  }
}
```

---

## 🚀 DOM concepts you just used

* `getElementById`
* `addEventListener`
* `textContent`
* `style` manipulation
* Event handling

---
