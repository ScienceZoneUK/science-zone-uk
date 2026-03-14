# 📘 **SQL Lesson Note: Essential Queries & Explanations (Using the *sales* Table)**

Your **sales** table contains columns such as  
`Region, Country, Item_Type, Sales_Channel, Order_Priority, Order_Date, Ship_Date, Units_Sold, Unit_Price, Unit_Cost, Total_Revenue, Total_Cost, Total_Profit`  
(based on the cleaned dataset loaded into `sales.db`). 

Below is a structured list of SQL queries with clear explanations, perfect for a classroom session.

***

# 🔹 **1. View All Data**

```sql
SELECT * FROM sales;
```

**Explanation:**  
Shows all rows and columns in the table. Perfect as a first step so students can see the dataset’s structure.  
(Dataset sourced from *sales.csv*.) [\[sales \| Excel\]](https://chamberlayneorg-my.sharepoint.com/personal/fonwuchekwa_westonsecondary_co_uk/_layouts/15/Doc.aspx?sourcedoc=%7BE1B65BC7-444D-41F3-983E-16434C04903D%7D&file=sales.csv&action=default&mobileredirect=true)

***

# 🔹 **2. Count Total Records**

```sql
SELECT COUNT(*) AS total_rows FROM sales;
```

**Explanation:**  
Counts how many sales transactions exist.  
(This dataset contains 100 rows.) 

***

# 🔹 **3. Find the Earliest & Latest Order Dates**

```sql
SELECT MIN(Order_Date) AS first_order,
       MAX(Order_Date) AS last_order
FROM sales;
```

**Explanation:**  
Helps students understand date range.  
(This dataset ranges from 2010‑02‑02 to 2017‑05‑22.) 

***

# 🔹 **4. Calculate Total Revenue, Cost & Profit**

```sql
SELECT
  SUM(Total_Revenue) AS revenue,
  SUM(Total_Cost) AS cost,
  SUM(Total_Profit) AS profit
FROM sales;
```

**Explanation:**  
Shows how aggregation functions help with business KPIs.  
(Your dataset totals: £137M revenue, £93M cost, £44M profit.) 

***

# 🔹 **5. Group Sales by Country**

```sql
SELECT Country,
       SUM(Total_Revenue) AS revenue
FROM sales
GROUP BY Country
ORDER BY revenue DESC;
```

**Explanation:**  
Teaches `GROUP BY` and ordering results.  
(Honduras, Myanmar, Djibouti, Turkmenistan, Mexico are top 5.) 

***

# 🔹 **6. Compare Online vs Offline Sales**

```sql
SELECT Sales_Channel,
       COUNT(*) AS orders,
       SUM(Total_Revenue) AS revenue,
       SUM(Total_Profit) AS profit
FROM sales
GROUP BY Sales_Channel;
```

**Explanation:**  
Shows categorical comparison.  
(This dataset has 50 offline & 50 online orders.) 

***

# 🔹 **7. Analyse Most Profitable Item Types**

```sql
SELECT Item_Type,
       SUM(Total_Revenue) AS revenue,
       SUM(Total_Profit) AS profit,
       ROUND(100.0 * SUM(Total_Profit) / SUM(Total_Revenue), 2) AS margin_pct
FROM sales
GROUP BY Item_Type
ORDER BY margin_pct DESC;
```

**Explanation:**  
Demonstrates grouped calculations & derived columns.  
(Clothes has the highest margin; Meat the lowest.) 

***

# 🔹 **8. Monthly Revenue Trend**

```sql
SELECT SUBSTR(Order_Date, 1, 7) AS year_month,
       SUM(Total_Revenue) AS revenue,
       SUM(Total_Profit) AS profit
FROM sales
GROUP BY year_month
ORDER BY year_month;
```

**Explanation:**  
Shows how to extract parts of dates and build time‑series analysis.

***

# 🔹 **9. Shipping Lead Time (Days)**

```sql
SELECT ROUND(AVG(julianday(Ship_Date) - julianday(Order_Date)), 2) AS avg_ship_days
FROM sales;
```

**Explanation:**  
Demonstrates date arithmetic with SQLite.  
(Average ship time in this dataset: **23.36 days**.) 

***

# 🔹 **10. Orders by Priority**

```sql
SELECT Order_Priority,
       COUNT(*) AS orders,
       SUM(Total_Revenue) AS revenue
FROM sales
GROUP BY Order_Priority
ORDER BY revenue DESC;
```

**Explanation:**  
Teaches how categorical levels affect performance.

***

# 🔹 **11. Filter Sales for One Country**

```sql
SELECT *
FROM sales
WHERE Country = 'Mexico';
```

**Explanation:**  
Shows basic filtering with `WHERE`.  
(Mexico appears multiple times in your dataset.) [\[sales \| Excel\]](https://chamberlayneorg-my.sharepoint.com/personal/fonwuchekwa_westonsecondary_co_uk/_layouts/15/Doc.aspx?sourcedoc=%7BE1B65BC7-444D-41F3-983E-16434C04903D%7D&file=sales.csv&action=default&mobileredirect=true)

***

# 🔹 **12. Find High‑Profit Orders Only**

```sql
SELECT *
FROM sales
WHERE Total_Profit > 500000
ORDER BY Total_Profit DESC;
```

**Explanation:**  
Good example of numeric filters and sorting.

***

# 🔹 **13. Show Only Online Cosmetic Sales**

```sql
SELECT *
FROM sales
WHERE Sales_Channel = 'Online'
  AND Item_Type = 'Cosmetics';
```

**Explanation:**  
Teaches combining multiple conditions using `AND`.

***

# 🔹 **14. Sort Items by Units Sold**

```sql
SELECT Country, Item_Type, Units_Sold
FROM sales
ORDER BY Units_Sold DESC;
```

**Explanation:**  
Shows ordering based on numeric columns.

***

# 🔹 **15. Calculate Unit Profit per Item**

```sql
SELECT Item_Type,
       AVG(Unit_Price - Unit_Cost) AS avg_unit_profit
FROM sales
GROUP BY Item_Type
ORDER BY avg_unit_profit DESC;
```

**Explanation:**  
Demonstrates computed expressions inside queries.

***

