
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


1. **Inspect the dataset**
   Find out how many rows and columns there are, and identify the types of data.

   ```python
   df.shape
   df.info()
   ```

2. **Look at the first and last records**
   Get a feel for what the data looks like.

   ```python
   df.head()
   df.tail()
   ```

3. **Calculate summary statistics**
   Find the mean, minimum, maximum, and spread of numerical variables.

   ```python
   df.describe()
   ```

4. **Count categories**
   Find out how many observations belong to each category.

   ```python
   df["class"].value_counts()
   ```

5. **Find the most and least common values**
   Investigate which values occur most frequently.

   ```python
   df["subject"].value_counts()
   ```

6. **Filter the data**
   Find records that meet a particular condition.

   ```python
   df[df["score"] > 80]
   ```

7. **Compare groups**
   Calculate statistics separately for different groups.

   ```python
   df.groupby("class")["score"].mean()
   ```

8. **Look for relationships**
   Investigate whether two numerical variables appear to be related.

   ```python
   df.plot.scatter(x="hours_studied", y="score")
   ```

9. **Find unusual values (outliers)**
   Look for observations that are unusually high or low.

   ```python
   df["score"].plot(kind="box")
   ```

10. **Make a data-driven discovery**
    Ask students to find **three interesting things** about the dataset and support each discovery with a calculation, table, or graph.

### A useful challenge

For the final task:

> **"Explore this dataset. Find something interesting, investigate it using Python, create a visualisation, and explain what you discovered."**


