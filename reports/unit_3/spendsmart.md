# SQL Assignment Report

## SQL Queries:

```sql
SELECT username, email FROM user;
```

![SQL Querry](../../imgs/sql1.png)

```sql
SELECT user.username, user.user_id, credit_card_statements.amount 
FROM credit_card_statements JOIN user ON user.user_id = credit_card_statements.user_id;
```

![SQL Querry](../../imgs/sql2.png)

```sql
SELECT SUM(credit_card_statements.amount), credit_card_statements.user_id 
FROM credit_card_statements
GROUP BY user_id;
```

![SQL Querry](../../imgs/sql3.png)

```sql
SELECT * FROM utility_bills WHERE amount > 50;
```

![SQL Querry](../../imgs/sql4.png)

```sql
INSERT INTO user (username, email, password_hash)
VALUES ("pavel_polak","pavel_polak@test-email.com", "1901a15662db83ab4b9e9448b83ace0f2ba02b34a090711525018f65d42b0d67");
```

![SQL Querry](../../imgs/sql5.png)

```sql
UPDATE budget_categories
SET budget_limit = 500 WHERE user_id = 2 AND category_name = "Travel";
```

![SQL Querry](../../imgs/sql6.png)

```sql
DELETE FROM credit_card_statements WHERE amount < 10;
```

![SQL Querry](../../imgs/sql7.png)

```sql
/* select columns set alias */
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

![SQL Querry](../../imgs/sql8.png)

```sql
/* select columns set alias */
SELECT u.username, c.budget_limit, c.category_name, SUM(e.amount), c.budget_limit - SUM(e.amount) AS total_health_expense_remaining
FROM user_expenses AS e 

/* join tables */
INNER JOIN user AS u ON u.user_id = e.user_id
INNER JOIN budget_categories AS c ON e.category_id = c.budget_category_id

/* filter */
WHERE u.username = 'rhian_thompson-russel' AND e.category_id = 16 AND e.expense_date LIKE '2023-03%'
```

![SQL Querry](../../imgs/sql9.png)
