
# Part 1
## Loading and understanding CSV files
<p>Load the dataset: Import pandas and load `retail_sales_data.csv` into a DataFrame called `df`. 
<p> Preview the data: Display the first 10 rows and the last 5 rows.
<p> Explore the dimensions: Find the number of rows and columns using `shape`.
<p> Inspect column names: Display all column names and their data types.
<p> Understand the structure: Use `info()` and explain what the output tells you.
<p> Select columns: Display only the `Product`, `Quantity`, and `Revenue` columns.
<p> Select rows: Display the first 15 transactions.
<p> Check data types: Confirm that `Date` is a date and `Revenue` is numeric. Convert `Date` using `pd.to_datetime()`.

# Part 2 
## Filtering and sorting
<p> Filter by category: Display only transactions in the Electronics category.
  ```
  
  ```python
electronics = df[df["Category"] == "Electronics"]

print(electronics.head(10))
````
<p> Filter by branch: Display transactions from the North branch.
<p> Combine conditions: Find Electronics transactions from the North branch.
<p> Filter by revenue: Display transactions with revenue greater than 50.
<p> Filter by discount: Find transactions with a discount of at least 10%.
<p> Sort by revenue: Display the 10 transactions with the highest revenue.
<p> Sort by quantity: Find transactions with the largest quantities sold.

# Part 3
## Descriptive statistics
<p> Calculate the mean: Find the average transaction revenue.
<p> Calculate the median: Find the median transaction revenue and compare it with the mean.
<p> Find the extremes: Find the minimum and maximum transaction revenue.
<p> Measure variability: Calculate the standard deviation of revenue.
<p> Summarise numeric columns: Use `describe()` and explain at least three statistics.
<p> Count transactions: Count the number of transactions for each payment method.
<p> Count products: Find how many transactions contain each product.

# Part 4 — Grouping and aggregation
<p> Revenue by category: Calculate total revenue for each product category.
<p> Revenue by branch: Calculate total revenue for each branch.
<p> Average revenue by branch: Compare average transaction revenue across branches.
<p> Quantity by product: Calculate the total quantity sold for each product.
<p> Most popular products: Identify the product with the highest total quantity sold.
<p> Payment method analysis: Calculate total revenue by payment method.
<p> Category and branch: Use `groupby()` with both `Category` and `Branch` to compare revenue.
<p> Rank the categories: Sort categories from highest to lowest total revenue.

# Part 5 — Dates and trends
<p> Extract the month: Create a `Month` column from the Date column.
<p> Monthly revenue: Calculate total revenue for each month.
<p> Find the best month: Identify the month with the highest revenue.
<p> Daily sales: Calculate total revenue for each date.
<p> Find the best sales day: Identify the date with the highest total revenue.
<p> Compare quarters: Create a quarter column and compare total revenue across quarters.

# Part 6 — Data quality and cleaning
<p> Find missing values: Use `isnull().sum()` to check every column.
<p> Find duplicate rows: Use `duplicated().sum()` to count duplicate rows.
<p> Check transaction IDs: Check whether `Transaction_ID` values are unique.
<p> Validate quantities: Check for zero or negative quantities.
<p> Validate prices: Check for zero or negative unit prices.
<p> Validate discounts: Check whether discounts fall between 0 and 1.
<p> Verify revenue: Calculate revenue again using quantity, price, and discount, then compare it with `Revenue`.
<p> Create a cleaned copy: Apply appropriate cleaning steps only when necessary, keeping the original DataFrame unchanged.

# Part 7 — Visualisation
<p> Bar chart: Plot total revenue by category.
<p> Horizontal bar chart: Plot total quantity sold by product.
<p> Histogram: Plot the distribution of transaction revenue.
<p> Box plot: Create a box plot of revenue and describe any potential outliers.
<p> Line chart: Plot monthly revenue over time.
<p> Pie chart: Visualise the proportion of transactions by payment method.
<p> Scatter plot: Plot quantity against revenue and describe the relationship.
<p> Improve chart design: Add a title, axis labels, readable category names, and suitable formatting to three charts.

# Part 8 — Independent analysis challenge
<p> Business question: Which product category should the store investigate for a sales improvement opportunity? Support your answer with evidence.
<p> Branch comparison: Which branch performs best in total revenue, and does it also have the highest average transaction revenue?
<p> Discount investigation: Compare revenue across discount levels. Explain why this comparison alone cannot establish whether discounts increase sales.
<p> Product performance: Identify products with high total revenue and products with high sales quantities. Are they the same?
<p> Executive summary: Write five evidence-based findings and recommend two actions the store could consider.
<p> Reproducible analysis: Put your code, charts, and conclusions in a well-organised Jupyter Notebook.
