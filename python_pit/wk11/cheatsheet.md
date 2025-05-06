# Pandas



## Cheat sheet

Import library
- import pandas as pd
- Create a data frame(df) ```df = pd.DataFrame(...some data....) ```
```python
df = pd.DataFrame(
{"a" : [4, 5 , 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])
```
Another way: create the dictionary first
```python
data = {
    "a": [4,5,6],
    "b": [7,8,9],
    "c": [10,11,12]
}
df = pd.DataFrame(data, index = [1,2,3])
```
- #1 Print the first 5 rows of data (detective work)
- #2 Print the whole data frame
- #3 Print Column names
```python
#1
df.head()

#2
print(df)

#3
print(df.columns)

```
- Get statistics from your data frame

```python
print(df.describe())
```
