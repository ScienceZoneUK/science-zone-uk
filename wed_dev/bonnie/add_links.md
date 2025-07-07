# 🌐 Workshop: “Make Your Website Click!”
*Learn how to add buttons that take you to new pages!*

---

## 🧠 What is a Link?

> Have you ever clicked on a button or word and it *magically* took you to a new page? That’s called a **link**!  
> Links are like **doors** that let you travel between different parts of a website.  
>
> Today, we’re going to make those doors for *our* site — so when someone clicks ‘About Me’ or ‘Tips,’ they zoom straight to that page. Cool, right?

---

## 🧰 What You Need

- `index.html` — your homepage  
- `about.html` — a new page we’ll link to  
- `style.css` — already has the colours and button styles  
- A browser (like Chrome)  
- A code editor (like VS Code or Replit)

---

## ✅ Step 1: Add the Navigation Bar (Magic Buttons!)

👩‍💻 Open `index.html` and find the part that looks like this:

```html
<header class="border-bottom secondary">
  <h1>May's Horse Tips</h1>
</header>
```

Now change it to this:

```html
<header class="border-bottom secondary">
  <h1>May's Horse Tips</h1>
  <nav class="topnav">
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="about.html">About Me</a></li>
    </ul>
  </nav>
</header>
```

🪄 That adds two buttons at the top: **Home** and **About Me**.  
When you click one — it opens that page!

---

## ✅ Step 2: Add the Same Nav to the Other Page

👩‍💻 Open `about.html`.  
Look for this part:

```html
<header class="border-bottom secondary">
  <h1>About</h1>
</header>
```

Now change it to the same thing we added before:

```html
<header class="border-bottom secondary">
  <h1>About</h1>
  <nav class="topnav">
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="about.html">About Me</a></li>
    </ul>
  </nav>
</header>
```

✅ Now this page has the same magic buttons!

---

## ✅ Step 3: Try It Out!

1. Click on `index.html` in your folder and open it in your web browser.
2. Click the **About Me** button.
3. Ta-da! You should land on the About page.
4. Click **Home** to go back.

---

## 🎨 Extra Fun

Let’s change how our buttons look!

👩‍🎨 Open `style.css`  
Scroll to the bottom and add:

```css
html {
  scroll-behavior: smooth;
}

.topnav a:hover {
  transform: scale(1.1);
}
```

That makes your buttons zoom a little when you hover!

---

## 🎓 What We Learned

- What a **link** is  
- How to make a **nav bar** with links  
- How to make **more pages**  
- How to **go back and forth** between them!

---

## 💬 Teacher Tip

Wrap up by asking:
> “What page would *you* like to add next?” (e.g., “My Pets”, “My Hobbies”, “My Art”)
