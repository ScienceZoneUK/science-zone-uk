# Web Coding Workshop for Ages 9–10: Build Your Own Horse Riding Website!

---

### 🐴 Welcome!
Today you will become a web coder! You'll learn how to build a website using something called HTML and CSS.
We will do this step by step, so don’t worry if you’ve never done it before.

We will also learn about why websites matter and how people use them to share ideas, hobbies, and more—including their love of **horse riding**!

---

### ✅ Step 1: What is the Web?
**Big Idea:** The Web is made up of lots of websites that people all over the world can visit.

**Simple Idea:** Think of websites like online posters or diaries you can click on.

**Tiny Bit of History:**
The web was invented by **Tim Berners-Lee** in 1989. He made it so people could share information using something called **HTML**.

---

### ✅ Step 2: Look at the Starting Website
Open the file called `index.html` and open it in your browser.

It might look simple at first, but don’t worry — we’re going to turn it into your very own **horse riding** site!

---

### ✅ Step 3: Change the Main Title
Find this line:
```html
<h1>My first website</h1>
```
Change it to say something like:
```html
<h1>My Horse Riding Adventures!</h1>
```

Also change the page title in the `<title>` tag near the top:
```html
<title>My Horse Riding Website</title>
```

---

### ✅ Step 4: Add a Section and Heading
Below the `<main>` tag, add this:
```html
<section>
  <h2>My Favourite Horse</h2>
</section>
```

**Why?**
This creates a new "part" of your website with its own title.

---

### ✅ Step 5: Add a Paragraph
Under the heading, add this:
```html
  <p>My favourite horse is Bella. She is calm, strong, and loves jumping over fences!</p>
```

**Semantic Tip:** A paragraph (`<p>`) is for writing your thoughts in sentences.

---

### ✅ Step 6: Add an Image
Still in your section, add this:
```html
  <img src="bella.png" alt="A beautiful brown horse named Bella" width="200">
```

**Semantic Tip:** `img` means image. The `alt` is a short description for people who can't see the picture.

---

### ✅ Step 7: Add Style with CSS
In the `<head>` part at the top, find these two lines and **uncomment** them:
```html
<link href="style.css" rel="stylesheet" type="text/css">
<link href="candy.css" rel="stylesheet" type="text/css">
```
**Remove the `<!--` and `-->` so they are active!**

**Big Idea:** CSS is like fashion for your website — it makes it look nice!

---

### ✅ Step 8: Change Your Heading Style
Open `style.css`. Find the part that says:
```css
h2 {
```
Add this line inside it:
```css
  text-align: center;
```
**This will move your subheading to the middle.**

---

### ✅ Step 9: Add Some Fancy Borders
In `index.html`, change your header tag like this:
```html
<header class="border-bottom secondary">
```
And change your footer like this:
```html
<footer class="border-top secondary">
```
This adds a thick top and bottom line and changes the colour.

---

### ✅ Step 10: Style the Middle
Make your main tag look like this:
```html
<main class="primary">
```
Now the middle of your page will use the primary background colour!

---

### ✅ Step 11: Style Your Section
Find your `<section>` with Bella the horse. Change it to:
```html
<section class="tertiary">
```
And change the paragraph inside to:
```html
<p class="xcenter">My favourite horse is Bella. She is calm, strong, and loves jumping over fences!</p>
```

**Now it looks more colourful and is centred!**

---

### ✅ Step 12: Make the Image Fancy
Find your `<img>` tag and change it to:
```html
<img src="bella.png" class="dashed-border rounded" alt="A beautiful brown horse named Bella" width="200">
```
Now it has a cool border and rounded corners.

---

### ✅ Step 13: Try a Different Look
Find the line in `<head>` that says:
```html
<link href="candy.css" rel="stylesheet" type="text/css">
```
Change `candy.css` to `vivid.css` to try a different style.

---

### ✅ Step 14: Add a List
Let’s add a list of your horse riding activities!
Inside your section, under the paragraph, add:
```html
<h3>Things I Love About Horse Riding:</h3>
<ul>
  <li>Going on long trail rides</li>
  <li>Jumping over small fences</li>
  <li>Brushing Bella's shiny coat</li>
</ul>
```

**Semantic Tip:** A list (`<ul>` and `<li>`) is great for showing many ideas clearly.

---

### ✅ Step 15: Add More Horse Friends!
Now add two more sections like this:

```html
<section class="secondary">
  <h2>Storm</h2>
  <img src="storm.png" class="rounded" width="200">
  <p class="xcenter">Storm is super fast and loves to gallop!</p>
</section>

<section class="tertiary">
  <h2>Twilight</h2>
  <img src="twilight.png" class="dashed-border rounded" width="200">
  <p class="xcenter">Twilight has a soft mane and loves cuddles!</p>
</section>
```

---

### 🏇 You're a Web Wizard!
You made your own website all about horse riding!

You now know how to:
- Add titles, sections, and paragraphs
- Insert images and descriptions
- Style everything with CSS
- Use lists to show your favourite things

You even learned about the history of the web!

Well done, young coder! 🐎💻
