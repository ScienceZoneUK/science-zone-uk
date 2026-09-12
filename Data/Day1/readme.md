
# Exploratory Data Analysis
When working with data to find insights into possible patterns, an exploratory Data Analysis is done on data to see

Imagine you have a spreadsheet containing information about 1,000 students:

<p></p>Student	Age	Attendance	Hours studied	Exam score
<p></p>A	16	92%	5	78
<p></p>B	17	65%	2	51
<p></p>C	16	98%	7	91

<p></p>You don't yet know what the data is telling you.

So you explore it by asking questions such as:

<p></p>What is the average exam score?
<p></p>What is the highest score?
<p></p>Are there any unusual scores?
<p></p>Do students who study more tend to score higher?
<p></p>Does attendance appear related to exam results?
<p></p>Are there differences between different groups?


<p></p>

Data Sets

https://archive.ics.uci.edu/dataset/53/iris?utm_source=chatgpt.com

https://www.data.gov.uk/dataset/ea9b5b48-c757-4cec-9391-be90e260f249/schools_pupils_and_their_characteristics?utm_source=chatgpt.com



# The Task

```python
import pandas as pd

df = pd.read_csv("the_file.csv")
```



## Day 1 — Exploring Data with Python

### Getting started

First, install pandas:

```python
pip install pandas
```

Then import pandas:

```python
import pandas as pd
```

Load your dataset:

```python
df = pd.read_csv("the_file.csv")
```

> **Your mission:** Explore the dataset and discover **3 interesting things** about it.

---

### 1. How big is the dataset?

Find out how many **rows and columns** the dataset contains.

```python
df.shape
```

Now find out what type of data each column contains:

```python
df.info()
```

**Question:**
How many rows and columns are there?

---

### 2. What does the data look like?

Look at the first 5 rows:

```python
df.head()
```

Look at the last 5 rows:

```python
df.tail()
```

**Question:**
What information does each row represent?

---

### 3. What are the numbers telling us?

Calculate some basic statistics:

```python
df.describe()
```

Look at the:

* mean
* minimum
* maximum
* median
* spread

**Question:**
What is the most interesting statistic you found?

---

### 4. How many are in each category?

Choose a categorical column.

For example:

```python
df["class"].value_counts()
```

**Question:**
Which category has the most observations?

---

### 5. What is the most common value?

Choose another column:

```python
df["subject"].value_counts()
```

**Question:**
What is the most common value?

**Challenge:**
What is the least common value?

---

### 6. Can we filter the data?

Find records where a value is greater than 80:

```python
df[df["score"] > 80]
```

Try changing the number.

**Questions:**

* How many records have a score above 80?
* What happens if you change `80` to `50`?
* What happens if you use `<` instead of `>`?

---

### 7. Can we compare groups?

Calculate the average score for each class:

```python
df.groupby("class")["score"].mean()
```

**Question:**
Which class has the highest average score?

**Challenge:**
Can you find the lowest?

---

### 8. Can we find relationships?

Compare two numerical variables:

```python
df.plot.scatter(
    x="hours_studied",
    y="score"
)
```

**Questions:**

* Can you see a pattern?
* Do students who study more tend to have higher scores?
* Are there any unusual points?

---

### 9. Can we find unusual values?

Create a box plot:

```python
df["score"].plot(kind="box")
```

**Question:**
Are there any scores that look unusual?

These unusual observations are sometimes called **outliers**.

---

### 10. Become a data detective 🕵️

Now explore the dataset independently.

Find **3 interesting things** about the data.

For each discovery, you must provide:

**1. A question**

> Do students who study more get higher scores?

**2. Some Python**

```python
df.groupby("class")["score"].mean()
```

**3. Evidence**

A number, table or graph.

**4. A conclusion**

> Class Red has a higher average score than Class Blue.

### Final challenge

> **What is the most interesting thing you discovered in the dataset?**

And, importantly:

> **Does the data prove your explanation, or does it simply suggest a pattern?**

