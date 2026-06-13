
#  Random Joke Generator (API Project)

## 🎯 Goal

Build a small app that:

* Fetches a random joke from an API
* Displays it on screen
* Lets the user get a new joke with a button

You’ll learn:

* GET requests
* Handling JSON
* DOM updates (or React state)
* Async/await

---

# 🔌 Joke API (Free & Simple)

Use this API:

👉 [https://official-joke-api.appspot.com/random_joke](https://official-joke-api.appspot.com/random_joke)

It returns data like:

```json
{
  "setup": "Why don't scientists trust atoms?",
  "punchline": "Because they make up everything!"
}
```



---

# 🧱 Version 1: HTML + JavaScript (Simple)

## 📄 index.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>Random Joke Generator</title>
</head>
<body>

  <h1>Joke Generator</h1>

  <div id="joke">
    Click the button to get a joke!
  </div>

  <button onclick="getJoke()">Get Joke</button>

  <script src="app.js"></script>
</body>
</html>
```

---

## ⚙️ app.js

```js
async function getJoke() {
  const response = await fetch("https://official-joke-api.appspot.com/random_joke");
  const data = await response.json();

  const jokeText = `${data.setup} 😆 ... ${data.punchline}`;

  document.getElementById("joke").innerText = jokeText;
}
```

---

# 🧪 What’s Happening

* `fetch()` → calls the API
* `await response.json()` → converts response into usable data
* You extract:

  * `setup` (first part)
  * `punchline` (joke ending)
* Then update the page

---

# 🎨 Version 2: Improve UI

Add basic styling:

```html
<style>
  body {
    font-family: Arial;
    text-align: center;
    margin-top: 100px;
  }

  #joke {
    margin: 20px;
    font-size: 20px;
  }

  button {
    padding: 10px 20px;
    cursor: pointer;
  }
</style>
```

---

# ⚛️ Version 3: React Version (Optional Upgrade) Actually don't do this but if you manage to get it right on you get #10 next lesson

```jsx
import { useState } from "react";

export default function JokeApp() {
  const [joke, setJoke] = useState("");

  const getJoke = async () => {
    const res = await fetch("https://official-joke-api.appspot.com/random_joke");
    const data = await res.json();
    setJoke(`${data.setup} ... ${data.punchline}`);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>😂 Joke Generator</h1>

      <p>{joke || "Click the button to get a joke!"}</p>

      <button onClick={getJoke}>Get Joke</button>
    </div>
  );
}
```

