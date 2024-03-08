# SQL Assignment Report

## SQL Queries:


```sql

```

![SQL Querry](../../imgs/sql1.png)

```sql

```

![SQL Querry](../../imgs/sql2.png)

```sql

```

![SQL Querry](../../imgs/sql3.png)

```sql

```

![SQL Querry](../../imgs/sql4.png)

```sql

```

![SQL Querry](../../imgs/sql5.png)

```sql

```

![SQL Querry](../../imgs/sql6.png)

```sql

```

![SQL Querry](../../imgs/sql7.png)

```sql

```

![SQL Querry](../../imgs/sql8.png)

```sql

SELECT u.user_id, u.username, c.category_name AS travel_category, SUM(e.amount) AS total_travel_expense
FROM user AS u

/* join tables */
INNER JOIN user_expenses AS e ON u.user_id = e.user_id
INNER JOIN budget_categories AS c ON e.category_id = c.budget_category_id

/* filter */
WHERE c.category_name LIKE 'Travel'

/* group results */
GROUP BY u.user_id, u.username, c.category_name
```

![SQL Querry](../../imgs/sql9.png)

```sql

```

![SQL Querry](../../imgs/sql10.png)
